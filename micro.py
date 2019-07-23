"""Mock implementation of a basic microprocessor.

"""

class Register(int):
    """An internal processor register"""
    

a = Register()
print(a)
print(a.__sizeof__())
print(type(a))

class StatusReg(Register):
    def __init__(self):
        pass

class Counter(Register):
    """A processor counter."""
    def __init__(self, bits=4):
        self.bits = bits

class ALU(object):
    """ Basic four bit arithmetic logic unit."""
    def __init__(self, bits=4, a=0, b=0):
        self.bits = bits
