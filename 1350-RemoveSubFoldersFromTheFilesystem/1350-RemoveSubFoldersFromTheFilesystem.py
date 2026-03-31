# Last updated: 3/31/2026, 9:35:16 PM
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        first = [folder[0]]
        for f in range(1, len(folder)):
            last = first[-1] + '/'
            if not folder[f].startswith(last):
                first.append(folder[f])
        return first