# Greedy 02

#내 풀이

#행, 열 입력받기
n, m = map(int, input().split())

# 행 리스트로 입력받기(이게 오래 걸리네)
final_list = []  # 빈 리스트 생성해주고
for i in range(n):
  data = int(min(list(map(
    int,
    input().split()))))  #리스트 입력받아서 그 중 최소값을 data에 int 형식으로 저장
  final_list.append(data)  # 최소값을 모아놓은 리스트 생성
print(max(final_list))  # 그 중 최대값 출력

# main()함수를 이용하는 답안 예

# N,M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 '가장 작은 수' 찾기
  min_value = min(data)
  # '가장 작은 수'들 중에서 가장 큰 수 찾기
  result = max(result, min_value)

print(result)

# 2중 반복문 구조를 이용하는 답안 예시
# N,M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한줄씩 입력받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 '가장 작은 수' 찾기
  min_value = 10001
  for a in data:
    min_value = min(min_value, a)

  result = max(result, min_value)

print(result)
