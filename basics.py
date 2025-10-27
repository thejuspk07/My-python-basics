#FOR LOOP
#ASENDING ORDER
# for i in range(11,1,-1):#start,end,step
#     print(i)
# #DESCENDING ORDER
# for i in range(11,1,-1):#start,end,step
#     print(i)

#WHILE LOOP
#while(condition):
    #code block
# x=10
# a=1
# while(a<=x):
#     print(a,end=" ")
#     a+=1


# x=1
# a=10
# while(a>=x):
#     print(a,end=" ")
#     a-=1


#NESTED LOOP                                                                    full command = ctrl + /
# for i in range(5):
#     for j in range(5):
#        print('*',end=' ')           #* * * * *   i=0 j=0 1 2 3 4
#                                     #* * * * *   i=1 j=0 1 2 3 4
#                                     #* * * * *   i=2 j=0 1 2 3 4
#                                     #* * * * *   i=3 j=0 1 2 3 4
#                                     #* * * * *   i=4 j=0 1 2 3 4
#     print()

# for i in range(5):
#     print(" "*(4-i),end='')    #        *
#     for j in range(i+1):
#        print('*',end=' ')           #* * * * *   i=0 j=0 1 2 3 4
#                                     #* * * * *   i=1 j=0 1 2 3 4
#                                     #* * * * *   i=2 j=0 1 2 3 4
#                                     #* * * * *   i=3 j=0 1 2 3 4
#                                     #* * * * *   i=4 j=0 1 2 3 4
#     print()


x='vilas'
print(x[::-1])
