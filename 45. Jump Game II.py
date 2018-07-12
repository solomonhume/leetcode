#45. Jump Game II, beat 97%

class Solution(object):
    def jump(self, n):
        if len(n)==1: return 0 
        l = len(n)-1
        s = 0
        f=n[0]
        count=1
        while f<l:
            s, f = f, max(i+ n[i] for i in range(s+1, f+1))
            count+=1
        return count
