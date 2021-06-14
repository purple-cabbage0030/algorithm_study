# quiz
# https://programmers.co.kr/learn/courses/30/lessons/12922


def solution(n):
    answer = ''
    
    for i in range(1, n+1):
        if i%2 != 0:
            answer = answer + '수'
        else:
            answer = answer + '박'
    
    return answer

# 생각지도 못한 풀이...

def solution(n):
    return "수박"*(n//2) + "수"*(n%2)
