import os
import sys


# 自动生成并运行指令
def main():
    option = ''
    if len(sys.argv) == 4:
        test_file_path = str(sys.argv[1])
        machine_code_file_path = str(sys.argv[2])
        data_file_path = str(sys.argv[3])
    elif len(sys.argv) == 1:
        test_file_path = 'test.asm'
        machine_code_file_path = 'machine_code.txt'
        data_file_path = 'mips_memory.txt'

    with open('mips_saved_bash.sh', 'w') as f:
        f.write('java -jar Mars4_5.jar ')
        option += 'java -jar Mars4_5.jar '
        registers = '$x'
        begin = 0
        end = 26
        for x in range(begin, end):
            f.write(registers.replace('x', str(x)) + ' ')
            option += registers.replace('x', str(x)) + ' '
        f.write('mc CompactDataAtZero nc dump .text HexText '
                + machine_code_file_path +
                ' dump .data HexText '
                + data_file_path + ' ' + test_file_path)
        option += 'mc CompactDataAtZero nc dump .text HexText ' + machine_code_file_path + ' dump .data HexText ' + data_file_path + ' ' + test_file_path

    os.system(option)


if __name__ == '__main__':
    main()
