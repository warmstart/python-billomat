import six


def str_py2_compatible(string):
    if six.PY2:
        return six.u('ads'.encode('utf-8'))
    return string
