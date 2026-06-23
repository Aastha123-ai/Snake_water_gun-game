'''
1 for snake
-1 for water 
0 for gun 
'''
import random
computer=random.choice([-1,0,1])
youstr=input("Enter your choice : ")
youdict={"s":1,"w":-1,"g":0}
reversedict={1:"Snake",-1:"Water",0:"Gun"}
you=youdict[youstr]
print(f"you chose:{reversedict[you]}\nComputer chose:{reversedict[computer]}")

if(computer == you):
    print("Its a draw!")

else:
    '''if(computer==-1 and you==1): # (-1-(1)=-2) 
        print("Congrats!!You win")
    elif(computer==-1 and you==0): #-1
        print("Oops!!You lose")
    elif(computer==1 and you==0):  #1
        print("Congrats!!You win")
    elif(computer==1 and you==-1): #2
        print("Oops!!You lose")
    elif(computer==0 and you==-1):    #1
        print("Congrats!!You win")
    elif(computer==0 and you==1):    #-1
        print("Oops!!You lose") 
    else:
        print("Something went wrong!")       '''

    if((computer-you)==-2 or (computer-you)==1):
        print("Congrats!!You win")   
    else:
        print("Oops!You lose")         