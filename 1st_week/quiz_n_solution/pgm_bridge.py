# quiz
# https://programmers.co.kr/learn/courses/30/lessons/42583

# solution
# resource: https://this-programmer.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Level2%ED%8C%8C%EC%9D%B4%EC%8D%AC3python3-%EB%8B%A4%EB%A6%AC%EB%A5%BC-%EC%A7%80%EB%82%98%EB%8A%94-%ED%8A%B8%EB%9F%AD


def solution(bridge_length, weight, truck_weights):
    answer = 0
    trucks_on_bridge = [0] * bridge_length

    while len(trucks_on_bridge):
        answer += 1
        trucks_on_bridge.pop(0)

        if truck_weights:
            if sum(trucks_on_bridge) + truck_weights[0] <= weight:
                trucks_on_bridge.append(truck_weights.pop(0))
            else:
                trucks_on_bridge.append(0)

    return answer


'''
At first, I tried to use queue starting as an empty list.
But the function ended up too long and complicated.
while true문 무한반복... 그걸 깨는 게 break
while 1도 같은 기능? while 0이 되면 없다가 돼서 false돼서 break되는 것.
if문은 오른쪽의 값이 있어야 true.
'''
