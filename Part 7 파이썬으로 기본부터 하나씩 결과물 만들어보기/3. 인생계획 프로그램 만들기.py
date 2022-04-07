long = '''
  __  ___   ___  
 /_ |/ _ \ / _ \ 
  | | | | | | | |
  | | | | | | | |
  | | |_| | |_| |
  |_|\___/ \___/

'''

print(long)
print("!!100세 시대!!")
print("100세, 나는 어떤 모습일까요")
print("상상이 되시나요?")

age = int(input("현재의 나이를 입력하세요"))
print("여기까지 달려오셨어요")
front_age = int(100 - age)
print("*" * age, end = "")
print("-" * front_age)
print()
print("세상은 넓고,우리에게는 수많은 기회와 새로운 도전들이 기다리고 있어요")
print("지금부터")
print("="*30)

print('일년에 한번씩 새로운 취미 만들기에 도전한다면 ' f"{front_age:,}" '개의 새로운 도전이 기다리고 있어요')
month = int(front_age * 12)
print("한달에 한번씩 여행을 간다면 " f"{month:,}" "곳에서 추억을 쌓을수가 있어요")
week =  int(front_age * 52)
print("일주일에 책 한권씩 읽는다면 " f"{week:,}" "권의 지혜를 얻을수 있어요")
day = int(front_age * 365)
print("하루에 1개씩 영어 단어를 외우면 " f"{day:,}" "개의 영어 단어를 익힐수 있어요")
print("일반 원어민의 어휘력은 20,000입닏다.")
print("="*30)