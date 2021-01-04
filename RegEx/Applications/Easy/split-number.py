#Solves this application problem: https://www.hackerrank.com/challenges/detecting-valid-latitude-and-longitude/problem
import sys, re
input_data =  sys.stdin.readlines()
for i in range(1,len(input_data)):
    regex = re.search(
        pattern = "^(\d+)(\s|-)(\d+)(\s|-)(\d+)",
        string = input_data[i]
    )
    if regex != None:
        output="CountryCode={0},LocalAreaCode={1},Number={2}"\
        .format(regex.group(1),
                regex.group(3),
                regex.group(5))
        print(output)
    del regex

