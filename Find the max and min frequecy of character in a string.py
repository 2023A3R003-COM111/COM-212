string="A Computer is like air conditionar, it becomes useless when you open windows in it!" # Quote by Linus Torvard, Only Linux users will understand!.
alph="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Assign 0 to every index of count
count=[]
for i in range(len(alph)):
    count.append(0)

# Assign the frequecny of each character to the 
# "count" list with corospond to alph list.
for i in string:
    # Dont compare blank-space
    if i != ' ':
        for j in range(len(alph)):
            if i.upper() == alph[j]:
                count[j]=count[j]+1
                break

# Initialize a default value
maxval=maxindex=minindex=0
minval=len(string)

# Loop over the "count" list to find max and min value and
# then there indexes which will corospond to "alph" list.
for i in range(len(count)):
    # Dont check for values which never appeared in the list.
    if count[i] != 0:
        if maxval < count[i]:
            maxval = count[i]
            maxindex=i
        elif minval > count[i]:
            minval = count[i]
            minindex=i

print("Max frequency character:",str(alph[maxindex])+"\nMin frequency character:",str(alph[minindex]))
