# 입력 받기
N, K = map(int, input().split())  # 칸의 개수 N, 명령의 개수 K
blocks = [0] * N  # 각 칸에 쌓인 블럭 수를 저장하는 리스트 (초기값은 0)

# 명령 처리
for _ in range(K):
    A, B = map(int, input().split())  # A부터 B까지 블럭 추가
    for i in range(A - 1, B):
        blocks[i] += 1

# 블럭 수를 오름차순으로 정렬
blocks.sort()

# 결과 출력
# 중간값 출력 (N은 항상 홀수이므로 중간값이 명확히 존재)
print(blocks[N // 2])
