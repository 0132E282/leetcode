from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sum_abs = 0;
        neg_count= 0;
        min_abs = float('inf');
        for i in matrix:
          for j in i:
            sum_abs += abs(j);
            min_abs = min(min_abs, abs(j));
            print(j);
            if(j < 0):
              neg_count += 1;

        if neg_count % 2 == 0:
          return sum_abs;
        else:
          return sum_abs - 2 * min_abs;

relust = Solution().maxMatrixSum([[1,2,3],[-1,-2,-3],[1,2,3]]);

print(relust);
