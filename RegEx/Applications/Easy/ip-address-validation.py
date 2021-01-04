# Solves this application problem: https://www.hackerrank.com/challenges/ip-address-validation/
import sys, re
input_data =  sys.stdin.readlines()
for i in range(1,len(input_data)):
    re_ip4 = re.match(
        pattern = "^(([0-9]|\d{2}|(1\d{2}|(2[0-4][0-9])|(25[0-5])))\.){3}(([0-9]|\d{2}|(1\d{2}|(2[0-4][0-9])|(25[0-5]))))$",
        string = input_data[i]
    )
    re_ip6 = re.match(
        pattern = "^([a-f0-9]{1,4}:){7}([a-fz0-9]{1,4})$",
        string = input_data[i]
    )

    if re_ip4 == None and re_ip6 == None:
        print("Neither")
    elif re_ip4 != None:
        print ("IPv4")
    elif re_ip6 != None:
        print("IPv6")
    del re_ip4, re_ip6
