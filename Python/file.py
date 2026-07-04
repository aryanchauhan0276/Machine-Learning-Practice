'''with open ("sample.txt","r") as fin:
    content=fin.read()
    print(content)
fin.close()
l=["\nHello How are you","\nI am good","\nWelcome to Course"]
with open("output.txt","w") as fout:
    fout.writelines(content)
fout.close()

with open("sample.txt","a") as fin:
    fin.write("Hello I am Udemy")
fin.close()
with open ("document.txt","r") as fin:
    content=fin.read()
    x=content.split()
    print(x)
    print(len(x))
fin.close()
with open ("document.txt","r+") as fin:
    b=[]
    content=fin.read()
    x=content.split()
    for word in x:
        if word=="Hello":
           b.append("Bye")
        else:
            b.append(word)
    c=" ".join(b)
    fin.write(c)
with open ("document.txt","r") as file:
    x=file.readlines()
    for line in range(len(x)-1,-1,-1):
        print(x[line])'''
with open("document.txt","r") as file:
    '''x=file.read()
    print(len(x))

    c=x.split()
    print(len(c))
    '''
    w=file.readlines()
    print(len(w))