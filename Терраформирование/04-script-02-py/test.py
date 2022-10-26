#!/usr/bin/env python3

dir="~/PycharmProjects/devops-homework"

import os

#bash_command = ["cd ~/PycharmProjects/devops-homework", "git status"]
dir=os.path.expanduser(dir)
bash_command = ["cd "+dir, "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
#is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(os.path.abspath(prepare_result))
        break
    if result.find('new file') != -1:
        prepare_result = result.replace('\tnew file:   ', '')
        print(os.path.abspath(prepare_result))
        break
else:
    print("Nothing changed.")

