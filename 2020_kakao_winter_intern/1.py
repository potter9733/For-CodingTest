def diverseDeputation(m, w):
    man = [0, m, (m * (m - 1)) // 2, ( m * (m - 1)*(m - 2)) // 6]
    wom = [0, w, (w * (w - 1)) // 2, ( w * (w - 1)*(w - 2)) // 6]
    
    
    
    return man[1] * wom[2] + man[2] * wom[1]



m = int(input())
w = int(input())
print(diverseDeputation(m, w))
