#!python3
# Read the contents of a file that has a json encoded list of numbers.
# Find the largest number in each list
# task01a: 63545
# task01b: 63876
# task01c: 63891

import json

print("Pick a Task file")
print("1 for 'task01a.txt'")
print("2 for 'task01b.txt'")
print("3 for 'task01c.txt'")

TXT = '0'


while TXT != '1' or TXT != '2' or TXT != '3':
    TXT = input(': ')
    if TXT == '1' or TXT == '2' or TXT == '3':
        break
    else:
        print('Invalid')

#Task A
if TXT == "1":
    #Open JSON file
    with open('task01a.txt', 'r') as openfile:
    
        #Read json file
        Num_List = json.load(openfile)
    
    Num_List.sort(reverse=True)

    #print(Num_List)

    MAX_NUM = (Num_List[0])

    print("The biggest Number in task01a.txt is", MAX_NUM)

#Task B
if TXT == "2":
    #Open JSON file
    with open('task01b.txt', 'r') as openfile:
    
        #Read json file
        Num_List = json.load(openfile)
    
    Num_List.sort(reverse=True)

    #print(Num_List)

    MAX_NUM = (Num_List[0])

    print("The biggest Number in task01b.txt is", MAX_NUM)

#Task C
if TXT == "3":
    #Open JSON file
    with open('task01c.txt', 'r') as openfile:
    
        #Read json file
        Num_List = json.load(openfile)
    
    Num_List.sort(reverse=True)

    #print(Num_List)

    MAX_NUM = (Num_List[0])

    print("The biggest Number in task01c.txt is", MAX_NUM)

#DONE