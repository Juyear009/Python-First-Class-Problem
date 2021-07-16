def solution(commands):
    list = [0, 0]
    for i in range(len(commands)):
        if commands[i] == 'L':
            list[0] = list[0] - 1

        elif commands[i] == 'R':
            list[0] = list[0] + 1

        elif commands[i] == 'U':
            list[1] = list[1] + 1

        elif commands[i] == 'D':
            list[1] = list[1] - 1

    return list


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
commands = "URDDL"
ret = solution(commands)
print("solution 함수의 반환 값은 ", ret, " 입니다.")
