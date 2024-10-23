import random


def rand_register():
    return '$' + str(random.randint(0, 25))


def rand_signed_immediate_16():
    return str(random.randint(-2 ** 15, 2 ** 15 - 1))


def rand_unsigned_immediate_16():
    return str(random.randint(0, 2 ** 16 - 1))


def main():
    number = 500
    op_set = ['add', 'sub', 'ori', 'lw', 'sw', 'beq', 'lui', 'nop', 'mark']
    mark_cnt = 0
    ready_to_mark = []
    with open("test.asm", "w") as f:
        f.write('.data\narr:.space 2000\n.text\n')
        f.write('loopx:\n'.replace('x', str(mark_cnt)))
        for _ in range(number):
            op = op_set[random.randint(0, len(op_set)-1)]
            if op == 'add':
                f.write(op + ' ' + rand_register() + ',' + rand_register() + ',' + rand_register() + '\n')
            elif op == 'sub':
                f.write(op + ' ' + rand_register() + ',' + rand_register() + ',' + rand_register() + '\n')
            elif op == 'ori':
                f.write(op + ' ' + rand_register() + ',' + rand_register() + ',' + rand_unsigned_immediate_16() + '\n')
            elif op == 'lw':
                f.write(op + ' ' + rand_register() + ',' + rand_signed_immediate_16() + '(' + rand_register() + ')\n')
            elif op == 'sw':
                f.write(op + ' ' + rand_register() + ',' + rand_signed_immediate_16() + '(' + rand_register() + ')\n')
            elif op == 'beq':
                if (random.randint(0,1) % 2 == 0):
                    f.write(op + ' ' + rand_register() + ',' + rand_register() + ',' +
                        'loopx\n'.replace('x', str(random.randint(0,mark_cnt))) + '\n')
                else:
                    mark_cnt += 1
                    f.write(op + ' ' + rand_register() + ',' + rand_register() + ',' +
                            'loopx\n'.replace('x', str(mark_cnt)) + '\n')
                    ready_to_mark.append(mark_cnt)
            elif op == 'lui':
                f.write(op + ' ' + rand_register() + ',' + rand_unsigned_immediate_16() + '\n')
            elif op == 'nop':
                f.write(op + '\n')
            elif op == 'mark':
                if len(ready_to_mark) == 0:
                    mark_cnt += 1
                    f.write('loopx:\n'.replace('x', str(mark_cnt)))
                else:
                    f.write('loopx:\n'.replace('x', str(ready_to_mark.pop())))
        while len(ready_to_mark) != 0:
            f.write('loopx:\n'.replace('x', str(ready_to_mark.pop())))

if __name__ == '__main__':
    main()
