f = open("file.txt",'w')
while True:
    s = input()
    if s == '': break
    f.write(s+'\n')
f.close()
