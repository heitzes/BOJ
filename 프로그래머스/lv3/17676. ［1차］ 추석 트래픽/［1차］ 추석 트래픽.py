def solution(lines):
    answer = 0
    timeline = []
    start_tl = []
    end_tl = []
    for line in lines:
        date, time, cost = line.split()
        hour, minute, sec = time.split(':')
        cost = float(cost[:-1]) * 1000
        end_time = int((3600 * int(hour) + 60 * int(minute) + float(sec)) * 1000)
        start_time = end_time - int(cost) + 1
        start_tl.append(start_time)
        end_tl.append(end_time)
        timeline.append([start_time, end_time])
    timeline = sorted(timeline, key = lambda x: (x[1]))
    start_tl = sorted(start_tl)
    end_tl = sorted(end_tl)
    s, e = 0, 0
    ans = 0
    max_ans = 0
    while s < len(timeline) and e < len(timeline):
        if start_tl[s] < end_tl[e] + 1000:
            ans += 1
            max_ans = max(ans, max_ans)
            s += 1
        else:
            e += 1
            ans -= 1
    # #print(timeline)
    # while e < len(timeline):
    #     #print("=============================")
    #     #print("s: {} e: {}".format(s, e))
    #     #print(timeline[s][1], timeline[e][0])
    #     if timeline[e][0] < timeline[s][1] + 1000:
    #         ans += 1
    #         max_ans = max(e-s+1, max_ans)
    #         #print("s: {} new e: {} ans: {}".format(s, e, ans))
    #     else:
    #         s += 1
    #         #print("new s: {} new s: {}".format(s, e))
    #     e += 1
    return max_ans