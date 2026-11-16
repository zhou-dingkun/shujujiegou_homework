a=[x for x in range(100)]
def memory_loc(a,i):
    return id(a[i])#用于获取a[i]的内存地址
print("a[0]的内存地址:",memory_loc(a,0))