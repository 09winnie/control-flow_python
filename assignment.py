a=range(20)
for c in a:
    if c%2==0:
        print(c)
b=range(30,50)
for d in b:
    if d%2!=0:
        print(d)
# adding items to an empty list
x=[]
z=range(100,200)
for i in z:
    if i%7==0:
        x.append(i)
print(x)
# getting even numbers
a=range(0,20)
for b in a:
    if b%2==0:
        print("Fizz")
    elif b%3==0:
        print("Buzz")
    else:
        print("FizzBuzz")
a=0
while a<50:
    a+=1
    if a%2!=0:
        continue
    print(a)