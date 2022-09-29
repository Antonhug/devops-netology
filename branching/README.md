Домашнее задание к занятию «2.3. Ветвления в Git»
===
Подготовка к выполнению задания
---
- Создаем каталоги и два файла _merge.sh_ и _rebase.sh_ идентичного содержания:

		$mkdir -p 02-git-03-branching/branching

		$cat << EOF > 02-git-03-branching/branching/merge.sh
		 #!/bin/bash
		 # display command line options
		
		 count=1
		 for param in "$*"; do
		     echo "\$* Parameter #$count = $param"
		     count=$(( $count + 1 ))
		 done
		 EOF

		$ cp 02-git-03-branching/branching/merge.sh 02-git-03-branching/branching/rebase.sh

- Сделаем предварительный коммит в ветку *main*:

		$ git status
		On branch main
		
		Untracked files:
		  (use "git add <file>..." to include in what will be committed)
		        02-git-03-branching/
		
		$git add .
		$git commit -m 'prepare for merge and rebase'
		$git status
		On branch main
		nothing to commit, working tree clean

Подготовка файла *merge.sh*
---
- Создадим ветку *git-merge*:

		$ git branch
		* main
		  master
		$ git switch -c git-merge
		Switched to a new branch 'git-merge'

- Заменим содержимое файла _merge.sh_ на

		$cat << EOF > 02-git-03-branching/branching/merge.sh
		#!/bin/bash
		# display command line options
		
		count=1
		for param in "$@"; do
		    echo "\$@ Parameter #$count = $param"
		    count=$(( $count + 1 ))
		done
		EOF

- Сделаем коммит и отправим изменения в репозиторий:

		$ git add .
		$ git commit -m 'merge: @ instead *'
		$ git push -u origin git-merge
		Enumerating objects: 34, done.
		Counting objects: 100% (34/34), done.
		Delta compression using up to 16 threads
		Compressing objects: 100% (20/20), done.
		Writing objects: 100% (24/24), 4.46 KiB | 198.00 KiB/s, done.
		Total 24 (delta 7), reused 0 (delta 0)
		remote: Resolving deltas: 100% (7/7), completed with 4 local objects.
		remote:
		remote: Create a pull request for 'git-merge' on GitHub by visiting:
		remote:      https://github.com/vladimir-chernyshev/devops-homework/pull/new/git-merge
		remote:
		To github.com:vladimir-chernyshev/devops-homework.git
		 * [new branch]      git-merge -> git-merge
		Branch 'git-merge' set up to track remote branch 'git-merge' from 'origin'.

- Внесем еще одно изменение в _merge.sh_:

		$cat << EOF > 02-git-03-branching/branching/merge.sh
		#!/bin/bash
		# display command line options
		
		count=1
		while [[ -n "$1" ]]; do
		    echo "Parameter #$count = $1"
		    count=$(( $count + 1 ))
		    shift
		done
		EOF

- Сделаем коммит и отправим изменения в репозиторий:

                $ git commit -a -m 'merge: use shift'
                $ git push 
