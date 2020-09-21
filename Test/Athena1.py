# Python2
import bisect

class RollingMin(object):
    def __init__(self, interval_length):
        self.interval_length=interval_length
        self.interval=[]
        self.sorted_interval=[] # maintain a sorted interval
        self.time=[]

    # Returns the min in (time - intervalLength, time)
    def update(self, time, value):
        """returns the minimum, of type int"""
        # if len(self.sorted_interval)==self.interval_length:
        #     e = self.interval.pop(0)
        #     self.sorted_interval.remove(e)
        while self.time and self.time[0]<=(time-self.interval_length):
            t = self.time.pop(0)
            e = self.interval.pop(0)
            self.sorted_interval.remove(e)
        self.time.append(time)
        self.interval.append(value)
        bisect.insort(self.sorted_interval, value) # maintain a sorted interval
        return self.sorted_interval[0]


a=[2,3,3,4]
a.remove(3)
# bisect.insort(a,3)
print(a)