import six


def str_py2_compatible(string):
    if six.PY2:
        return str(string, encoding = "utf-8")
    return string
