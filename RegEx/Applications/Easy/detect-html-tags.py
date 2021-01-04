# Solves this application problem: https://www.hackerrank.com/challenges/detect-html-tags/
import sys, re
input_data =  sys.stdin.readlines()
tags = []
for i in input_data:
    regex = re.findall(r"<\s?([a-z0-9]+)\s?([^>]?)*>",i)
    if regex != []:
        for j in regex:
            tags.append(j[0])
    del regex

print(";".join(str(x) for x in sorted(set(tags))))