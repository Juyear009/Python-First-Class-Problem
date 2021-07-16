def solution(n):
    list = []
    result = 0
    cnt = n + 1
    for i in range(1, n * n + 1):
        list.append(i)
    for x in range(len(list)):
        if cnt == n + 1:
            result += list[x]
            cnt = 0
        cnt += 1
    return result


# The following is code to output testcase.
n1 = 3
ret1 = solution(n1)

# Press Run button to receive output.
print("Solution : return value of the function is ", ret1, ".")

n2 = 2
ret2 = solution(n2)

# Press Run nutton to receive output.
print("Solution : return value of the function is ", ret2, ".")
