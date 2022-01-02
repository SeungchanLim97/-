# 문자열처리 함수
python = 'Python is Amazing'
print(python.lower()) # 모두 소문자
print(python.upper()) # 모두 대문자
print(python[0].isupper()) # 첫문쨰 문자 대문자 소문자 여부
print(len(python)) # 문자의 길이
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1) # 두번째 "n"의 위치
print(index)

print(python.find("n"))
print(python.find("Java")) # 오류 없이 -1 반환
# print(python.index("Java")) # 오류

print(python.count("n")) # "n"이 총 몇번나왔는지
