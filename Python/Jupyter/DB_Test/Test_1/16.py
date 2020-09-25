# def reverse_r(str):
#     len_str = len(str)
#     if len_str > 1:
#         return (str[len_str-1] + reverse_r(str[0:(len_str - 1)]))
#     else:
#         return str

# def reverse_i(str):
#     return_str = ""
#     for i in range(len(str)):
#         return_str += (str[len(str) - (i+1)])
#     print(return_str)

def reverse_r(str):
    if str == "":
        return ""
    else:
        return reverse_r(str[1:]) + str[0]


def reverse_i(str):
    rev = ""
    for ch in str:
        rev = ch + rev
    return rev
    # return_str = ""
    # for i in range(len(str)-1, -1, -1):
    #     return_str += str[i]
    # return return_str
    # rev = ""


print(reverse_r("Hello"))
print(reverse_i("Hello"))

# def reverse_i(str):

# reverse_i("Hello")

# str1 = "Hello"
# print(str1[1:2])
# print(str1[:2])
# print(str1[:-1])
# print(str1[1:])
# print(str1[1:-1])
# print(str1[-1:1])  # nothing
# e
# He
# Hell
# ello
# ell
