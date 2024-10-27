import os
# 该程序用于生成logisim源文件和测试文件的结果
import sys
def main():
    test_circ_path = '../standard_cpu/cpu_test.circ'
    standard_cpu_path = '../standard_cpu/cpu.circ'
    machine_code_path = '../docs/machine_code.txt'
    right_ans_path = '../docs/right_ans.xls'
    my_ans_path = '../docs/my_ans.xls'

    if len(sys.argv) == 2:
        student_circ_path = sys.argv[1]
    else:
        print("Wrong argument")
        return


    option1 = ('java -jar logisim.jar ' + test_circ_path + ' -tty table '
              '-load ' + machine_code_path + ' > ' + right_ans_path)
    os.system(option1)

    option2 = ('java -jar logisim.jar ' + test_circ_path +
              ' -sub ' + standard_cpu_path + ' ' + student_circ_path + ' -tty table '
              '-load ' + machine_code_path + ' > ' + my_ans_path)
    os.system(option2)


if __name__ == '__main__':
    main()
