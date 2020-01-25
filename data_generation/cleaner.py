# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 19:46:57 2020

@author: Tim-Laptop

This file is for cleaning the raw data generated by the trackmouse.py recording
"""

import csv

SOURCE_CSV = "../data/recorded_cursor_data.csv"
DEST_CSV = "../data/cleaned_cursor_data.csv"

source_data = []
clean_data = []

class Cleaner():
    def __init__(self):
        self.source_data = []
        self.clean_data = []
        self.line_offset = self.get_line_offsets()
        
    def get_line_offsets(self):
        with open(SOURCE_CSV, 'r', 4096) as file:
            line_offsets =[]
            offset = 0
            for line in file:
                line_offsets.append(offset)
                offset += len(line)
        return line_offsets
    
    def read_next_block():
        pass
    
    def write_next_block():
        pass
    
        