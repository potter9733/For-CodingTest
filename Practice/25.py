def solution(N, stages):
    cons = []
    every = len(stages)
    stage = 0
    # while stage < N:
    #     stage += 1
    #     fail = stages.count(stage) / every
    for i in range(1, N+1):
        count = stages.count(i)
        
        if every == 0:
            fail = 0
        else:
            fail = count / every

    
        cons.append([stage, fail])
        every -= stages.count(stage)
    
        
        
    cons = sorted(cons, key = lambda x: x[1], reverse = True)
    
    cons = [i[0] for i in cons]
        
    print(cons)