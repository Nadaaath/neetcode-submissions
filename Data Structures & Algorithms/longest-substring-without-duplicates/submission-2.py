class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        maxlength=0
        while r<len(s):
            if s[r] in s[l:r]:
                l=l+1
            else:
                maxlength=max(maxlength,r-l+1)
                r=r+1
        return maxlength




            

        