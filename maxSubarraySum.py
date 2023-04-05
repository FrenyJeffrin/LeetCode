"""Given an array Arr[] of N integers. 
Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum."""

class Solution:
    
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        
        maxend=0
        maxsum=0
        for i in range(N):
            maxend=maxend+arr[i]
            if(maxend>maxsum):
                maxsum=maxend
            if i==0:
                maxsum=maxend
            if(maxend<0):
                maxend=0
        return maxsum