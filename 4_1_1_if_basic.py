
# if문은 java와 다르게 if(조건문) 작성할 필요 없음 
# if문은 true일때만 출력함 / false는 출력안함
# if True:
#   조건문 (대신 들여쓰기 해야함, 단 아래에 작성할 조건문도 다 같은 횃수로 들여써야 함)
# 보통은 Tap키를 많이 쓴다고 함


# 제대로 실행이 안됨/ 결과 : 0 1 2
print(0)
if True:
    print(1)
print(2)


print('----------------------')

# 결과값 : 0 2  (1은 false라서 출력안함)
print(0)
if False:
    print(1)
print(2)



