#Hello day 13
'''
def fibonacci(x):
    a=0
    b=1
    print(a,b,end=" ")
    for i in range(x):
        c=a+b
        if(c>50):
            print("\nStopped")
            break
        print(c,end=" ")
        a=b
        b=c
fibonacci(12)

a=list(map(int,input().split()))
def duplicate_val(a):
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    print(b)
duplicate_val(a)



def count_words(para):
    l1=para.split()
    s=len(l1)
    print(s)

count_words(input())
    
'''
count=0
so="qwert qwert qaswdefrtgh azsxdfg asdfg asdfg asdfg qawsert qawsedfgh aqsweh asdf"
def word_str(so,count):
    for j in so:
        count+=1
    print(count)
word_str(so,count)
