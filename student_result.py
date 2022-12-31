maths=int(input("Enter maths Mark:"))
gujrati=int(input("Enter gujrati Mark:"))
english=int(input("Enter english Mark:"))



if maths>=40 and gujrati>=40 and english>=40: 

    print("maths:",maths)
    print("gujrati:",gujrati)
    print("english:",english)

    total=maths+gujrati+english
    print("Total:",total)

    PR=total/3
    print("PR:",PR)

    
    if PR>=70:
        print("A grade")
    elif PR>=60:
        print("b grade")
    elif PR>=50:
        print("c grade")
    elif PR>=40:
        print("d grade")
        
else:
    print("Result:Fail")