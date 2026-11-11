def get_next(p):
    """计算 next 数组，规定 next[0] = -1"""
    if not p:
        return []

    nxt = [-1] * len(p)
    j, k = 0, -1

    while j < len(p) - 1:
        if k == -1 or p[j] == p[k]:
            j += 1
            k += 1
            nxt[j] = k
        else:
            k = nxt[k]

    return nxt


# 方法一：课本版，i 表示本轮匹配起点
def kmp_book(T, P, begin=0):
    if not P:
        return begin

    nxt = get_next(P)
    i, j = begin, 0

    while i + j < len(T) and j < len(P):
        if T[i + j] == P[j]:
            j += 1
        elif j == 0:
            i += 1
        else:
            i += j - nxt[j]
            j = nxt[j]

    return i if j == len(P) else -1


# 方法二：老师 PPT 版，i 表示主串当前比较位置
def kmp_ppt(T, P, begin=0):
    if not P:
        return begin

    nxt = get_next(P)
    i, j = begin, 0

    while i < len(T) and j < len(P):
        if j == -1 or T[i] == P[j]:
            i += 1
            j += 1
        else:
            j = nxt[j]

    return i - j if j == len(P) else -1


# 测试
T = "ABAABAABDBCABABC"
P = "ABABCABABA"

print("next 数组:", get_next(P))
print("课本版匹配结果:", kmp_book(T, P))
print("PPT 版匹配结果:", kmp_ppt(T, P))
