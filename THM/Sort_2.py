#위에서 아래로

n = int(input())
data_list = []

for _ in range(3):
    data = int(input())
    data_list.append(data)
'''
data_list.sort()
data_list.reverse()
'''
data_list = sorted(data_list,reverse=True)

for i in data_list:
    print(i, end=' ')