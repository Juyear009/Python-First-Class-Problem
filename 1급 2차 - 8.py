def solution(arr):
    result = []
    while len(arr) > 0:
        a = arr.pop(0)
        result.append(a)
        a = arr.pop(-1)
        result.append(a)
    return result

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
print("반환 값은 ", solution([1, 2, 3, 4, 5, 6]), " 입니다.")
