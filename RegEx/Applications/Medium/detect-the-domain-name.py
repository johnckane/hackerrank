# Solves this application problem: https://www.hackerrank.com/challenges/detect-the-domain-name
import sys, re
input_data =  sys.stdin.readlines()
dlist=[]
for line in input_data[1:]:
    regex = re.findall(
        pattern = "(?<=http:\/\/)(?:ww(?:w|2)\.)?((?:\w{1,}\.){1,}[A-Za-z0-9]{1,})",
        string = line 
    )
    for m in regex:
        dlist.append(m)
    del regex
print(";".join(domain for domain in sorted(set(dlist))))
