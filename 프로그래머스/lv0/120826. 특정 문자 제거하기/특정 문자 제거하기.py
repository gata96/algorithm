def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if i != letter:
            answer += i
    return answer

# 방2
# def solution(my_string, letter):
#     answer = ''
#     for i in range(len(my_string)):
#         if my_string[i] != letter:
#             answer += my_string[i]
#     return answer


     
            