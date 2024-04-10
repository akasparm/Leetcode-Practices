class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = []
        for a in nums1:
            l.append(a)
        for b in nums2:
            l.append(b)
        l.sort()
        
        if(len(l)%2 == 0):
            return ((l[int(len(l)/2)] + l[int(len(l)/2) - 1])/2)
        else:
            return (l[int(len(l)/2)])