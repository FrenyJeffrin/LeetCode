"""Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element."""
class Solution:
    def countTriplet(self, arr, n):
        
        dictt={}
        for i in arr:
            dictt[i]=1
        count=0
        for i in range(n):
            for j in range(i+1,n):
                if arr[i] + arr[j] in dictt.keys():
                    count += 1
                
        return count
                
