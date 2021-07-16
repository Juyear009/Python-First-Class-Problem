def solution(arr, K):  # 문제 해결 능력이 진짜 중요하다는 것을 깨달음
    cnt = 0  # 문제 읽을때는 간단해보였고 짤때도 간단했는데 짜고나니 알수없는 오류들이 많이 나옴....
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for x in range(j + 1, len(arr)):
                test = arr[i] + arr[j] + arr[x]
                if test % K == 0:
                    cnt += 1
    return cnt


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [1, 2, 3, 4, 5]
K = 3
ret = solution(arr, K)
print("solution 함수의 반환 값은 ", ret, " 입니다.")
