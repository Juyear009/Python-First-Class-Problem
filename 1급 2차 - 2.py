def func_a(subt, curt):  # 분으로 바꾸기
    if int(subt[0:2]) < int(curt[0:2]):
        return -1
    elif int(subt[0:2]) >= int(curt[0:2]):
        subt1 = int(subt[0:2]) * 60
        result_subt = subt1 + int(subt[3:5])
        curt1 = int(curt[0:2]) * 60
        result_curt = curt1 + int(curt[3:5])
        return result_subt - result_curt


def solution(subway_times, current_time):  # 결과 return
    for i in range(len(subway_times)):
        result = func_a(subway_times[i], current_time)
        if result == -1:
            continue
        elif result >= 0:
            break
    return result


# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
subway_times1 = ["05:31", "11:59", "13:30", "23:32"]
current_time1 = "12:00"
ret1 = solution(subway_times1, current_time1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")
subway_times2 = ["14:31", "15:31"]
current_time2 = "15:31"
ret2 = solution(subway_times2, current_time2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")
