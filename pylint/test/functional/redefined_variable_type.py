"""Checks variable types aren't redefined within a method or a function"""

# pylint: disable=too-few-public-methods, missing-docstring, unused-variable

_OK = True

class MyClass(object):
    def __init__(self):
        self.var = True
        self.var1 = 2
        self.var2 = 1.
        self.var1 = 2.  # [redefined-variable-type]
        self.a_str = "hello"
        a_str = False
        (a_str, b_str) = (1, 2)
        a_str = 2.0 if self.var else 1.0

    def _getter(self):
        return self.a_str
    def _setter(self, val):
        self.a_str = val
    var2 = property(_getter, _setter)

    def some_method(self):
        self.var = 1
        test = 'foo'
        myint = 2
        myint = False  # [redefined-variable-type]

_OK = "This is OK"  # [redefined-variable-type]

SOME_FLOAT = 1.

def dummy_function():
    return 2

def other_function():
    instance = MyClass()
    instance = True  # [redefined-variable-type]

SOME_FLOAT = dummy_function()  # [redefined-variable-type]

A_GLOB = None
A_GLOB = [1, 2, 3]
