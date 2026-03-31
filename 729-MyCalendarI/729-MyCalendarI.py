# Last updated: 3/31/2026, 9:37:09 PM
class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.events:
            if not (end<=s or start>=e):
                return False
        self.events.append((start, end))
        return True  


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)