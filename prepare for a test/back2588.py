A = int(input())  # 첫 번째 입력 문자: 숫자로 변환
B = input()       # 두 번째 입력 문자: 문자로 유지

# 문자열 인덱스를 이용해 두 번째 입력 문자를 하나씩 숫자로 변환, A와 곱함.
AxB2 = A * int(B[2])
AxB1 = A * int(B[1])
AxB0 = A * int(B[0])
AxB = A * int(B)

print(AxB2, AxB1, AxB0, AxB, sep='\n')
