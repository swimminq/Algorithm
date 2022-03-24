# 거슬러 줘야 할 돈이 n원일 때, 최소 동전의 수


coin = [500,100,50,10]

n = int(input("거스름 돈을 입력하세요 : "))

result = 0

for i in coin:
    count = 0
    count = n // i
    n = n - (i * count)
    print(i, "원 동전 개수:", count)
    
    result += count

print("거슬러 줘야하는 동전의 수 :", result)
