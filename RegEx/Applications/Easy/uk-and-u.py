# Solves this application problem: https://www.hackerrank.com/challenges/uk-and-us/
import sys, re
input_data =  sys.stdin.readlines()
num_lines = int(input_data[0])
num_testcases = int(input_data[num_lines+1])
for i in range(num_testcases):
    testcase = input_data[num_lines + 2]
    total = 0
    for j in range(1,num_lines):
        regex = re.search(
            pattern = "("+testcase[:-2]+"(ze|se))",
            string = input_data[j]
        )
        if regex != None:
            print(regex)
            total+=1
    print(total)

