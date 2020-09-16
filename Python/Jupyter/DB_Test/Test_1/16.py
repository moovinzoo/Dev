def reverse_r(str):
    len_str = len(str)
    if len_str > 1:
        return (str[len_str-1] + reverse_r(str[0:(len_str - 1)]))
    else:
        return str


def reverse_i(str):
    return_str = ""
    for i in range(len(str)):
        return_str += (str[len(str) - (i+1)])
    print(return_str)


reverse_i("Hello")
