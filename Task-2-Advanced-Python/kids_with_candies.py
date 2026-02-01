Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> from typing import List
... 
... class Solution:
...     def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
...         max_candies = max(candies)  # find the current maximum
...         result = []
...         for c in candies:
...             result.append(c + extraCandies >= max_candies)
...         return result
... 
... # Example usage
... if __name__ == "__main__":
...     sol = Solution()
...     print(sol.kidsWithCandies([2,3,5,1,3], 3))   # [True, True, True, False, True]
...     print(sol.kidsWithCandies([4,2,1,1,2], 1))   # [True, False, False, False, False]
