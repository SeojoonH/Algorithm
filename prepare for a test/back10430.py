
A, B, C = map(int,input().split())
# input은 문자열 반환, 따라서 int로 타입 변환 필요.
# split은 문자열 나누는 함수, sep=파라미터로 문자열 구분 기호 입력 가능, 아무것도 없을 경우 공백으로 문자를 나눔.
print((A+B)%C, ((A%C)+(B%C))%C, (A*B)%C, ((A%C)*(B%C))%C, sep='\n')
# 각 입력식을 쉼표로 구분
# 각 값을 세로로 출력해야 하므로 sep=파라미터에 '\n' 입력, 줄바꿈