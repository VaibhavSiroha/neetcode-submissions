class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        maxarea=0
        i=0
        j=len(heights)-1
        while i<j:
            size=j-i
            hmin=min(heights[i],heights[j])
            area=hmin*size
            maxarea=max(area,maxarea)
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
        return(maxarea)
