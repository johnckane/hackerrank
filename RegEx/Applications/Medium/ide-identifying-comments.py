# Solves this application problem: https://www.hackerrank.com/challenges/detect-the-domain-name
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys, re
# looking at read vs readlines...read in as one string or as each line on new page
#input_data =  sys.stdin.readlines()
#input_data = open("C:\\Users\\jokane\\Desktop\\HackerRank\\RegEx\\Applications\\Medium\\ide-identifying-comments-input1.txt", "r").readlines()
input_data = open("C:\\Users\\jokane\\Desktop\\HackerRank\\RegEx\\Applications\\Medium\\ide-identifying-comments-input1.txt", "r").read() 
regex = re.findall(
        pattern = "(\/\/.*(?=\n))|(\/\*.*\n{1,}.*\*\/)",
        string = input_data,
        )
for t in regex:
    for i in t:
        if i != '':
            print(i)
            
            
            