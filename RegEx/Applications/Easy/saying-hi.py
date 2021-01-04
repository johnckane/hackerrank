# Solves this application problem: https://www.hackerrank.com/challenges/saying-hi/
import sys, re
input_data =  sys.stdin.readlines()
for i in range(1,len(input_data)):
    regex = re.match(
        pattern = "^[Hh][Ii]\s[^Dd]",
        string = input_data[i]
    )
    if regex != None:
        print(input_data[i], end = '')
    del regex