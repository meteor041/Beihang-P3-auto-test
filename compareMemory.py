import sys


def main():
    if len(sys.argv) == 1:
        mips_path = "mips.txt"
        logisim_path = "logisim.txt"
    elif len(sys.argv) == 3:
        mips_path = str(sys.argv[1])
        logisim_path = str(sys.argv[2])
    else:
        print("Wrong argument!!!")
        return

    mips_file = open(mips_path, "r")
    logisim_file = open(logisim_path, "r")

    mips_mem = []
    lines = mips_file.readlines()
    for line in lines:
        line = remove_suffix(line)
        mips_mem.append(int(line, 16))

    logisim_mem = [0] * len(mips_mem)
    lines2 = logisim_file.readlines()
    line = lines2[1]
    line = remove_suffix(line)
    index = 0
    for s in line.split(" "):
        if "*" in s:
            # cnt为10进制,value为16进制
            cnt, value = s.split("*")
            cnt = int(cnt)
            value = int(value, 16)
            for _ in range(cnt):
                logisim_mem[index] = value
                index += 1
        else:
            value = int(s, 16)
            logisim_mem[index] = value
            index += 1

    flag = True
    wrong_loc = []
    for i, (x, y) in enumerate(zip(logisim_mem, mips_mem)):
        if x != y:
            flag = False
            wrong_loc.append(i + 1)

    if flag:
        print("Two Memories are the same!!!")
    else:
        print("Two Memories are different!!!")
        print("Mistakes:")
        for x in wrong_loc:
            print('line: ', x, ', ', 'mips_mem: ', mips_mem[x-1],
                  'logisim_mem: ', logisim_mem[x-1])


def remove_suffix(s):
    if '\n' in s:
        return s[:-(len('\n'))]
    else:
        return s


if __name__ == "__main__":
    main()
