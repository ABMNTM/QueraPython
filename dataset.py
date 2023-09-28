def checker(datas:dict , testcases:list):
    anses = list()
    t = {}
    for testcase in testcases:
        if testcase in datas.keys():
            anses.append(datas[testcase])
        else:
            anses.append("Unknown")
    return anses

n, q, l = [int(item) for item in input().split()]
dataset = {}
for i in range(n):
    key, val = input().split()
    dataset[key] = val

tests = []
for i in range(q):
    tests.append(input())

finalAns = checker(dataset , tests)

for ans in finalAns:
    print(ans)