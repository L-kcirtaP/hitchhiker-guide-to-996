#coding=utf-8
import sys 
#str = input()
#print(str)
import heapq
import time

class Log:
    def __init__(self, login_time, logout_time):
        self.login_time = login_time
        self.logout_time = logout_time
    def __lt__(self, other):
        return self.logout_time < other.logout_time


class UserStat:
    def __init__(self):
        self.min_heap = []
        heapq.heapify(self.min_heap)
        self.peak = 0
        self.during_peak = False
        self.peak_starting_time = 0
        self.peak_ending_time = 0
        self.peak_duration = 0
    
    def push(self, log):
        if self.min_heap:
            while log.login_time >= self.min_heap[0]:
                popped = heapq.heappop(self.min_heap)
                if self.during_peak and len(self.min_heap) == self.peak-1:
                    self.peak_ending_time = popped.logout_time
                    self.during_peak = False
                    self.peak_duration = self.peak_ending_time - self.peak_starting_time

        heapq.heappush(self.min_heap, log)

        if len(self.min_heap) >= self.peak:
            self.peak = len(self.min_heap)
            self.peak_starting_time = log.login_time
            self.during_peak = True
    
    def get_peak_number(self):
        return self.peak
    
    def get_peak_duration(self):
        return self.peak_duration
