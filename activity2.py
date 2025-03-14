#Program to show linear time complexity(O(n)) by entering any n.
def myfun(n):
    iterations=0
    for i in range(1,n+1):
        iterations+=1
    print("When n is ",n,"No of iterations is",iterations)    

myfun(10)
myfun(40)
myfun(70)    