# Solves this application problem: https://www.hackerrank.com/challenges/utopian-identification-number/
import sys, re
input_data =  sys.stdin.readlines()
for i in range(1,len(input_data)):
    regex = re.match(
        pattern = "[a-z]{0,3}[0-9]{2,8}[A-Z]{3,}",
        string = input_data[i]
    )
    if regex != None:
        print("VALID")
    else:
        print("INVALID")
    del regex
