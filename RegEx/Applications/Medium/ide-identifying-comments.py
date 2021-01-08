# Solves this application problem: https://www.hackerrank.com/challenges/detect-the-domain-name
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys, re
#input_data =  sys.stdin.readlines()
input_data = open("C:\\Users\\jokane\\Desktop\\HackerRank\\RegEx\\Applications\\Medium\\ide-identifying-comments-input1.txt", "r").readlines()
for line in input_data[1:]:
    regex = re.findall(
        pattern = "(\/\/.*$)|(\/\*\*.*\n.*\*\*\/)",
        string = line 
    )
    print(regex)
    del regex