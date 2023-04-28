##!/usr/bin/env python

import string
import random
import re

def obf_funcs(line:str,obf_iter:int,keys):

    for key in keys:
        if(f'{key[0]}(' in line):
            line = line.replace(key[0],key[1])
            #print(line)
            return line,obf_iter,keys

    pattern = r"(?<=\bdef )\w+(?=\()"
    func_name = re.search(pattern,line)
    if(func_name and func_name.group()!='main'):
        print(func_name.group())
        fstart = func_name.start()
        fend = func_name.end()
        cur_char = string.ascii_uppercase[obf_iter]
        new_s = f'{line[:fstart]}{cur_char}{line[fend:]}'
        keys.append((func_name.group(),cur_char))
        obf_iter+=1
        return new_s,obf_iter,keys
    
    return line,obf_iter,keys


def make_copy(filename:string):
    obf_funcs_iter: int = 0
    keys = []
    with open(filename,'r') as file_1, open('new.py','w') as new:
        for line in file_1:
            newL_iter = obf_funcs(line,obf_funcs_iter,keys)
            line = newL_iter[0]
            obf_funcs_iter = newL_iter[1]

            new.write(line)
        

def main():
    make_copy("test.py")

    

if __name__ == "__main__":
    main()