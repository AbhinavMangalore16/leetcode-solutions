# Last updated: 8/27/2026, 4:28:10 AM
1class Solution:
2    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
3        nums=s.count("1")
4        if nums<k:
5            return ""
6        ones=[]
7        for i in range(0,len(s)):
8            if s[i]=='1':
9                ones.append(i)
10        start=ones[0]
11        end=ones[k-1]
12        pointer=1
13        ans=s[start:end+1]
14        for i in range(end+1,len(s)):
15            if s[i]=='1':
16                ones.append(i)
17                start=ones[pointer]
18                end=i
19                pointer+=1
20                curr=s[start:end+1]
21                if len(curr)<len(ans) or len(curr)==len(ans) and curr<ans:
22                    ans=curr  
23        return ans