# quiz
# https://programmers.co.kr/learn/courses/30/lessons/42584

# solution
# resource: https://deftkang.tistory.com/175

def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    while stack:
        i = stack.pop()
        answer[i] = len(prices) - 1 - i
    return answer
