class Solution:
    def dailyTemperatures(self, temperatures: List[int] ) -> List[int]:
        st = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            if len(st) != 0 and temperatures[i] <= st[-1][0]:
                st.append([temperatures[i], i]) 
            if len(st) != 0 and temperatures[i] > st[-1][0]:
                while len(st) != 0 and temperatures[i] > st[-1][0]:
                    a = st.pop()
                    res[a[1]] = i - a[1]
                st.append([temperatures[i], i])
            else:
                st.append([temperatures[i], i])
        return res