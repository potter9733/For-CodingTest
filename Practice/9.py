#문자열 압축
s = input()
n=len(s)
data = []
for x in range(1, (len(s) // 2) + 1):
    count = 1
    result = ''
    for y in range(0, len(s), x):
        if s[y:(y + x)] == s[(y + x):(y + x + x)]:
            count += 1
        else:
            if count != 1:
                result += str(count) + s[y:(y + x)]
            else:
                result += s[y:(y + x)]
            count = 1
    n = min(n, len(result))
print(n)