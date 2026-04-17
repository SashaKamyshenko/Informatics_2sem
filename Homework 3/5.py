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


def find(text, s):
    n, m = len(text), len(s)
    pieces = []
    i = 0
    while i < m:
        if s[i] == "?":
            i += 1
            continue
        j = i
        while j < m and s[j] != "?":
            j += 1
        pieces.append((s[i:j], i))
        i = j

    if not pieces:
        return list(range(n - m + 1))

    pos = set(range(n - m + 1))

    for piece, pos2 in pieces:
        combined = piece + "#" + text
        z = z_function(combined)
        plen = len(piece)

        new_pos = {
            i - plen - 1 - pos2
            for i in range(plen + 1, len(combined))
            if z[i] >= plen and 0 <= i - plen - 1 - pos2 <= n - m
        }

        pos &= new_pos

    return sorted(pos)


print(find("ababbaca", "a?a"))
