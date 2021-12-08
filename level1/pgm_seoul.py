# quiz
# https://programmers.co.kr/learn/courses/30/lessons/12919


# 문제 설명
# String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. 
# seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

# 제한 사항
# seoul은 길이 1 이상, 1000 이하인 배열입니다.
# seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
# "Kim"은 반드시 seoul 안에 포함되어 있습니다.


def solution(seoul):
    answer = ''
    
    x = seoul.index('Kim')
    answer = '김서방은 '+str(x)+'에 있다'
    
    return answer


'''
index(value) 함수는 해당하는 문자열의 위치값을 반환해준다. 
list.index(10,2,9) #index(value, start, end) 
list.index('1') #list 문자열에 '1'이라는 문자 위치 찾기 
만약 찾고자하는 value가 없을 경우에는 예외 처리를 해줘야한다. 


출처: https://wooaoe.tistory.com/69 [개발개발 울었다]
'''

def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))
    