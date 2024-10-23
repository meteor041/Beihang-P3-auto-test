python autoGenerate.py
python autoRun.py test.asm machine_code.txt mips_memory.txt > mips_registers.txt
python compareMemory.py mips_memory.txt logisim_memory.txt > result.txt
python compareRegister.py mips_registers.txt logisim_registers.txt >> result.txt