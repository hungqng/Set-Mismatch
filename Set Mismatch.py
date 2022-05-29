# 645. Set Mismatch

# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

# You are given an integer array nums representing the data status of this set after the error.

# Find the number that occurs twice and the number that is missing and return them in the form of an array.

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        rep, mis = None, None
        lookup = Counter(nums)
        
        for i in range(1, len(nums) + 1):
            if i not in lookup:
                mis = i
            if lookup[i] > 1:
                rep = i
        return [rep,mis]