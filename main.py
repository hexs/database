import random
import time
from manage_json_files import json_load, json_update
from update_git import if_status_change_add_commit_push

while True:
    json_update('database/id1.json', {
        "id": 1,
        "mc_name": "1x01",
        "fixed_move": "fixed",
        "res": [
            random.randint(0, 1000),
            random.randint(0, 1000),
            random.randint(0, 1000),
            random.randint(0, 1000),
            random.randint(0, 1000),
            random.randint(0, 1000)
        ],
        "status": "ok",
        "status_detail": "....",
    })

    json_update('database/id2.json', {
        "id": 2,
        "mc_name": "2x01",
        "fixed_move": "fixed",
        "res": [
            random.randint(0, 1000),
            random.randint(0, 1000),
            random.randint(0, 1000),
            random.randint(0, 1000),
            random.randint(0, 1000),
            random.randint(0, 1000)
        ],
        "status": "ok",
        "status_detail": "....",
    })

    if_status_change_add_commit_push()
    time.sleep(10)
