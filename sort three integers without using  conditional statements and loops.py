x=int(input('enter first number : '))
y=int(input('enter second number : '))
z=int(input('enter third number : '))

a1=min(x, y, z)
a3=max(x, y, z)
a2=(x + y + z)-a1 - a3
print("Numbers in sorted order: ", a1, a2, a3)