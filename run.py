import random
from typing import List
import math
from argparse import ArgumentParser


def split_group(samples: List, size: int) -> List[List]:
    random.shuffle(samples)
    return [samples[i::size] for i in range(size)]


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-m', '--members', nargs='*')
    parser.add_argument('-t', '--team-size', type=int, default=4)
    args = parser.parse_args()

    comment_body = open('comment-body.md', 'w')
    members = [
       "김수영", "김원호", "김유리",
       "류나현", "신규용", "이다운",
       "임승재", "정다운", "정승재",
       "정지수", 'Max',# "Xingdong"
    ]
    group_num = 3
    team_size = math.ceil(len(members) / group_num)
    comment_body.write('|Team|' + '|'.join([str(i) for i in range(team_size)]) + '|\n')
    comment_body.write('|' + '---|' * (team_size + 1) + '\n')
    for group_idx, group in enumerate(split_group(members, group_num)):
        group = group + [' '] * (team_size - len(group))
        group_str = '|'.join(group)
        comment_body.write(f'|{group_idx:02}|{group_str}|\n')

    comment_body.close()
