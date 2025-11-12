#!/usr/bin/env python3

class Time:
    def __init__(self, hour=12, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    s = Time(0, 0, 0)
    s.hour = t1.hour + t2.hour
    s.minute = t1.minute + t2.minute
    s.second = t1.second + t2.second
    if s.second >= 60:
        s.minute += s.second // 60
        s.second %= 60
    if s.minute >= 60:
        s.hour += s.minute // 60
        s.minute %= 60
    return s

def valid_time(t):
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True

def change_time(time, seconds):
    """Modify the given time object by adding 'seconds' (can be negative)."""
    time.second += seconds

    # normalize seconds upward
    while time.second >= 60:
        time.second -= 60
        time.minute += 1
    # normalize seconds downward (borrow from minutes)
    while time.second < 0:
        time.second += 60
        time.minute -= 1

    # normalize minutes upward
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1
    # normalize minutes downward (borrow from hours)
    while time.minute < 0:
        time.minute += 60
        time.hour -= 1

    # note: we do not wrap hours to 0–23 here unless assignment requires it
    return None
