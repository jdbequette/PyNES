"""
Indexed addressing with Y-Register
"""
size = 2


def read(cpu, param):
    return cpu.memory.read(param + cpu.registers['y'].read())


def write(cpu, param, value):
    cpu.memory.write(param + cpu.registers['y'].read(), value)


def print(param):
    return "{0:#06x}, Y".format(param)
