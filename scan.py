##!/usr/bin/env python

import string
import random
import re
from typing import List, Tuple
import ast

def obf_funcs(line:str,obf_iter:int,keys:List[Tuple[int, chr]]):
    """
    This function takes in a line and will obfuscate the functions and function calls.
    A function call will be obfuscated in the case that it exists in the keys list of tuples otherwise it is ignored

    Return: a line (modified if necessary), the current function obfuscation iteration, the keys list
    """
    
    for key in keys:
        if(f'{key[0]}(' in line):
            line = line.replace(key[0],key[1])
            return line,obf_iter,keys

    pattern:string = r"(?<=\bdef )\w+(?=\()"
    func_name = re.search(pattern,line)
    if(func_name and func_name.group()!='main'):
        fstart:int = func_name.start()
        fend:int = func_name.end()
        cur_char:chr = string.ascii_uppercase[obf_iter]
        new_s:string = f'{line[:fstart]}{cur_char}{line[fend:]}'
        keys.append((func_name.group(),cur_char))
        obf_iter+=1
        return new_s,obf_iter,keys
    
    return line,obf_iter,keys

def obf_vars(line):
    if not line.strip():  # Skip empty lines
        return set()
    if not line.endswith('\n'):  # Add a newline character if not present
        line += '\n'
    tree = ast.parse(line)
    variables = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            if isinstance(node.ctx, ast.Store):
                variables.add(node.id)
    return variables


def make_copy(filename:string):
    """
    This function will call each of the obfuscation methods in a sequence and print it to a new py file given a file name to scan
    """
    obf_funcs_iter: int = 0
    keys:List[Tuple[int, str]] = []
    with open(filename,'r') as file_1, open('new.py','w') as new:

        for line in file_1:
            print(line)
            print(obf_vars(line))


            newL_iter = obf_funcs(line,obf_funcs_iter,keys)
            line = newL_iter[0]
            obf_funcs_iter = newL_iter[1]

            new.write(line)
        

def main():
    make_copy("test.py")

    

if __name__ == "__main__":
    main()