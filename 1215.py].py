import time


print("프로그램 시작")

a = int(input())
start = time.time()
for y in range(a):
    print("죄송합니다" , y,"번")
print("실행시간 : ",time.time()-start)



start = time.time()
n = 0
while n<1000:
    print("열심히 하겠습니다",n)
    n = n+1
print("실행시간 : ",time.time()-start)

    





print("프로그램 종료")
