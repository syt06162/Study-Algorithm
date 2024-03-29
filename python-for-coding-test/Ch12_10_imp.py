# Ch12_10
# https://school.programmers.co.kr/learn/courses/30/lessons/60059
# 기본 코드가 제공되므로 반드시 해당 링크에서 실행

def solution(key, lock):
    # key 가 더 작으면 크기 맞추기
    M = len(key)
    N = len(lock)
    
    sub = N - M
    if sub>0:
        for i in range(sub):
            key.append([0 for i in range(M)])
        for i in range(N):
            for j in range(sub):
                key[i].append(0)
                
                
    # 옮겨가며 key lock 맞나 확인
    for k in range(0,4):
        key = matrix_rotation_clock_90(key)
        for i in range(-N , N+1):
            for j in range(-N , N+1):
                if isMatch( move_row_col(key, i, j), lock) == True:
                    return True
    return False
    

def matrix_rotation_clock_90(matrix):
    N = len(matrix)
    result = [ [0 for i in range(N)] for i in range(N)]
    
    for i in range(N):
        for j in range(N):
            result[j][N-1-i] = matrix[i][j]
    
    return result

def move_row_col(matrix, row, col):
    N = len(matrix)
    result = [ [0 for i in range(N)] for i in range(N)]
    
    ptr_row = 0 + row
    ptr_col = 0 + col

    for i in range(0, N):
        for j in range(0, N):
            now_row = ptr_row + i
            now_col = ptr_col + j
            if now_row<0 or now_row>=N or now_col<0 or now_col>=N:
                continue
            else:
                result[now_row][now_col] = matrix[i][j]
    
    return result

def isMatch(key, lock):
    length = len(key)
    for i in range(length):
        for j in range(length):
            if key[i][j] + lock[i][j] != 1:
                return False
    
    return True
        