words = ['frodo','front','frost','frozen','frame','kakao']

queries = ['fro??','????o','fr???','fro???','pro??']

def vs(query, word):
    list_q = []
    list_w = []
    idx = []
    
    for i in range(1, len(word)+1):
        list_w.append([i, word[i-1]])
        
    for i in range(1, len(query)+1):
        list_q.append([i, query[i-1]])
    
    for i in range(len(list_q)):
        if list_q[i][1] == '?':
            idx.append(list_q[i][0])
            
    for i in list_w:
        for j in idx:
            if j == i[0]:
                list_w[j-1][1] = '?'
    
    if list_w == list_q:
        return True
        
    else:
        return False
    
def solution(queries, words):            
    answer = [] 
    for query in queries:
        n = 0
        for word in words:
            result = vs(query, word)
            if result == True:
                n += 1
        answer.append(n)
    
    return answer            