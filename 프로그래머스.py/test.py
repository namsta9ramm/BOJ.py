new_list=[[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
for i in new_list:
    if 4 in i:
        print(new_list.index(i),i.index(4))
    