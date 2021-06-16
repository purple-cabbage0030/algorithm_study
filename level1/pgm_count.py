# quiz
# https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    answer = True

    if list( s.lower() ).count("p") != list( s.lower() ).count("y"):
        answer = False

    return answer

# how can I make this code simpler?


def numPY(s):
    return s.lower().count('p') == s.lower().count('y')
    