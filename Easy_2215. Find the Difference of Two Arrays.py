class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        answer = []
        sub_answer = []

        for i in nums1:
            if i not in nums2 and i not in sub_answer:
                sub_answer.append(i)
                # print("sub_answer, loop1: ", sub_answer)
        
        answer.append(sub_answer)

        sub_answer = []

        for i in nums2:
            if i not in nums1 and i not in sub_answer:
                sub_answer.append(i)
                # print("sub_answer, loop2: ", sub_answer)

        answer.append(sub_answer)

        return answer


        ###################### from solutions ######################
        # set1, set2 = set(nums1), set(nums2)
        # return [list(set1 - set2), list(set2 - set1)]

