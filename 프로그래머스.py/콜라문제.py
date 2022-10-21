a,b,n=2,1,20
sub_ans=0
sub_ans2=0
ans=0
while n>=a:
    sub_ans=(n//a)*b   # (20//3)*2 =12
    sub_ans2=n%a       # 20%3 = 2
                       # (14//3)*2 = 8
                       # 14%3 = 2
                       # (10//3)*2 = 6
                       # 10%3 = 1
                       # (7//3)*2 = 4
                       # 7%3 = 1
                       # (5//3)*2 = 2
                       # 5%3 = 2
                       # (4//3)*2 = 2
                       # 4%3 = 1
                       # (3//3)*2 = 2
                       # 3%3 = 0
                       # (2//3)*2 = 0
                       # 2%3 = 2
    print(sub_ans,sub_ans2)
    n=sub_ans+sub_ans2                   
    ans=ans+sub_ans
print(ans)