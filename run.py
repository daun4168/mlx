import random
from typing import List
from argparse import ArgumentParser


def split_group(samples: List, size: int):
    p = len(samples)
    for _ in range(0, len(samples), size):
        for _ in range(size):
            i = random.randrange(p)
            p -= 1
            samples[i], samples[p] = samples[p], samples[i]
        yield samples[p:p + size]


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-m', '--members', nargs='*')
    parser.add_argument('-t', '--team-size', type=int, default=4)
    args = parser.parse_args()

    comment_body = open('comment-body.md', 'w')

    comment_body.write("Members\n")
    members = [
       "김수영", "김원호", "김유리",
       "류나현", "신규용", "이다운",
       "임승재", "정다운", "정승재",
       "정지수", 'Max', "Xingdong"
    ]
    team_size = 4
    for group_idx, group in enumerate(split_group(members, team_size)):
        comment_body.write(f'{group_idx:02} | {group}\n')

    comment_body.close()
