'''
选择题：
BACCBBA
填空题：
3.O(n),O(1)
4.O(n),O(n^2)
5.O(n),O(1)
'''
def takeDifference(sqlist1,sqlist2):
    return [x for x in sqlist1 if x not in sqlist2]

# if __name__ == '__main__':
#     s = input("顺序表1\n").strip()
#     s = s[1:-1]
#     sqlist1 = [int(x) for x in s.split(',')]
#     s = input("顺序表2\n").strip()
#     s = s[1:-1]
#     sqlist2 = [int(x) for x in s.split(',')]
#     result = takeDifference(sqlist1, sqlist2)
#     print("差集：", result)