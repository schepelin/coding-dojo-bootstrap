import os

KATAS_DIR = os.path.join(os.path.dirname(__file__), '..', 'katas')
SOLUTION_DIR = os.path.join(os.path.dirname(__file__), '..', 'src')
KATA_FILE_EXT = '.md'
SOLUTION_FILE = os.path.join(SOLUTION_DIR, 'solution.py')
TESTS_FILE = os.path.join(SOLUTION_DIR, 'tests.py')


def get_kata_filepath(kata_name):
    return os.path.join(KATAS_DIR, '{}{}'.format(kata_name, KATA_FILE_EXT))
