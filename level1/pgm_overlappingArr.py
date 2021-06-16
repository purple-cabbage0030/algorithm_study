# quiz
# https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    
    for v in range(len(arr)):
        if arr[0] not in answer:
            answer.append(arr[0])
        elif arr[v] != arr[v-1]:
            answer.append(arr[v])
    
    return answer


# 슬라이싱 이용한 해법
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
    