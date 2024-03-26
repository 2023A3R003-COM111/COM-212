num=int(input())
fac=num

print(num,end="")
for i in range(1,num):
    fac*=i
    #print(str(num)+" "+str(i))
    print(" X "+str(num-i),end="")

print(" = "+str(fac))
