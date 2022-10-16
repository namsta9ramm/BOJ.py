S = input()
q = int(input())
str_len = len(S)
check = True
sub_total = [0] * (str_len+1)
for i in range(q):
  char, start, end = input().split()
  start = int(start)
  end = int(end)
  while check:
    for j in range(str_len):
      if S[j] == char:
        sub_total[j + 1] += 1
      sub_total[j + 1] += sub_total[j]
    check = False
  
  print(sub_total[end+1] - sub_total[start])