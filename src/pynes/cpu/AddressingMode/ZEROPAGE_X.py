__author__ = 'misha'

size = 1


def read(cpu, param):
    address = param + cpu.registers['x'].read()
    return cpu.memory.read(address), 0


def write(cpu, param, value):
    address = param + cpu.registers['x'].read()
    cpu.memory.write(address, value)


def print(param):
    return "{0:#04x},X".format(param)