from collections import defaultdict
def solution(genres, plays):
    answer = []
    gen_played = defaultdict(int)
    song_played = defaultdict(list)
    for ind, gen in enumerate(genres):
        gen_played[gen] += plays[ind]
        song_played[gen].append([plays[ind], ind])
    gen_list = sorted(gen_played.items(), key=lambda x: -x[1])
    for gen, _ in gen_list:
        song_list = sorted(song_played[gen], key=lambda x: (-x[0], x[1]))
        answer.extend([i[1] for i in song_list[:2]])
    return answer