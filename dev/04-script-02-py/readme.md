Домашнее задание к занятию "4.2. Использование Python для решения типовых DevOps задач"
===

1.  Есть скрипт:
---
```python
		#!/usr/bin/env python3
		a = 1
		b = '2'
		c = a + b
```

Какое значение будет присвоено переменной c?

```python
		c = a + b
		TypeError: unsupported operand type(s) for +: 'int' and 'str'
		Операция сложения не поддерживает операнды разного типа.  
```

Как получить для переменной c значение 12?  

```python
		c = str(a) + b
```

Как получить для переменной c значение 3?  

```python
		c = a + int(b)
```

2. Доработать скрипт, чтобы в выводе были все измененные файлы, а так же полный путь к каталогу, где они находятся.
---
Исходный скрипт:
```python
		#!/usr/bin/env python3
		
		import os
		
		bash_command = ["cd ~/netology/sysadm-homeworks", "git status"]
		result_os = os.popen(' && '.join(bash_command)).read()
		is_change = False
		for result in result_os.split('\n'):
		    if result.find('modified') != -1:
		        prepare_result = result.replace('\tmodified:   ', '')
		        print(prepare_result)
		        break
```
Доработанный скрипт:
```python
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
```
3. Доработать скрипт выше так, чтобы он мог проверять не только локальный репозиторий в текущей директории, а также умел воспринимать путь к репозиторию, который мы передаём как входной параметр. Мы точно знаем, что начальство коварное и будет проверять работу этого скрипта в директориях, которые не являются локальными репозиториями.
---
```python
		#!/usr/bin/env python3

		import os, sys

		if len(sys.argv) < 2:
		    print("Usage:",sys.argv[0],"<repodir>")
		    sys.exit(1)
		if not os.path.exists(sys.argv[1]+'/.git'):
		    print(sys.argv[1], "not a git repository.")
		    sys.exit(2)
		dir=os.path.expanduser(sys.argv[1])
		bash_command = ["cd "+dir, "git status"]
		result_os = os.popen(' && '.join(bash_command)).read()
		#print(dir)
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
```
4. Мы хотим написать скрипт, который опрашивает веб-сервисы, получает их IP, выводит информацию в стандартный вывод в виде: <URL сервиса> - <его IP>. Также, должна быть реализована возможность проверки текущего IP сервиса c его IP из предыдущей проверки. Если проверка будет провалена - оповестить об этом в стандартный вывод сообщением: [ERROR] <URL сервиса> IP mismatch: <старый IP> <Новый IP>. Будем считать, что наша разработка реализовала сервисы: drive.google.com, mail.google.com, google.com.
---
```python
		#!/usr/bin/env python3

		hosts=['drive.google.com', 'mail.google.com', 'google.com', 'localhost.localdomain.']

		import socket

		prev_ips={}
		while True:
		    for host in hosts:
		        # resolv DNS
		        try:
		            junk1, junk2, ips=socket.gethostbyname_ex(host)
		        except :
		            print("Can not resolve", host)
		            continue
			# if set of IPs NEQ previous set
		        if host in prev_ips and set(ips) != set(prev_ips[host]):
		            print("[ERROR]", host," IP mismatch:", prev_ips, ips)
		        for ip in ips:
		            try:
		                #https://docs.python.org/3/howto/sockets.html
		                s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		                s.connect((ip,80))
		                print(host, ip, "OK")
		                s.close()
		            except : # Can't connect()
		                print("[ERROR]",host,ip,"FAIL")
		        prev_ips[host]=ips
```
