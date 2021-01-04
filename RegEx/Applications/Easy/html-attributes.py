# Solves this application problem: https://www.hackerrank.com/challenges/html-attributes/
import re,sys
input_data =  sys.stdin.readlines()
tag_dict={}
for i in range(1,len(input_data)):
    tag_regex = re.findall(
        pattern = '(?:<(\w+))|([A-z]+)(?==[\'\"])',
        string = input_data[i]
    )
    if(tag_regex != None):
        tag=None
        for t in tag_regex:
            if t[0] != '': #this is a new tag
                tag=t[0]
                if tag in tag_dict.keys():
                    pass
                else:
                    tag_dict[tag] = []
            if t[1] != '': #this is an attribute to go with the prior tag
                tag_dict[tag].append(t[1])
sorted_tag_dict = dict(sorted(tag_dict.items()))        
for entry in (sorted_tag_dict):
    print(entry+":"+",".join([str(elem) for elem in sorted(set(sorted_tag_dict[entry]))]))