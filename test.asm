ori $0, $0, 10
ori $1, $0, 11
ori $2, $0, 22
ori $3, $0, 40
ori $4, $0, 2000
ori $5, $4, 12

nop
nop
nop

add $6, $5, $4
add $7, $6, $2
add $8, $7, $1
add $9, $8, $0
add $10, $0, $3

sw $0, 0($10)
sw $1, 4($10)
sw $2, 8($10)

nop
nop
nop


lw $11, 0($10)
lw $12, 0($10)
lw $13, 0($10)

sub $14, $10, $0
sub $15, $14, $1
sub $16, $15, $2

lui $17, 0xffff
lui $18, 0x4fff
lui $19, 0x1
lui $20, 0x223

ori $21, $21, 1
ori $22, $22, 1
loop:
sub $22, $22, $4
beq $21, $22, loop
