import os

path ='G:\\Nier Automata'
k = 0

def o(path):
    global k
    for i in os.listdir(path):
        if '.exe' in i:
            print(path+' '+i)
            k += 1
        if os.path.isdir(path+'\\'+i):
            o(path+'\\'+i)
o(path)
print(k)

