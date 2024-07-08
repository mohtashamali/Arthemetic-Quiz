# This is a basic game which ask you randomly add,multip,div,diff question under the range 1 to 100
import random
import time
operator="+","-","*","/"
no1=1
no2=10 #you can change a range from double digit q.n to single digit ?quest?
list=[]
opr=["+","-","*","/"]
for i in range(no1,no2):
    list.append(i)

print("--------------------------")
input("To start press Enter  ")
i=1
starttimer=time.time()
while i<=10 :
        a=random.choice(list)
        b=random.choice(list)
        c=random.choice(opr)
        print("problem no ",i+1,">>>>",a,c,b,": ",end="")
        # print(a,c,b,": ",end="")
        ans=input()
        if(c=="+"):
                if(a+b==int(ans)):
                    pass     # print("right")
                elif(int(ans)!=a+b):
                    while(int(ans)!=a+b):
                        print("problem no ",i+1,">>>> Wrong, Try again",a,c,b,": ",end="")
                        ans=int(input())
        if(c=="-"):
                if(int(ans)==a-b):
                    pass # print("-- right")
                elif(int(ans)!=a-b):
                    while(int(ans)!=a-b):
                        print("problem no ",i+1,">>>>  Wrong,Try again",a,c,b,": ",end="")
                        ans=int(input())
            # break
        if(c=="*"):
                if(int(ans)==a*b):
                   pass # print("-- right")
                elif(int(ans)!=a*b):
                    while(int(ans)!=a*b):
                        print("problem no ",i+1,">>>> Wrong,Try again",a,c,b,": ",end="")
                        ans=int(input())
       
        if(c=="/"):
                ans=ans[:3]
                if(ans==round(a/b),2):
                   pass # print("-- right")
                elif(ans!=a/b):
                    while(ans!=a/b):
                        print("carefull enter the number after points .00 as its a float value")
                        print("problem no ",i+1,">>>> Wrong,Try again",a,c,b,": ",end="")
                        ans=round(float(input()),2)
                    
        i+=1
endtimer=time.time()
ttime=endtimer-starttimer
print("----------------------------------------")
print("Well done solved in",ttime[:4],"secound !!")
