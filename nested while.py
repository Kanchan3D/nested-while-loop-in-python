#explanation for while nested loop
#while expression:
#    while expression:
#        statement(S)
#statement(S)
n=int(input())
while(n<=10):
    print(n,"outer loop is executed")
    j=1
    while(j<=5):
        print(j,"inner loop is executed until to comletion")
        j+=1
    n+=1
