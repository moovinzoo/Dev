# foo.txt에 저장되어 있는 모든 라인을 출력하라.

f = open('./DB_Test/Test_1/foo.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
