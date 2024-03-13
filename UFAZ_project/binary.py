import pandas as pd

def twos(val_str, bytes):
    import sys
    val = int(val_str, 2)
    b = val.to_bytes(bytes, byteorder=sys.byteorder, signed=False)                                                          
    return int.from_bytes(b, byteorder=sys.byteorder, signed=True)

file = pd.read_csv('/home/emiliaveron/Desktop/code/codingformyself/python/image.csv')
print(file)

numbersDF = pd.DataFrame()
numbersDF = numbersDF.applymap(str)

list = []

columnN = 0
for j in file.columns.tolist()[::-1]:
    for i in file[j]:
        x = int(i[1:],2)
        if x < 32767:
            list.append(str(x))
        else:
            list.append(str(twos(i[1:], 2)))
    
    numbersDF.insert(columnN,j, list)
    list.clear()
    columnN+=1

count = 0
columnN = 0
with open("/home/emiliaveron/Desktop/code/codingformyself/python/catwalk.asm", 'w') as f:
    for column in numbersDF.columns:
        j = 16384+columnN
        for i in numbersDF[column]:
                if j < 24575:
                    if '-' in i:
                        f.write("@"+str(i[1:])+"\n")
                        f.write("D=-A\n")
                        f.write("@"+str(j)+"\n")
                        f.write("M=D\n")
                    else:
                        f.write("@"+str(i)+"\n")
                        f.write("D=A\n")
                        f.write("@"+str(j)+"\n")
                        f.write("M=D\n")  
                j+=32
        columnN+=1
    f.write("(END)\n@END\n0;JMP")