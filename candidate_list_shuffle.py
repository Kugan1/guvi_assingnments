
n=int(input('enter no of candidate : '))
k=int(input('enter priority in the end of the list : '))
candidate_list=input(f'enter {n} candidate list : ').split(' ')


end_list=[]
for i in range(n-k,n):
    end_list.append(candidate_list[i])

new_list=end_list+candidate_list

shuffle=[]
for i in range(0,len(new_list)-k):
    shuffle.append(new_list[i])

if k<=0:
    for c_list in candidate_list:
        print(c_list,end=" ")
elif len(candidate_list) == n :
    for each in shuffle :
        print(each,end=" ")
else:
    print('check the length of candidate_list')