# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 22:01:49 2020

@author: Tim-Laptop
"""

from datetime import datetime
import time
import win32api
import win32con
import os
import csv

csv_header = "sequence number, x, y, time"
csv_path = "../data/mouse_data.csv"

event_num = 0
save_interval = 120  # seconds


def run():
    global event_num
    if os.path.exists(csv_path):
        event_num = get_event_num()
    else:
        with open(csv_path, 'w') as f:
            f.write(csv_header)
    while not esc_key_pressed():
        log = record()
        if not is_idling(log):
            with open(csv_path, 'a') as f:
                writer = csv.writer(f)
                writer.writerows(log)


def record():
    ''' record the position of the mouse cursor on screen every 8 milliseconds
    (Windows default mouse polling rate) sleep() on Windows has a resolution
    of about 10 milliseconds - not ideal'''
    global event_num
    log = []
    while time.time() % save_interval != 0:
        while not mouse_click():
            start = time.time()
            pos = win32api.GetCursorPos()
            log.append([event_num, pos[0], pos[1], get_epoch_ms()])
            time.sleep(0.008 - (max(0, time.time() - start)))
            if mouse_click():
                event_num += 1
    return log


def get_event_num():
    with open(csv_path, 'rb') as f:
        f.seek(-2, os.SEEK_END)
        while f.read(1) != b'\n':
            f.seek(-2, os.SEEK_CUR)
        last_line = f.readline().decode()
        return int(last_line.strip().split(',')[0])


def is_idling(data):
    if len(data) > 2:
        if data[0][1] == data[len(data)//4][1]:
            return True
    return False


def get_epoch_ms():
    ''' get an exact time in microseconds since Jan 1st, 2020 at 12:00 AM,
    this is exactly 50 years after UNIX epoch'''
    time_ms = (datetime.now().year - 2020) * 31556952000000
    time_ms += (datetime.now().month - 1) * 2592000000000
    time_ms += (datetime.now().day - 1) * 86400000000
    time_ms += datetime.now().hour * 3600000000
    time_ms += datetime.now().minute * 60000000
    time_ms += datetime.now().second * 1000000
    time_ms += datetime.now().microsecond
    return time_ms


def esc_key_pressed():
    return (win32api.GetAsyncKeyState(win32con.VK_ESCAPE) != 0)


def mouse_click():
    return (win32api.GetAsyncKeyState(win32con.VK_LBUTTON) != 0)
            
run()
                

                
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        
    
    