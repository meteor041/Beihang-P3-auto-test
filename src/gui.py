# coding=gb2312
import os
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Auto Test Program for P3, made by Liu Xinyu")

label = tk.Label(root, text='Welcome to Auto Test Program!')
label.pack(pady=10)

def exit_app():
    root.quit()

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# add Exit command
file_menu.add_command(label="Exit", command=exit_app)

# run auto test program
def run():
    file_path = path_entry.get()
    print("file_path: " + file_path)
    os.system("python autoGenerate.py")
    print("代码自动生成程序运行完毕")
    os.system("python autoRun.py > ../docs/mips_registers.txt")
    print("标准运行结果生成程序运行完毕")
    os.system("python logisimRun.py " + file_path)
    print("测试文件运行结果生成程序运行完毕")
    os.system("python beatMatch.py")
    print("对拍程序运行完毕")


bm_frame = tk.Frame(root)
bm_frame.pack(pady=10)

note_label = tk.Label(bm_frame, text="Beatmatch with standard cpu :\n"
                                     +"input the circle path below and press run button")
note_label.pack(pady=10)

path_entry = tk.Entry(bm_frame)
path_entry.pack(pady=10)

# create a button "run"
run_button = tk.Button(bm_frame, text="run", command=run)

run_button.pack(pady=10)

bm_frame2 = tk.Frame(root)
bm_frame2.pack(pady=10)

def get_machine_code():
    mips_docs_path = path_entry_mips.get()
    machine_code_path = "../docs/machine_code.txt"
    mips_memory_path = "../docs/mips_memory.txt"
    mips_registers_path = "../docs/mips_registers.txt"
    os.system("python autoRun.py " + mips_docs_path + " " + machine_code_path + " " +
              mips_memory_path + " > " + mips_registers_path)
    messagebox.showinfo("", "The machine code has been generated")

def run2():
    logisim_memory_path = path_entry_lm.get()
    logisim_registers_path = path_entry_lr.get()
    mips_memory_path = "../docs/mips_memory.txt"
    mips_registers_path = "../docs/mips_registers.txt"

    result_path = "../result/memory_and_registers_result.txt"


    os.system("python compareMemory.py " + mips_memory_path +
              " " + logisim_memory_path + " > " + result_path)
    os.system("python compareRegister.py " + mips_registers_path +
              " " + logisim_registers_path + " >> " + result_path)

note_label2 = tk.Label(bm_frame2, text='Beatmatch with your mars result : \n' +
                       "input the circle path below and press run button",)
note_label2.pack(pady=10)

note_label_mips = tk.Label(bm_frame2, text='mips docs :')
note_label_mips.pack(pady=10)
path_entry_mips = tk.Entry(bm_frame2)
path_entry_mips.pack(pady=5)

# create a button "generate machine code"
run_button2 = tk.Button(bm_frame2, text="generate machine code", command=get_machine_code)
run_button2.pack(pady=10)

note_label3 = tk.Label(bm_frame2, text='input your logisim memory result :')
note_label3.pack(pady=10)
path_entry_lm = tk.Entry(bm_frame2)
path_entry_lm.pack(pady=5)

note_label4 = tk.Label(bm_frame2, text='input your logisim registers result')
note_label4.pack(pady=10)
path_entry_lr = tk.Entry(bm_frame2)
path_entry_lr.pack(pady=10)

# note_label5 = tk.Label(bm_frame2, text='input your cpu circuit')
# note_label5.pack(pady=10)
# path_entry_cr = tk.Entry(bm_frame2)
# path_entry_cr.pack(pady=10)





# create a button "compare registers and memory"
run_button3 = tk.Button(bm_frame2, text="compare registers and memory", command=run2)
run_button3.pack(pady=10)

# start loop
root.mainloop()