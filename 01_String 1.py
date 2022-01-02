# 문자열
sentence = "나는 소년입니다"
print(sentence)
sentence2 = " 파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

# 슬라이싱
id = "971230-1234567"

print("성별 : " + id[7])
print("연 : " + id[0:2]) # 0~2 직전까지 (0, 1)
print("월 : " + id[2:4])
print("일 : " + id[4:6])
print("생년월일 : " + id[:6]) # 처음부터 6 직전까지
print("뒤 7 자리 : " + id[7:]) # 7부터 끝까지
print("뒤 7 자리(뒤에부터) : " + id[-7:]) # 맨 뒤에서 7번쨰부터 끝까지