class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num1 = len(nums1)
        num2 = len(nums2)
        index = num1 + num2
        pointer1, pointer2 = 0, 0
        new_lst = []
        while pointer1 < num1 and pointer2 < num2:
            if nums1[pointer1] < nums2[pointer2]:
                new_lst.append(nums1[pointer1])
                pointer1 += 1
            else:
                new_lst.append(nums2[pointer2])
                pointer2 += 1
        if pointer1 == num1:
            new_lst  = new_lst + nums2[pointer2:]
        else:
            new_lst = new_lst + nums1[pointer1:]
        if index % 2 == 0:
            return (new_lst[index // 2 - 1] + new_lst[index //2])/2
        else:
            return new_lst[index // 2] / 1.0
