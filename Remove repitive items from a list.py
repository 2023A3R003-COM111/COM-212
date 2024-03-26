#for i in range(10):
#	list[i]=str(input())

list_=["vim", "nano", "Emacs", "nano", "vim", "Emacs", "Emacs", "nano", "Emacs", "Vim"]
i=0
j=0
poped=0


while True:
    while True:
        j=i+1
        if list_[i] == list_[j]:
            list_.pop(j)
    i+=1
    if i == len(list_):
        break



#for i in range(len(list_)):
#    for j in range(i,len(list_)-i):
#        if list_[i] == list_[j-poped]:
#            list_.pop(j-poped)
#            poped+=1


#for i in list_:
#    count+=1
#    for j in range(count,len(list_)-count+1):
#        if list_[j-poped] == i:
#            list_.pop(j-poped)
#            poped+=1

print(list_)


