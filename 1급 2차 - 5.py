def solution(arr):
    arr.append(0)
    list = []
    cnt = 0
    result = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            cnt += 1
        elif arr[i] <= arr[i - 1]:
            list.append(cnt + 1)
            cnt = 0
    for i in list:
        if i > result:
            result = i
    return result


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [3, 1, 2, 4, 5, 1, 2, 2, 3, 4]
ret = solution(arr)
print("solution 함수의 반환 값은", ret, "입니다.")
