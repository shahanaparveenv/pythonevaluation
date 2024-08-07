def countWord(word):
    total = 0
    x= c.split()
    print(word)
    for i in x:
        if i == word:
            total += 1
    print(total)


f = open(r"C:\Users\ASUS\Desktop\evaluation.txt", 'r')
c = f.read()
print(c)
x=input("enter the word to be counted ")
countWord(x)