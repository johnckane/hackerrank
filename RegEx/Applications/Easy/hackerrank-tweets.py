# Solves this application problem: https://www.hackerrank.com/challenges/hackerrank-tweets/
import sys, re
input_data =  sys.stdin.readlines()
total = 0
for i in range(1,len(input_data)):
    regex = re.search(
        pattern = "hackerrank",
        string = input_data[i],
        flags = re.IGNORECASE)
    if regex != None:
        total+=1
print(total)
