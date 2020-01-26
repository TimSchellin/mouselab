# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 15:21:20 2020

@author: Tim-Laptop
"""

# Imports
import csv
#import cleaner

# Globals
TEST_SOURCE_CSV = "../../sandbox/sample.csv"
CURRENT_LINE = 0
CURRENT_BATCH_NUM = 1
LAST_SEEK_POS = 28


def main():
    test_seek()


def test_seek():
    global CURRENT_LINE
    global CURRENT_BATCH_NUM
    global LAST_SEEK_POS
    batch_data = []
    #offsets = get_line_offsets()
    with open(TEST_SOURCE_CSV, 'r') as f:
        f.seek(LAST_SEEK_POS)
        while get_batch_num(f) == CURRENT_BATCH_NUM:
            batch_data.append([int(i) if i.isdigit() else i 
                               for i in f.readline().rstrip('\n').split(',')])
        for entry in batch_data:
            print(entry)
        CURRENT_BATCH_NUM += 1
        LAST_SEEK_POS = f.tell()
    with open(TEST_SOURCE_CSV, 'r') as f:
        f.seek(LAST_SEEK_POS)
          

def get_batch_num(file):
    start_pos = file.tell()
    batch_num = int(file.readline()[0])
    file.seek(start_pos)
    return batch_num
    
    
def get_line_offsets():
    with open(TEST_SOURCE_CSV, 'rb', 4096) as file:
        line_offsets = []
        offset = 0
        for line in file:
            line_offsets.append(offset)
            offset += len(line)
    return line_offsets
    
    
def test_file():
    with open(TEST_SOURCE_CSV, 'r') as f:
        for line in f.readlines():
            print(line)
              
            
if __name__ == "__main__":
    main()

    
