# File I/O
'''
f=open("sample.txt","wt")
#w: write(overwrite)
#r.read (throws error if file does not exist)
#a: append
#x: write(throws error if file already exists)
#t: text file
#b: Binary
f.write('Hello')
f.close()
'''
with open("sample.txt",'at') as f:
    f.write("Hello\n")
    names=['Ashish','Sonali','Mahesh','Aparna']
    #f.writelines(names)
    for name in names:
        f.write(name +'\n')
#automatic close
