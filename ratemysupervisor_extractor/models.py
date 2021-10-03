from datetime import datetime
from json_fix import fix_it
from typing import Optional

fix_it()


class _Serializable:
    def __json__(self):
        return self.__dict__


class Supervisor(_Serializable):
    def __init__(self, school_cate: str, university: str, department: str, supervisor: str):
        self.school_cate = school_cate
        self.university = university
        self.department = department
        self.supervisor = supervisor


class Comment(_Serializable):
    class Rates(_Serializable):
        def __init__(self, academic_level: float = None, research_budget: float = None, relationship: float = None,
                     student_development: float = None):
            self.academic_level = academic_level
            self.research_budget = research_budget
            self.relationship = relationship
            self.student_development = student_development

        def average(self) -> Optional[float]:
            valid_rates = {}
            for key in self.__dict__:
                value = self.__dict__[key]
                if value is not None:
                    valid_rates[key] = value
            if not valid_rates:
                return None
            return sum(valid_rates.values()) / len(valid_rates)

    def __init__(self, supervisor: Supervisor, description: str, date: datetime, rate: float = None,
                 rates: Rates = None, counts: int = 0):
        self.supervisor = supervisor
        self.description = description
        self.date = date
        self.counts = counts
        if rate is None and rates is None:
            raise TypeError('At least one of parameters rate, rates are required')
        elif rate is None:
            self.rate = rates.average()
            self.rates = rates
        elif rates is None:
            self.rate = rate
            self.rates = Comment.Rates()
        else:
            self.rate = rate
            self.rates = rates

    def __json__(self):
        json = super(Comment, self).__json__().copy()
        json.update(self.supervisor.__json__())
        json['date'] = json['date'].strftime('%Y-%m')
        return json
