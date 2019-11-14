# https://leetcode.com/problems/k-closest-points-to-origin/ 
# Logic: Sort based on the sum of square of (x,y). Choose first K elements
class Solution:
    # shreyas
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0]**2+x[1]**2)
        print(points)

        return points[0:K]
