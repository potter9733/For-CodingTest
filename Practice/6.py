#무지의 먹방 라이브
def solution(food_times, k):
    answer = 0
    sec = 0
    food_times[answer] = food_times[answer] - 1
    
    while True:
        answer = (answer + 1) % len(food_times)
        
        if food_times[answer] == 0:
            answer = (answer + 1) % len(food_times)
            
        food_times[answer] = food_times[answer] - 1
        sec += 1
        
        #print(sec,'~',sec+1, answer + 1, food_times)
        if sec == k:
            break
    answer += 1
    return answer

print(solution([3,1,2] , 5))
    