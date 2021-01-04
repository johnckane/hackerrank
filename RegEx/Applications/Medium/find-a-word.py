# Solves this application problem: https://www.hackerrank.com/challenges/find-a-word
# this had a special situation, when looking for a word attach, a sequence of " attach attach" would only
# match once, since, the space separating the two was counted only as the space after the first, but not as
# the space before the second. Using a positive lookahead gets around this issue.
import sys, re
#input_data =  sys.stdin.readlines()
input_data = open("C:\\Users\\jokane\\Desktop\\HackerRank\\RegEx\\Applications\\Medium\\find-a-word-input.txt", "r").readlines()
n = int(input_data[0])
t = int(input_data[n+1])
for word in input_data[(1+n+1):]:
    total = 0
    regex="(?=(?:^|[^A-z0-9_])("+word.replace("\n","")+")(?:$|[^A-z0-9_]))" 
    for sentence in input_data[1:(n+1)]:
        regex_match = re.findall(pattern=regex, string=sentence.replace("\n",""))
        total+=len(regex_match)
    print(total)