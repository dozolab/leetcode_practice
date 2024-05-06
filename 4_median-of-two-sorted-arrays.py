class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        len_1=len(nums1)
        len_2=len(nums2)
        nums3=[]
        index1=0
        index2=0
        while index1<len_1 or index2<len_2:
            print(index1,index2)
            num1, num2=None, None
            if index1<len_1:
                num1=nums1[index1]
            if index2<len_2:
                num2=nums2[index2]
            if num1 is None:
                nums3.append(num2)
                index2+=1
            if num2 is None:
                nums3.append(num1)
                index1+=1
            if num1 is not None and num2 is not None:
                if num1<num2:
                    index1+=1
                    number_to_add=num1
                else:
                    index2+=1
                    number_to_add=num2
                nums3.append(number_to_add)
        len3=len(nums3)
        if len3%2==1:
            return nums3[len3//2]
        return (nums3[len3//2-1]+nums3[len3//2])/2
list_1=[0,0]
list_2=[0,0]
print(Solution().findMedianSortedArrays(list_1,list_2))