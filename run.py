import os
import random
import math
from argparse import ArgumentParser
from typing import List

import pandas as pd


def split_group(samples: List, size: int) -> List[List]:
    random.shuffle(samples)
    return [samples[i::size] for i in range(size)]


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-s', '--seed', type=int, default=None)
    parser.add_argument('-m', '--members', nargs='*')
    parser.add_argument('-n', '--group_num', type=int, default=3)
    print(os.environ['Comment'])
    inputs = os.environ['Comment'].replace('team generator', '').split()
    args = parser.parse_args(inputs)

    if args.seed is not None:
        random.seed(args.seed)

    if args.members is None:
        members = [
           "김수영", "김원호", "김유리",
           "류나현", "신규용", "이다운",
           "임승재", "정다운", "정승재",
           "정지수", 'Max', "Xingdong",
        ]
    else:
        members = args.members

    group_num = args.group_num
    team_size = math.ceil(len(members) / group_num)

    df = pd.DataFrame(columns=[' '] * team_size)
    for group_idx, group in enumerate(split_group(members, group_num)):
        group = group + [' '] * (team_size - len(group))
        df.loc[len(df)] = group
    df.index.name = 'Team'

    comment_body = open('comment-body.md', 'w')
    print(df.to_markdown(comment_body, tablefmt='github'))
