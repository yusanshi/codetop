import json

with open('data.json') as f:
    data = json.load(f)

for x in data:
    if x['url'] == 'https://leetcode.cn/problems/coin-change-2/':
        x['url'] = 'https://leetcode.cn/problems/coin-change-ii/'

with open('data.json', 'w') as f:
    json.dump(data, f, indent=4, ensure_ascii=False)
