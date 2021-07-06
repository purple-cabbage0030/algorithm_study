# quiz
# https://programmers.co.kr/learn/courses/30/lessons/12954#qna

def solution(x, n):
    answer = [x*i for i in range(1, n+1)]
    return answer

# 6점 받았다 행복하다 ㅎㅎ

# 다른 풀이
def number_generator(x, n):
    return [i * x + x for i in range(n)]
