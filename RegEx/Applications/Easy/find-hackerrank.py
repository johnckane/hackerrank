# Solves this application problem: https://www.hackerrank.com/challenges//find-hackerrank
import sys, re
input_data =  sys.stdin.readlines()
for i in range(1,len(input_data)):
    starts = re.search(
        pattern = "^hackerrank",
        string = input_data[i]
    )
    ends = re.search(
        pattern = "hackerrank$",
        string = input_data[i]
    )
    if starts == None and ends == None:
        print(str(-1))
    elif starts == None and ends != None:
        print(str(2))
    elif starts != None and ends == None:
        print(str(1))
    elif starts != None and ends != None:
        print(str(0))
    del starts, ends
