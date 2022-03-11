#method-1

num = int(input("Enter a number"))

for i in range(0,num):
    for j in range(0,i+1):
        print("* ",end = '')
    print()
    
#method-2


for j in range(0,num+1):
    print("* "*j)

#output

* 
* * 
* * * 
* * * * 
* * * * * 
