# quiz
# https://programmers.co.kr/learn/courses/30/lessons/42586

# solution
# resource: https://huidea.tistory.com/15

def solution(progresses, speeds):

    answer = []
    time = 0
    count = 0
    
    while len(progresses)> 0:
        # 기능이 완성되면 queue에서 pop
        if (progresses[0] + time*speeds[0]) >= 100: 
            progresses.pop(0)
            speeds.pop(0)
            count += 1

        # 완성된 기능을 출시시키고, count 초기화    
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
