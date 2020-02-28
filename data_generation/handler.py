# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 19:46:57 2020

@author: Tim-Laptop
"""

import csv


# global constants
SOURCE_CSV = "../data/recorded_cursor_data.csv"
DEST_CSV = "../data/cleaned_cursor_data.csv"
BUFFER_SIZE = 4096


class Handler:
    
    
    def __init__(self):
        self.current_line = 0
        self.current_batch_num = 1
        self.last_seek_pos = 0
        self.batch_count = find_batch_count()
        self.batch_locations = find_batch_locations()
        
    
        
    def get_batch(self, batch_num):
        read_block(self, self.batch_locations[batch_num])
    
    
    def get_next_batch(self):
        
        
    def read_block(self, seek_pos):
        ''' open the csv file, read in all the data entries for one movement,
        all the coords between two click events, and close the file when you
        reach the next batch ie movement between click events'''
        batch_data = []
        with open(SOURCE_CSV, 'r', BUFFER_SIZE) as f:
            f.seek(seek_pos)
            while self.get_batch_num(f) == self.current_batch_num:
                batch_data.append([int(i) if i.isdigit() else i for i in
                                   f.readline().rstrip('\n').split(',')])
                for entry in batch_data:
                    print(entry)
                self.current_batch_num += 1
                self.last_seek_pos = f.tell()
        return batch_data
                
    
    def write_block(self, clean_data):
        ''' append the cleaned data to a cleaned_data csv file, one batch at
        a time'''
        with open(DEST_CSV, 'a', BUFFER_SIZE) as f:
            writer = csv.writer(f)
            writer.writerows(clean_data)


    def find_batch_locations(self, file, offsets):
        ''' find the seek position at which each new batch starts in the csv
        file'''
        batch_nums = []
        last_batch = 0
        for line_pos in offsets:
            current_batch_num = (find_batch_num(self, file, line_pos)) 
            if current_batch_num > last_batch:
                batch_nums.append(current_batch_num, line_pos)
                last_batch = current_batch_num
        return batch_nums
        
                              
    def find_batch_num(self, file, seek_pos):
        ''' find the current data batch based on seek location in a file '''
        file.seek(seek_pos)
        this_row = csv.reader(file).__next__()
        file.seek(seek_pos)
        return this_row[0]


    def find_batch_count(self):
        ''' find the total number of batches in the source csv file '''
        with open(SOURCE_CSV, 'r') as file:
            return reversed(list(csv.reader(file)))[0][0]


    def find_line_offsets(self):
        with open(SOURCE_CSV, 'rb', BUFFER_SIZE) as file:
            line_offsets = []
            offset = 0
            for line in file:
                line_offsets.append(offset)
                offset += len(line)
        return line_offsets
    
c = Cleaner()
c.clean()

        