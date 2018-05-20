# Usage:
# python prepopulate.py /path/to/sample/data/file.jsonl

import os
import sys
import requests


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def make_request(batch):
    url = 'http://localhost:5000/player-session-service/player-events/'
    payload = '[{}]'.format(','.join(batch))
    print(payload)
    headers = {'Content-Type': 'application/json'}
    res = requests.post(url, data=payload, headers=headers)
    print(res)


filename = sys.argv[1]
if os.path.exists(filename):
    with open(os.path.basename(filename), "r") as file:
        batch = []
        i = 0
        batches = 0
        for line in file:
            batch.append(line.rstrip('\n'))
            i += 1
            if i == 10:
                i = 0
                batches += 1
                make_request(batch)
                batch = []
            if batches > 1000:
                break

else:
    print("Could not find sample data file..")
