# 다음은 두개의 숫자를 받아서 나누기를 수행하는 프로그램
# 오류가 발생하는 경우를 고려하여 예외처리함
# Traceback을 참고하여 다음 코드의 빈칸을 채우세요

print("Give me two numbers and I'll divide them.")
print("Enter 'q' to exit.")

while True:
    first_number = input("\nFirst number : ")
    if first_number == 'q':
        break
    second_number = input("Second number : ")

    try:
        answer = int(first_number) / int(second_number)
    
        print("You can't divide by 0!")
    else:
        print(answer)

    # except ZeroDivisionError as e:
    #     print("You can't divide by 0!")
    #     print(e)
    # else:
    #     print(answer)
