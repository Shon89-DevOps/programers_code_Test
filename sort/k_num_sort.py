def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        pop = commands[i][2]
        sub_list = array[(commands[i][0])-1:commands[i][1]]
        sub_list.sort()
        answer.append(sub_list[pop-1])
    return answer
