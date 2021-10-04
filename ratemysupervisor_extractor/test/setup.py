# Test resources
TEST_SOURCE_FILE = 'ratemysupervisor_extractor/test/resources/ratemysupervisor-tokiwadai.txt'
TEST_EXPECTED_FILE = 'ratemysupervisor_extractor/test/resources/ratemysupervisor-tokiwadai-expected.json'

# Additional options
SCHOOL_CATE = 'School District 7, Academy City'
UNIVERSITY = 'School Garden'
FILE_OPTIONS = {
    'encoding': 'utf-8',
}
JSON_OPTIONS = {
    'sort_keys': True,
    'ensure_ascii': True,
    'indent': 2,
}
