heigh = [0,1,0, 2,1,0, 1,3,2, 1,2,1]
def trap(height):
  if not height:
    return

  volume = 0
    # LEFT= 0  , RIGHT=11
  left, right = 0, len(height) - 1
  left_max, right_max = height[left], height[right]
  # 0 , 1
  # 2, 11
  while left < right:
    left_max, right_max = max(height[left], left_max), max(height[right], right_max)
    # 0 1
    if left_max <= right_max:
      volume += left_max - height[left]
      left += 1
    else:
      volume += right_max - height[right]
      right -= 1
  return volume

print(trap(heigh))