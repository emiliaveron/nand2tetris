@SCREEN
D=A
@32
D=A+D
@R
M=D
@1
D=-A
@R
A=M
M=D

(LOOP)
@1
D=-A
@R
M=M+1
A=M
M=D

@24575
D=D-A
@LOOP
D;JNE



(END)
@END
0;JMP
