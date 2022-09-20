import sys
input=sys.stdin.readline
target=int(input())
n=int(input())
non=list(map(int,input().split()))

channel=abs(100-target)

for nums in range(1000001):
    nums=str(nums)
    #1,2,3, , , ,1000001 nums='5000'
    for j in range(len(nums)):
        if int(nums[j]) in non:
            break
        elif j==len(nums)-1:
            channel=min(channel,abs(int(nums)-target)+len(nums))

print(channel)