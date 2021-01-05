# Solves this application problem: https://www.hackerrank.com/challenges/detect-the-email-addresses
import sys, re
#input_data =  sys.stdin.readlines()
input_data = open("C:\\Users\\jokane\\Desktop\\HackerRank\\RegEx\\Applications\\Medium\\detect-the-email-addresses-input2.txt", "r").readlines()
elist=[]
for line in input_data[1:]:
    regex = re.findall(
        pattern = "(\w{1,}(?:\.\w{1,})?@\w{1,}(?:\.\w{1,}){1,})",
        string = line 
    )
    for m in regex:
        elist.append(m)
    del regex
print(";".join(email for email in sorted(set(elist))))