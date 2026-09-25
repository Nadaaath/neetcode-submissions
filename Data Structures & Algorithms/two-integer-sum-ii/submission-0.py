class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index1=0
        n=len(numbers)
        index2=n-1
        while index2>index1:
            if numbers[index2]+numbers[index1]>target:
                index2=index2-1
            if numbers[index2]+numbers[index1]<target:
                index1+=1
            if  numbers[index2]+numbers[index1]==target:
                return[index1+1,index2+1]
                
        


        