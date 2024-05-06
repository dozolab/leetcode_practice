class Solution:
    def maxArea(self, height: list[int]) -> int:
        area=0
        last_index=len(height)-1
        first_index=0
        while first_index<last_index:
            width=last_index-first_index
            first_item=height[first_index]
            last_item=height[last_index]
            if first_item>last_item:
                current_height=last_item
                last_index-=1
            elif first_item<last_item:
                current_height=first_item
                first_index+=1
            else:
                current_height=first_item
                last_index-=1
                first_index+=1
            current_area=width*current_height
            if current_area>area:
                area=current_area
        return area