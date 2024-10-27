# -*- coding: utf-8 -*-
import sys


def main():
    if len(sys.argv) == 1:
        mips_registers_path = '../docs/mips_registers.txt'
        logisim_log_path = '../docs/logisim_registers.txt'
    elif len(sys.argv) == 3:
        mips_registers_path = str(sys.argv[1])
        logisim_log_path = str(sys.argv[2])
    else:
        print("Wrong argument!")
        return

    logisim_registers = [0] * 32
    mips_registers = [0] * 32

    with open(logisim_log_path, 'r') as logisim_file:
        logisim_lines = logisim_file.readlines()

        line1 = logisim_lines[-1]
        for i, x in enumerate(line1.split('\t')):
            logisim_registers[i] = int(x.replace(' ', ''), 16)

    with open(mips_registers_path, 'r') as mips_file:
        mips_lines = mips_file.readlines()
        for line in mips_lines:
            if line == '\n' or not line.startswith('$'):
                # 忽略空行
                continue
            reg, value = line.split('\t')
            reg_mark = int(reg[1:])
            value_int = int(value[2:], 16)
            mips_registers[reg_mark] = value_int


    if mips_registers == logisim_registers:
        print("Two registers are the same!!!")
    else:
        print("Two registers are different!!!")
        print("mips registers:", mips_registers)
        print("logisim registers:", logisim_registers)
        print("Mistakes:")
        for i, (x, y) in enumerate(zip(mips_registers, logisim_registers)):
            if x != y:
                print("register $" + str(i), "|| mips register", hex(x), "|| logisim register", hex(y))


if __name__ == '__main__':
    main()
