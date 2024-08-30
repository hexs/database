import json
import os
import psutil
from git import Repo

with open('config.json') as f:
    config = json.loads(f.read())


def pull():
    repo = Repo(config['Directory'])
    pull = repo.git.pull('origin', 'main')
    print(pull)


def if_status_change_add_commit_push():
    repo = Repo(config['Directory'])
    status = repo.git.status()
    print('status', status, '- -' * 30, sep='\n')
    if status.split('\n')[-1] != 'nothing to commit, working tree clean':
        add = repo.git.add('.')
        print('add', add, '- -' * 30, sep='\n')
        for v in status.split('\n'):
            if '	modified:   ' in v:
                print(v.split('	modified:   ')[-1])
                break
        else:
            v = ''
        commit = repo.git.commit('-am', f'auto update {v.strip()}')
        print('commit', commit, '- -' * 30, sep='\n')

        try:
            push = repo.git.push('origin', 'main')
            print('push', push, '- -' * 30, sep='\n')

        # if Authentication failed key หมดอายุ
        except Exception as e:
            if 'fatal: Authentication failed for' in str(e):
                users = psutil.users()
                user_name = (users[0].name)
                with open(rf'C:\Users\{user_name}\Documents\git_config.json') as f:
                    git_config = json.loads(f.read())
                new_url = f"https://zxjq:{git_config['tokens']}@github.com/hexs/PD_Attendance.git"

                # remote remote origin
                try:
                    repo.git.remote('remove', 'origin')
                except:
                    pass

                # remote add origin
                repo.git.remote('add', 'origin', new_url)

                push = repo.git.push('origin', 'main')
                print('push', push, '- -' * 30, sep='\n')


if __name__ == '__main__':
    if_status_change_add_commit_push()
