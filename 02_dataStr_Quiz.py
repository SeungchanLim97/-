from random import *
## my answer
lst = [1, 2, 3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(lst)
print(lst)
chiWinner = sample(lst, 1)
coffWinner = sample(lst, 3)
print("치킨 당첨자 :", chiWinner)
print("치킨 당첨자 :", coffWinner)
print("-- 축하합니다 --")

## answer
from random import *
users = range(1, 21) # 1부터 20까지 숫자를 생성
# print(type(users))
users = list(users)
# print(type(users))

print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명 중에서 1명은 치킨, 3명은 커피
print("--- 당첨자 발표 ---")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("--- 축하합니다 ---")
