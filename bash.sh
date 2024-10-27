python autoGenerate.py
python autoRun.py ../docs/test.asm ../docs/machine_code.txt ../docs/mips_memory.txt > ../docs/mips_registers.txt
python logisimRun.py ../your_cpu/cpu_wrong.circ
python compareMemory.py mips_memory.txt logisim_memory.txt > result.txt
python compareRegister.py mips_registers.txt logisim_registers.txt >> result.txt