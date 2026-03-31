# Last updated: 3/31/2026, 9:37:19 PM
class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))
        
        # Track the last occurrence of each digit (0-9)
        last = {int(d): i for i, d in enumerate(num_list)}
        
        # Traverse the number from left to right
        for i, digit in enumerate(num_list):
            # Check for a larger digit to swap
            for d in range(9, int(digit), -1):
                if last.get(d, -1) > i:
                    # Swap and return the new number
                    num_list[i], num_list[last[d]] = num_list[last[d]], num_list[i]
                    return int(''.join(num_list))
        
        # If no swap occurred, return the original number
        return num 