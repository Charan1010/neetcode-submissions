class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0 
        right = len(heights) - 1
        max_area = (right - left)* min(heights[left], heights[right])

        while left < right:

            net_width = right - left

            height_left = heights[left]
            height_right = heights[right]

            if height_left < height_right:

                net_height = height_left
                if net_height*net_width > max_area:
                    max_area =  net_height*net_width

                left += 1

            elif height_left > height_right:
                net_height = height_right
                if net_height*net_width > max_area:
                    max_area =  net_height*net_width

                right -= 1

            else:
                net_height = height_left
                if net_height*net_width > max_area:
                    max_area =  net_height*net_width
                left += 1

        return max_area

    


        