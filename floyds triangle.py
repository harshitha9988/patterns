r=int(input("please enter the total nomber of rows"))
n=1

print("Floyd's Triangle")

for i in range(1,r+1):

    for j in range(1,i+1):

        print(n,end='')
        n=n+1
    print()