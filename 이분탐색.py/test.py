a=int(input())
list_a=list(map(int,input().split()))
b=int(input())
list_b=list(map(int,input().split()))
ans_list=[]
list_a.sort()
for k in range(b):
    flag=True
    target = list_b[k]
    
    length = len(list_a)

    left = 0 
    right = length-1
    #1 2 3 4 5
    #left=0 right=4 mid=2
    while left<=right:
        mid = (left+right)//2
        if list_a[mid] == target:
            flag=False
            break
        elif list_a[mid]>target:
            right = mid-1
        else :
            left = mid+1
    if flag==False:
        print(1)
    else:
        print(0)

