def solution(X, Y):
    ans=''
    new_list=[]
    ans_list=[]
    print(list(set(X)&set(Y)))
    if len(list(set(X)&set(Y)))==0:
        return "-1"
    elif list(set(X)&set(Y))==['0']:
        return "0"
    else:
      for i in list(set(X)&set(Y)):
            if X.count(i)>Y.count(i):    # x=
                for _ in range(Y.count(i)):
                    new_list.append(i)
            else:
                for _ in range(Y.count(i)):
                    new_list.append(i)
      for k in new_list:
        ans_list.append(int(k))
      ans_list.sort(reverse=True)
      for k in ans_list:
        ans+=str(k)
      return ans
print(solution("000","00"))
    