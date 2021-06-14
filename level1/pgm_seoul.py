# quiz
# https://programmers.co.kr/learn/courses/30/lessons/12919


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
    