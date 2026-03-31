# Last updated: 3/31/2026, 9:29:00 PM
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        c = 0
        lp = 0
        vowel = {}
        consonant = 0
        subs = 0

        def remove_char(char):
            if char in {'a', 'e', 'i', 'o', 'u'}:
                vowel[char] -= 1
                if vowel[char] == 0:
                    del vowel[char]
            else:
                nonlocal consonant
                consonant -= 1

        for rp in range(len(word)):
            char = word[rp]

            if char in {'a', 'e', 'i', 'o', 'u'}:
                vowel[char] = vowel.get(char, 0) + 1
            else:
                consonant += 1
                c = 0

            while consonant > k:
                remove_char(word[lp])
                lp += 1

            while consonant == k and len(vowel) == 5:
                c += 1
                remove_char(word[lp])
                lp += 1

            subs += c

        return subs