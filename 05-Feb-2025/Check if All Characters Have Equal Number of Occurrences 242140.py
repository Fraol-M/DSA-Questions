# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        

        count = Counter(s)

        count_set = set()
        for value in count.values():
            count_set.add(value)

        return len(count_set) == 1