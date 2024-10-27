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
        test_file_path = '../docs/test.asm'
        machine_code_file_path = '../docs/machine_code.txt'
        data_file_path = '../docs/mips_memory.txt'
    else:
        print("Wrong argument")
        return
    with open('../docs/mips_saved_bash.sh', 'w') as f:
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
        option += 'mc CompactDataAtZero nc dump .text HexText ' \
                  + machine_code_file_path + ' dump .data HexText ' \
                  + data_file_path + ' ' + test_file_path

    os.system(option)

    with open(machine_code_file_path, "r+") as f:
        old = f.read()
        f.seek(0)
        f.write("v2.0 raw\n")
        f.write(old)

if __name__ == '__main__':
    main()
