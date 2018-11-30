import random
import math
import numpy as np

#This finds the accumulative sum of the list and returns the said list.
def accumu(lis):
    list=[]
    list.append(round(lis[0],7))
    for i in range(1,len(lis)):
        list.append(round(lis[i]+list[i-1],7))
    return list

#Finding position based on the accumulative sum of the list using a random number
def findPos(list):
    rn=random.random()
    c=0
    for val in list:
        if(rn < val):
            break
        c=c+1
    return c

#READING A FILE FOR A, B, PI, OPCHARS
f = open ( 'A.txt' , 'r')
a = [[float(num) for num in line.split(' ')] for line in f]
print ("A matrix is " + str(a))
print ("**************************************")
f.close()
f = open ( 'B.txt' , 'r')
b = [[float(num) for num in line.split(' ')] for line in f ]
print ("B matrix is " +str(b))
print ("**************************************")
f.close()
f = open ( 'Pi.txt' , 'r')
pi = [float(num) for num in f.readline().split()]
print ("Pi matrix is " +str(pi))
print ("**************************************")
f.close()
f = open ( 'opChars.txt' , 'r')
opChars=[letter.strip() for letter in f.readline().split()]
print ("Output characters are" +str(opChars))
print ("***************************************")
f.close()

#This finds the accumulative sum of the pi list and therefore finds the start state
piAcc=accumu(pi)
startState=findPos(piAcc)

k=int(input("How many output characters do you want?: "))
print("Output characters are: ")


"""
    This uses the a and b list's accumulative sum
    to find which state to go to and which output to
    print respectively.
"""
curState=startState
for i in range(k):
    bAcc=accumu(b[curState])
    op=findPos(bAcc)
    print(opChars[op]),
    aAcc=accumu(a[curState])
    nextState=findPos(aAcc)
    curState=nextState
