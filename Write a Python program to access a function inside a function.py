def function1(): 
    print ("Hello from outer function")
    def function2(): 
        print ("Hello from inner function")
    function2()

function1()