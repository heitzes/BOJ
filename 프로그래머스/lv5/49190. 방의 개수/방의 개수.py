from collections import defaultdict
                
def solution(arrows):
    answer = 0
    x, y = 0, 0
    direction = {0: [0, 1], 1: [1, 1], 2: [1, 0], 3: [1, -1], 
                4: [0, -1], 5: [-1, -1], 6: [-1, 0], 7: [-1, 1]}
    visited_node = set()
    visited_node.add(frozenset([(0,0)]))
    visited_line = set()
    cross = [1,3,5,7]
    for arr in arrows:
        X, Y = x + direction[arr][0], y + direction[arr][1]
        line = frozenset([(x, y), (X, Y)])
        
        if arr in cross:
            if arr == 1 or arr == 7:
                if frozenset([(x, y + 1), (X, Y - 1)]) in visited_line and line not in visited_line:
                    answer += 1
            else:
                if frozenset([(x, y - 1), (X, Y + 1)]) in visited_line and line not in visited_line:
                    answer += 1 
        if frozenset([(X, Y)]) not in visited_node:
            visited_node.add(frozenset([(X, Y)]))
            visited_line.add(line)
        else:
            if line not in visited_line:
                visited_line.add(line)
                answer += 1
        x, y = X, Y
    
    return answer
