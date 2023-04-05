"""Given an unsorted array A of size N that contains only positive integers, find a continuous sub-array that adds to a given number S and return the left and right index(1-based indexing) of that subarray.

In case of multiple subarrays, return the subarray indexes which come first on moving from left to right."""

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
        left, right, sum = 0, 0, arr[0]
        while(right < n):
            if sum == s: 
                break
            if sum < s:
                right += 1
                if right < n:
                    sum += arr[right]
            else:
                sum -= arr[left]
                left += 1
        if sum == s and left <= right:
            return [left+1, right+1]
        return [-1]
                
       
