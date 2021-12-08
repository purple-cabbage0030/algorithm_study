# quiz
# https://programmers.co.kr/learn/courses/30/lessons/12922


# 문제 설명
# 길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.

# 제한 조건
# n은 길이 10,000이하인 자연수입니다.



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
# // 몫 % 나머지
