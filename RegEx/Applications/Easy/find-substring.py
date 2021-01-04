# Solves this application problem: https://www.hackerrank.com/challenges/find-substring
import sys, re
input_data =  sys.stdin.readlines()
tags = []
n = int(input_data[0])
q = int(input_data[n+1])
for w in input_data[(1+n+1):]:
    total = 0
    new_regex_string = "[A-z0-9_]+"+w.replace("\n","")+"[A-z0-9_]+"
    for s in input_data[1:(n+1)]:
        regex = re.findall(new_regex_string,s)
        total += len(regex)
        del regex
    print(total)