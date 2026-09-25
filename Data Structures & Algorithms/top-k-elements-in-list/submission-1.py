class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        D={}
        L=[]
        for num in nums:
            if num in D:
                D[num]=D[num]+1
            else:
                D[num]=1

        while k!=0:
            m=max(D.values())
            for num in list(D.keys()):
                if D[num]==m:
                    L.append(num)
                    D.pop(num)
                    k=k-1
                    break
        return L

                


        