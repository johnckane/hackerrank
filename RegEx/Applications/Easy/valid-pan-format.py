# Solves this application problem: https://www.hackerrank.com/challenges/valid-pan-format/
import sys, re
input_data =  sys.stdin.readlines()
for i in range(1,len(input_data)):
    re_pan = re.match(
        pattern = "[A-Z]{5}[0-9]{4}[A-Z]",
        string = input_data[i]
    )
    if re_pan != None:
        print("YES")
    else:
        print("NO")