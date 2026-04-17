def z_function(s):
    zf = [0] * len(s)
    left, right = 0, 0
    for i in range(1, len(s)):
        zf[i] = max(0, min(zf[i - left], right - i))
        while i + zf[i] < len(s) and s[zf[i]] == s[i + zf[i]]:
            zf[i] += 1
        if i + zf[i] > right:
            left, right = i, i + zf[i]
    return zf


def count_prefixes(s):
    n = len(s)
    z = z_function(s)
    result = [1] * n

    for i in range(1, n):
        for length in range(1, z[i] + 1):
            result[length - 1] += 1

    return result


s = "ababa"
print(count_prefixes(s))
