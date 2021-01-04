# Solves this application problem: https://www.hackerrank.com/challenges/stack-exchange-scraper/
# Enter your code here. Read input from STDIN. Print output to STDOUTimport sys, re
import re,sys
input_data =  sys.stdin.readlines()
out=""
for i in range(1,len(input_data)):
    id_regex = re.search(
        pattern = "\"question-summary-(\d{1,})\">",
        string = input_data[i]
    )
    if id_regex != None:
        out+=str(id_regex.group(1))+";"

    text_regex = re.search(
        pattern = "class=\"question-hyperlink\">(.*)<\/a><\/h3>",
        string = input_data[i]
    )
    if text_regex != None:
        out+=str(text_regex.group(1))+";"
    
    time_regex = re.search(
        pattern = "class=\"relativetime\">(.*)<\/span>",
        string = input_data[i]
    )
    if time_regex != None:
        out+=str(time_regex.group(1))
        out+="\n"
print(out)

