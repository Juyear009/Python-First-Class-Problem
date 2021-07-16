def solution(money):
    coin = [10, 50, 100, 500, 1000, 5000, 10000, 50000]
    counter = 0
    idx = len(coin) - 1
    while money:
        counter += money // coin[idx]
        money = money % coin[idx]
        idx -= 1
    return counter


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
print("solution 함수의 반환 값은", solution(2760), "입니다.")
