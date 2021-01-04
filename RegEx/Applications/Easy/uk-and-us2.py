# Solves this application problem: https://www.hackerrank.com/challenges/uk-and-us2/
import sys, re
input_data =  sys.stdin.readlines()
num_lines = int(input_data[0])
num_testcases = int(input_data[num_lines+1])
for i in range(num_testcases):
    testcase = input_data[num_lines + 2 + i].strip()
    us_version = str.replace(testcase,"our","or")
    total = 0
    for j in range(1,num_lines+1):
        regex = re.findall(
            pattern = "("+testcase+"|"+us_version+")\\b",
            string = input_data[j]
        )
        if regex != []:
            total+=len(regex)
    print(total)
2