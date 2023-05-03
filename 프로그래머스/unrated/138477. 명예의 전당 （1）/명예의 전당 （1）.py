def solution(k,score):
    lst = []
    answer = []
    for i in range(len(score)):
        lst.append(score[i])

        if len(lst) <= k and score[i] < min(lst):
            continue
            
        elif len(lst) > k:
            lst = sorted(lst)
            lst.pop(0)
        answer.append(min(lst))
    return answer
        

        