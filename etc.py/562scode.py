list_blocks =list(map(int,input().split()))
water_block = 0
heigh = max(list_blocks)
a=len(list_blocks)
ind=1
for i in list_blocks[1:a-1]:
    
    while i <=heigh:
        i +=1
        if i<=max(list_blocks[:ind]) and i<=max(list_blocks[ind+1:]):
            water_block +=1
    
    ind=ind+1
print(water_block)