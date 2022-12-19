import random


class ProduceChars:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        current = self.start
        while current < 3:
            yield random.randrange(self.start, self.stop)
            current += 1
