from bisect import bisect_right
def solution(n, t, m, timetable):
    answer = ''
    new_timetable = []
    for time in timetable:
        hour, minute = map(int, time.split(':'))
        new_timetable.append(60*hour + minute)
    new_timetable.sort()
    start = 60 * 9
    bus_timetable = []
    for i in range(n):
        bus_timetable.append(start + t * i)
    inbus = [0]
    for bus in bus_timetable:
        available = bisect_right(new_timetable, bus)-sum(inbus)
        if available > m:
            inbus.append(m)
        else:
            inbus.append(available)
    #print(bus_timetable)
    #print(new_timetable)
    #print(inbus)
    def toString(hm):
        h, m = hm // 60, hm % 60
        if h < 10:
            h = '0' + str(h)
        if m < 10:
            m = '0' + str(m)
        return str(h) + ':' + str(m)
    
    if inbus[-1] < m:
        answer = toString(bus_timetable[-1])
    else:
        last = max(new_timetable[sum(inbus[:-1]):sum(inbus[:-1])+inbus[-1]])
        corn = last - 1
        answer = toString(corn)

    return answer