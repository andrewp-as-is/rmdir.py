__all__ = ['rmdir']


import os


def dirs(path):
    for root, dirs, files in os.walk(path):
        for d in dirs:
            yield os.path.join(root, d)


def isempty(path):
    return len(os.listdir(path)) == 0


def rmdir(path):
    """recursively delete empty directories"""
    path = os.path.abspath(os.path.expanduser(path))
    for _dir in reversed(list(dirs(path))):
        if isempty(_dir):
            os.rmdir(_dir)
