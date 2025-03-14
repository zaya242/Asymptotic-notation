#Program to show time complexity(O(n^2)) by entering any n.
def myfun(n):
    iterations=0
    for i in range(0,n):
        for j in range(0,n):
            iterations+=1
            print(" * ",end="")
        print("")
    print("No of iteration for ",n," is ",iterations)


myfun(10) 

myfun(3)

myfun(4)
