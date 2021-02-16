# Solves this application problem: https://www.hackerrank.com/challenges/detect-html-links
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys, re
#input_data =  sys.stdin.readlines()
input_data = open("C:\\Users\\jokane\\Desktop\\HackerRank\\RegEx\\Applications\\Medium\\detect-html-links-test3.txt", "r").readlines()
for line in input_data[1:]:
    link_regex = re.findall(
        pattern = "(?:<a href=\")([^\"]*)(?:\")",
        string = line 
    )
    name_regex = re.findall(
        pattern = "(?:<a href=\"[^\"]*\"[^>]*>)(?:<[^>]*>){0,}([A-Za-z0-9\s.,\/]*)(?:<)",
        string = line
    )
    if link_regex != []:
        for i in range(len(link_regex)):
            if name_regex != []:
                print(link_regex[i].strip()+","+name_regex[i].strip())
            else:
                print(link_regex[i]+",")
    del link_regex, name_regex