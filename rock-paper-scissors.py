import random
import re

# class rps:
a_count=0
p_count=0
arr={"r":"rock","p":"paper","s":"scissors"}
# def r_p_s()
def ai_choice(arr):
    ch=random.choice(list(arr.keys()))
    return ch


def checkwin(a,p):
    if a[0].lower()==p[0].lower():
        print("AI choice: "+a+" Player choice: "+p)
        print("Draw!")
        return 0
    if a[0].lower()=="r" and p[0].lower()=="p":
        print("AI choice: "+a+" Player choice: "+p)
    elif a[0].lower()=="p" and p[0].lower()=="s":
        print("AI choice: "+a+" Player choice: "+p)
    elif a[0].lower()=="s" and p[0].lower()=="r":
        print("AI choice: "+a+" Player choice: "+p)
    else:
        print("AI choice: "+a+" Player choice: "+p)
        print("AI wins")
        # a_count+=1
        return "ai"
    return "player"
        
def scoreboard(a,p):
    print("- - - - -")
    print("|AI count-",a,"|")
    print("-------------")
    print("|P count-",p,"|")
    print("- - - - -")

while True:
    move=input("Player enter your move(r/p/s): ")
    # if move.lower() not in arr:
    #     print("Invalid input")
    #     break
    s=checkwin(ai_choice(arr.values()),move)
    if s=="ai":
        a_count+=1
    elif s=="player":
        p_count+=1
    scoreboard(a_count,p_count)
    
