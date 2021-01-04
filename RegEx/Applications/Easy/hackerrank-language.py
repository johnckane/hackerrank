# Solves this application problem: https://www.hackerrank.com/challenges/hackerrank-language/problem
import sys, re
input_data =  sys.stdin.readlines()

string="(C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)"
for i in range(1,len(input_data)):
    regex = re.match(
        pattern = "^[1-9][0-9]{3,4} "+string+"$",
        string = input_data[i]
    )
    if regex != None:
        print("VALID")
    else:
        print("INVALID")