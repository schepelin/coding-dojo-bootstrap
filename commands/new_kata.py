from string import Template

from commands import get_kata_filepath, SOLUTION_FILE, TESTS_FILE

__all__ = (
    'build_boilerplate',
)


SrcTempalte = Template("""\"""
$kata_desription
\"""


def solution(input):
    # Your code here
    pass
""")


TestTempalte = Template("""import unittest

from .solution import solution


class KataTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_solution(self):
        self.assertTrue(False)
""")


def get_kata_description(kata_name):
    path = get_kata_filepath(kata_name)
    with open(path) as f:
        description = f.read()
    return description


def write_solution_file(name):
    with open(SOLUTION_FILE, 'w') as f:
        f.write(SrcTempalte.substitute(kata_desription=get_kata_description(name)))


def write_test_file(name):
    with open(TESTS_FILE, 'w') as f:
        f.write(TestTempalte.substitute())


def build_boilerplate(name):
    write_solution_file(name)
    write_test_file(name)
