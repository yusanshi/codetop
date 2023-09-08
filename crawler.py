import requests
import math
import json

from time import sleep
from tqdm import tqdm


def page_url(i=1):
    return f'https://codetop.cc/api/questions/?page={i}&search=&ordering=-frequency'


r = requests.get(page_url())
count = r.json()['count']
page_num = math.ceil(count / 20)
data = []

level_map = {1: 'easy', 2: 'medium', 3: 'hard'}


def get_url(url):
    if url is None:
        return None
    if url.startswith('http://') or url.startswith('https://'):
        return url
    return f"https://leetcode.cn/problems/{url}/"


for i in tqdm(range(1, page_num + 1)):
    r = requests.get(page_url(i))
    data.extend([{
        'leetcode_id': x['leetcode']['frontend_question_id'],
        'title': x['leetcode']['title'],
        'url': get_url(x['leetcode']['slug_title']),
        'level': level_map[x['leetcode']['level']],
        'frequency': x['value'],
    } for x in r.json()['list']])

    sleep(1)

assert len(data) == count
data = [{'id': i + 1, **x} for i, x in enumerate(data)]

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
