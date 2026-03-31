# Last updated: 3/31/2026, 9:36:14 PM
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for e in emails:
            l, d = e.split("@")
            loc = l.split("+")[0].replace(".","")
            s.add(loc+"@"+d)
        return len(s)