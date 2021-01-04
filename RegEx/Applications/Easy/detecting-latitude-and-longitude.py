#Solves this application problem: https://www.hackerrank.com/challenges/detecting-valid-latitude-and-longitude/problem
import sys, re
input_data =  sys.stdin.readlines()

lat="(\+|-)?((90(\.0+)?)|([1-8][0-9](\.\d{1,})?)|[1-9](\.\d{1,})?)"
lon="(\+|-)?((180(\.0+)?)|(1[0-7]\d(\.\d{1,})?)|([1-9]\d(\.\d{1,})?)|[1-9](\.\d{1,})?)"

for i in range(1,len(input_data)):
    regex = re.match(
        pattern = "^\({0}, {1}\)$".format(lat,lon),
        string = input_data[i]
    )
    if regex == None:
        print("Invalid")
    else:
        print("Valid")
    del regex
