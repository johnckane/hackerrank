# Solves this application problem: https://www.hackerrank.com/challenges/detect-the-domain-name
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys, re
input_data =  sys.stdin.readlines()
dlist=[]
for line in input_data[1:]:
    regex = re.findall(
        pattern = "(?:https?:\/\/)(?:ww(?:w|2)\.)?((?:[A-Za-z0-9_-]{1,}\.){1,}[A-Za-z0-9]{1,})",
        string = line 
    )
    for m in regex:
        dlist.append(m)
    del regex
print(";".join(domain for domain in sorted(set(dlist))))
