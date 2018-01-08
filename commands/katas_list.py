import os
from commands import KATAS_DIR, KATA_FILE_EXT

__all__ = (
    'get_katas_list',
)


def is_kata(filepath):
    _, ext = os.path.splitext(filepath)
    conditions = (
        os.path.isfile(os.path.join(KATAS_DIR, filepath)),
        ext == KATA_FILE_EXT,
    )
    return all(conditions)


def get_katas_list():
    return [os.path.splitext(f)[0] for f in os.listdir(KATAS_DIR) if is_kata(f)]
