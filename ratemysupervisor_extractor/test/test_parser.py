import json
from unittest import TestCase
from .setup import *
from ..core.parser import *


class ParserTest(TestCase):
    def setUp(self) -> None:
        with _open_file(TEST_EXPECTED_FILE) as f:
            self.expected_text = f.read()
        with _open_file(TEST_SOURCE_FILE) as f:
            self.source_text = f.read()
        self.maxDiff = None

    def test_parse_text(self):
        actual_text = _to_json(parse_text(self.source_text, school_cate=SCHOOL_CATE, university=UNIVERSITY))
        self.assertEquals(self.expected_text, actual_text)

    def test_parse_file(self):
        with _open_file(TEST_SOURCE_FILE) as f:
            actual_text = _to_json(parse_file(f, school_cate=SCHOOL_CATE, university=UNIVERSITY))
            self.assertEquals(self.expected_text, actual_text)

    def test_parse_file_path(self):
        actual_text = _to_json(parse_file(TEST_SOURCE_FILE, school_cate=SCHOOL_CATE, university=UNIVERSITY, **FILE_OPTIONS))
        self.assertEquals(self.expected_text, actual_text)


def _to_json(obj) -> str:
    return json.dumps(obj, **JSON_OPTIONS)


def _open_file(path):
    return open(path, 'r', **FILE_OPTIONS)
