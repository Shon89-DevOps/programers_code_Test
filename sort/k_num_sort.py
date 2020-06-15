def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        pop = commands[i][2]
        aa = array[(commands[i][0])-1:commands[i][1]]
        aa.sort()
        print ('aa :',aa)
        answer.append(aa[pop-1])
    return answer
