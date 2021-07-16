def solution(num):
    num += 1
    num = str(num)
    num_list = []
    result = ""
    for i in range(len(num)):
        num_list.append(num[i])

    for x in range(len(num_list)):
        if num_list[x] == '0':
            num_list[x] = '1'

    print(num_list)

    for k in range(len(num_list)):
        result += num_list[k]

    return result


# The following is code to output testcase.
num = 9949999
ret = solution(num)
print("Solution : return value of the function is ", ret, ".")
