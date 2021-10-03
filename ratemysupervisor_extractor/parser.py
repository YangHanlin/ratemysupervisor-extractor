import re
from typing import Iterable, Union, TextIO
from .models import Comment, Supervisor
from datetime import datetime

_SUPERVISOR_SEPARATOR = '********************************************************************************'
_COMMENT_SEPARATOR = '------------------'

_SOURCE_HEADER_PATTERN = re.compile(r'.*\s*.*\s+(?P<department>.*)\s*')
_SUPERVISOR_HEADER_PATTERN = re.compile(r'\s*Name:(?P<supervisor_name>.*)\s*')
_COMMENT_PATTERN = re.compile(
    r'\s*评星\(满分5星\) 学术水平:(?P<rate_academic_level>\d+|未填) 科研经费:(?P<rate_research_budget>\d+|未填) 师生关系:('
    r'?P<rate_relationship>\d+|未填) 学生前途:(?P<rate_student_development>\d+|未填)\s*(?P<description>.*)\s*(?P<date>\d{4}-\d{'
    r'2})\s*', re.DOTALL)


def parse(source: Union[str, TextIO], school_cate: str = None, university: str = None) -> Iterable[Comment]:
    if not isinstance(source, str):
        source = source.read()
    comments = []
    supervisor_sections = source.split(_SUPERVISOR_SEPARATOR)
    department = re.match(_SOURCE_HEADER_PATTERN, supervisor_sections[0]).groupdict()['department']
    for supervisor_section in supervisor_sections[1:]:
        comment_sections = supervisor_section.split(_COMMENT_SEPARATOR)
        supervisor_name = re.match(_SUPERVISOR_HEADER_PATTERN, comment_sections[0]).groupdict()['supervisor_name']
        supervisor = Supervisor(school_cate, university, department, supervisor_name)
        for comment_section in comment_sections[1:]:
            comment_data = re.match(_COMMENT_PATTERN, comment_section).groupdict()
            rates = Comment.Rates(_parse_rate(comment_data['rate_academic_level']),
                                  _parse_rate(comment_data['rate_research_budget']),
                                  _parse_rate(comment_data['rate_relationship']),
                                  _parse_rate(comment_data['rate_student_development']))
            comment = Comment(supervisor, comment_data['description'],
                              datetime.strptime(comment_data['date'], '%Y-%m'), rates=rates)
            comments.append(comment)
    return comments


def _parse_rate(rate: str):
    if rate == '未填':
        return None
    return int(rate)
