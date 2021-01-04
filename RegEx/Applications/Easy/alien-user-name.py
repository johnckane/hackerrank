# Solves this application problem: https://www.hackerrank.com/challenges/alien-username/
import sys, re
import sys, re
input_data =  sys.stdin.readlines()
for i in range(1,len(input_data)):
    regex = re.match(pattern = "^(_|\.)[0-9]+[A-Za-z]*_?$", string=input_data[i])
    if regex != None:
        print("VALID")
    else:
        print("INVALID")
    del regex