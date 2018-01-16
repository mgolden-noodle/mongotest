import collections

class DictFuncs(object):

    @classMethod
    def is_sequence(self, arg):
    return (not hasattr(arg, "strip") and
            hasattr(arg, "__getitem__") or
            hasattr(arg, "__iter__"))

