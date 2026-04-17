def kmp(text, s):
    n = len(s)
    p = [0] * n
    for i in range(1, n):
        k = p[i - 1]
        while k > 0 and s[k] != s[i]:
            k = p[k - 1]
        if s[k] == s[i]:
            k += 1
        p[i] = k
    count = 0
    j = 0

    for ch in text:
        while j > 0 and ch != s[j]:
            j = p[j - 1]
        if ch == s[j]:
            j += 1
        if j == n:
            count += 1
            j = p[j - 1]

    return count


def count(text, s):
    n = len(s)
    if n == 0:
        return 0

    total = 0

    for i in range(n):
        shift = s[i:] + s[:i]
        cnt = kmp(text, shift)
        total += cnt
        print(shift, cnt)
    return total


text = "ababac"
s = "ba"


result = count(text, s)
print(result)
