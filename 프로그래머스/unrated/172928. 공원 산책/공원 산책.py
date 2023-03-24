def solution(park, routes):
    move = {'E': [0, 1], 'W': [0, -1], 'S': [1, 0], 'N': [-1, 0]}

    # 공원 세로/가로
    w, h = len(park[0])-1, len(park)-1
    x, y = [[i, row.index('S')] for i, row in enumerate(park) if 'S' in row][0]
    
    for route in routes:
        di, step = route.split()
        step = int(step)
        
        # 벗어나는지 확인
        next_x, next_y = x + move[di][0] * step, y + move[di][1] * step
        if not ((0 <= next_x <= h) and (0 <= next_y <= w)):
            continue
            
        # 가는길 장애물 확인
        for i in range(1, step + 1):
            next_x, next_y = x + move[di][0] * i, y + move[di][1] * i
            if park[next_x][next_y] == "X":
                break
        else: # 없으면 현재위치 업데이트
            x, y = next_x, next_y
            
    return [x, y]