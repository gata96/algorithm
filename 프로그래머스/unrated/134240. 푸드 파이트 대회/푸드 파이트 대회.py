answer = ''
def solution(food):
    global answer
    for i in range(1,len(food)):
        mok = (food[i] // 2)  # mok = 3, 0, 1
        answer += str(i) * mok # 1113
    return answer+'0'+answer[::-1]
