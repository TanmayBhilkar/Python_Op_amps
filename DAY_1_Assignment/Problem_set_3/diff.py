class Solution:
       def solve(self, L1, L2):
      L1.sort()
      L2.sort()
      ans = float("inf")
      i = j = 0
      while i < len(L1) and j < len(L2):
         ans = min(ans, abs(L1[i] - L2[j]))
         if L1[i] < L2[j]:
            i += 1
         else:
            j += 1
      return ans
ob = Solution()
L1 = [2, 7, 4] L2 = [16, 10, 11]
print(ob.solve(L1, L2))