def solution(s):
    # #s = '{{1,2,3},{2,1},{1,2,4,3},{2}}'
    # s = s.replace('{{','')
    # s = s.replace('},{',' ')
    # s = s.replace('}}','')
    # s = s.split(' ')
    
    s = s.lstrip('{').rstrip('}').split('},{')
    
    result = []
    
    for i in range(len(s)):
        s[i] = sorted(s[i].split(','))
        
    s = sorted(s, key = len)
    
    for i in range(len(s)):
        for j in range(i + 1):
            s[i][j] = int(s[i][j])
            
    for i in range(len(s)):
        a = s[i][0]
        for j in range(i, len(s)):
            s[j].remove(a)
            print(s)
        result.append(a)
        
    return result