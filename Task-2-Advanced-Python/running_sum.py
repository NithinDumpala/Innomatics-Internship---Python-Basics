Python 3.13.9 (tags/v3.13.9:8183fa5, Oct 14 2025, 14:09:13) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> class Solution:
...     def shuffle(self, nums: List[int], n: int) -> List[int]:
...         result = []
...         for i in range(n):
...             result.append(nums[i])      # take x_i
...             result.append(nums[i+n])    # take y_i
...         return result
... 
... # Example usage
... if __name__ == "__main__":
...     sol = Solution()
...     print(sol.shuffle([2,5,1,3,4,7], 3))       # [2,3,5,4,1,7]
...     print(sol.shuffle([1,2,3,4,4,3,2,1], 4))   # [1,4,2,3,3,2,4,1]
