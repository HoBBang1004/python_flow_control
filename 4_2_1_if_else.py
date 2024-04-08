

#결과 값 : 0 1 3 (print(2)는 false일때라 출력안됨)
print(0)
if True:
    print(1)
else:
    print(2)
print(3)


print('-----------------------------')


# 0 2 3 (이번엔 print(1)이 false라 출력안됨)
print(0)
if False:
    print(1)
else:
    print(2)
print(3)