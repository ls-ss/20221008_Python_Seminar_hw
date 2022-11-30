class Init:
    def __init__(self):
        self.lst = []

    def add_number(self, num):
        self.lst.append(num)


class MinStat(Init):
    def result(self):
        return min(self.lst) if self.lst else None


class MaxStat(Init):
    def result(self):
        return max(self.lst) if self.lst else None


class AverageStat(Init):
    def result(self):
        return sum(self.lst) / len(self.lst) if self.lst else None
