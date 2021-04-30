
# control flow
x=range(10)
print(x)
for y in x:
    print(y)

a=range(5,20)
for c in a:
    print(c)

w=range(20)
for y in w:
    if y%3==0:
        print(y)
c=range(10)
for a in c:
    if a%3 !=0:
        print(a)

# else
n=range(15)
for m in n:
    if m%2==0:
        print(" {} is divisible by 2".format(m))
    else:
        print("{} is not divisible by 2".format(m))

# elif statement
        b=range(30)
        for v in b:
            if v%5==0:
                print("{} is divisible by 5".format(v))
            elif v%7==0:
                print(" {} is divisible by 7".format(v))
            else:
                print("{} is not divisible by both 5 and 7".format(v))
# while loop
b=100
while b>=50:
    print(b)
    b-=10

c=1
while c<=10:
    print("I love Python")
    c+=1
# break
x=1
while x<50:
    print(x)
    if x%20==0:
        break
    x+=1
# continue
x=0
while x<50:
    x+=1
    if x%2!=0:
        continue
    print(x)

