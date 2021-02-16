# Solves this application problem: https://www.hackerrank.com/challenges/detect-html-links
# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys, re
#input_data =  sys.stdin.read()
input_data = open("C:\\Users\\jokane\\Desktop\\HackerRank\\RegEx\\Applications\\Medium\\programming-language-detection-test3.txt", "r").read()
python_regex = re.findall(
        pattern = "((?:^|\n)[a-zA-z0-9]*\s=\s)|(def [^):]*\):)",
        string = input_data
        )
java_regex = re.findall(
        pattern = "(?:^|\n|\s)import [^;()]*;",
        string = input_data)
c_regex = re.findall(
        pattern = "int main()\b",
        string = input_data) 

if python_regex != [] and java_regex == [] and c_regex == []:
    print("Python")
elif python_regex == [] and java_regex != [] and c_regex == []:
    print("Java")
elif python_regex == [] and java_regex == [] and c_regex != []:
    print("C")
else:
    print("None")
