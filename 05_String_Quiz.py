# Quiz
## MY ANSWER
# web = input("사이트를 입력하시오. ")
web = "http://naver.com"
web1 = web[-9:] # 규칙 1
web2 = web1[:5] # 규칙 2
print(web2)
passw = web2[:3] + str(len(web2)) + str(web2.count("e")) + "!"
print("생성된 비밀번호 : ", passw)

## ANSWER
url = "http://naver.com"
# url = "http://daum.net"
# url = "http://youtube.com"

my_str = url.replace("http://", "") # 규칙 1
print(my_str)
my_str = my_str[:my_str.index(".")] # my_str[0:5] -> 0 ~ 5 직전까지 (0, 1, 2, 3, 4, 5)
print(my_str) # 규칙 2
password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))