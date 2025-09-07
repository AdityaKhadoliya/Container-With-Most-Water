#This Code is writen by me using max number:

class Solution(object):
    def maxArea(self, height):
        
        # Finding the max number.
        # Initialize first and second max

        max1 = max2 = float('-inf')

        for num in height:
            if num > max1:
                max2 = max1 # Update Second max
                max1 = num # Udate mmax
            
            elif num > max2 and num != max1:
                max2 = num # Update second max if smaller than max1
            
            
        result = max2 * max2

        return result
    
sol = Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))
print(sol.maxArea([1,2,3]))

# This code is by ChatGPT: Usig Two Pointer

def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        # Calculate current area
        width = right - left
        h = min(height[left], height[right])
        area = width * h
        max_area = max(max_area, area)

        # Move the pointer pointing to the smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


# Example usage
heights = [1,8,6,2,5,4,8,3,7]
print(maxArea(heights))   # Output: 49
