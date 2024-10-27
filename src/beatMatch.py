import csv
def main():
    right_ans_path = '../docs/right_ans.xls'
    my_ans_path = '../docs/my_ans.xls'
    info_path = '../result/beat_match_result.txt'
    with open(right_ans_path, 'r') as f1, open(my_ans_path, 'r') as f2,\
            open(info_path, 'w') as w:
        right_data = csv.reader(f1)
        my_data = csv.reader(f2)
        flag = True
        for i, (right_line, my_line) in enumerate(zip(right_data, my_data)):
            if right_line != my_line:
                flag = False
                w.write("line " + str(i) + '\n')
        if flag:
            print("The results are correct!!!")
            w.write("The results are correct!!!")


if __name__ == '__main__':
    main()