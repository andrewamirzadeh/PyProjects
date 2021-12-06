#Author Name: Bijan Amirzadehasl
#Date: 11/2/2021
#Program Name: Amirzadehasl_Recursive_lines.py
#Purpose: Recursive function that can find the biggest number in a list and return the index
import random

def main():
    #Populate a list with random numbers between 1 and 1000
    randomList = []
    for i in range(0, 10):
        n = random.randint(1, 1000)
        randomList.append(n)

    #prints out the random List
    print(randomList)

    #prints out the results with method calls
    #similar results could use randomList.index(Max(randomList)
    print("Biggest number is:", Max(randomList))
    print("Biggest number index is:", Max_Index(randomList))

#recursive method to find the maximum of the random list
def Max(randomList):
    if len(randomList) <= 1:
        return randomList[0]

    else:

        return Max(randomList[1:]) if Max(randomList[1:]) > randomList[0] else randomList[0]


def Max_Index(randomList):
    if len(randomList) <= 1:
        return randomList.index(randomList[0])

    else:

        return randomList.index(Max(randomList[1:])) if randomList.index(Max(randomList[1:])) > randomList.index(randomList[0]) else randomList.index(randomList[0])

main()