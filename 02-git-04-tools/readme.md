Домашнее задание к занятию «2.4. Инструменты Git»
===
Подготовительная работа.
---
		$mkdir 02-git-04-tools
		$cd 02-git-04-tools
		$git clone git@github.com:hashicorp/terraform.git
		$echo "terraform/" > .gitignore
		$cd terraform
Выполнение задания.
---
1. Найдите полный хеш и комментарий коммита, хеш которого начинается на *aefea*.
		
		$ git show -s aefea 
		commit aefead2207ef7e2aa5dc81a34aedf0cad4c32545
		Author: Alisdair McDiarmid <alisdair@users.noreply.github.com>
		Date:   Thu Jun 18 10:29:58 2020 -0400
		
		    Update CHANGELOG.md

2. Какому тегу соответствует коммит *85024d3*?

		$ git show -s --oneline 85024d3
		85024d310 (tag: v0.12.23) v0.12.23

3. Сколько родителей у коммита *b8d720*? Напишите их хеши.

 - Переберем всех предков коммита:

		$ git show -s  b8d720^1
		commit 56cd7859e05c36c06b56d013b55a252d0bb7e158
		Merge: 58dcac4b7 ffbcf5581
		Author: Chris Griggs <cgriggs@hashicorp.com>
		Date:   Mon Jan 13 13:19:09 2020 -0800
		
		    Merge pull request #23857 from hashicorp/cgriggs01-stable
		    
		    [cherry-pick]add checkpoint links
		$ git show -s  b8d720^2
		commit 9ea88f22fc6269854151c571162c5bcf958bee2b
		Author: Chris Griggs <cgriggs@hashicorp.com>
		Date:   Tue Jan 21 17:08:06 2020 -0800
		
		    add/update community provider listings
		$ git show -s  b8d720^3
		fatal: ambiguous argument 'b8d720^3': unknown revision or path not in the working tree.
- ИЛИ воспользуемся указанием всех предков коммита из gitrevisions(7):

		$ git show -s  b8d720^@
		commit 56cd7859e05c36c06b56d013b55a252d0bb7e158
		Merge: 58dcac4b7 ffbcf5581
		Author: Chris Griggs <cgriggs@hashicorp.com>
		Date:   Mon Jan 13 13:19:09 2020 -0800
		
		    Merge pull request #23857 from hashicorp/cgriggs01-stable
		    
		    [cherry-pick]add checkpoint links
		
		commit 9ea88f22fc6269854151c571162c5bcf958bee2b
		Author: Chris Griggs <cgriggs@hashicorp.com>
		Date:   Tue Jan 21 17:08:06 2020 -0800
		
		    add/update community provider listings

4. Перечислите хеши и комментарии всех коммитов которые были сделаны между тегами *v0.12.23* и *v0.12.24*.

		$ git show -s --oneline v0.12.23..v0.12.24
		33ff1c03b (tag: v0.12.24) v0.12.24
		b14b74c49 [Website] vmc provider links
		3f235065b Update CHANGELOG.md
		6ae64e247 registry: Fix panic when server is unreachable
		5c619ca1b website: Remove links to the getting started guide's old location
		06275647e Update CHANGELOG.md
		d5f9411f5 command: Fix bug when using terraform login on Windows
		4b6d06cc5 Update CHANGELOG.md
		dd01a3507 Update CHANGELOG.md
		225466bc3 Cleanup after v0.12.23 release

5. Найдите коммит в котором была создана функция *func providerSource*, ее определение в коде выглядит так: _func providerSource(...)_ (вместо троеточего перечислены аргументы).

		$ git log -S"func providerSource(" --pretty=short
		commit 8c928e83589d90a031f811fae52a81be7153e82f
		Author: Martin Atkins <mart@degeneration.co.uk>
		
		    main: Consult local directories as potential mirrors of providers
		$ git show --pretty=short  8c928e83589d90a031f811fae52a81be7153e82f
		commit 8c928e83589d90a031f811fae52a81be7153e82f
		Author: Martin Atkins <mart@degeneration.co.uk>
		
		    main: Consult local directories as potential mirrors of providers
		[..]
		diff --git a/provider_source.go b/provider_source.go
		new file mode 100644
		index 000000000..9524e0985
		--- /dev/null
		+++ b/provider_source.go
		[..]
		+func providerSource(services *disco.Disco) getproviders.Source {

6. Найдите все коммиты в которых была изменена функция *globalPluginDirs*.

		$ git grep "func globalPluginDirs"
		plugins.go:func globalPluginDirs() []string {
		$ git log -s --oneline -L :globalPluginDirs:plugins.goi
		78b122055 Remove config.go and update things using its aliases
		52dbf9483 keep .terraform.d/plugins for discovery
		41ab0aef7 Add missing OS_ARCH dir to global plugin paths
		66ebff90c move some more plugin search path logic to command
		8364383c3 Push plugin discovery down into command package

7.Кто автор функции *synchronizedWriters*?

		$ git log --pretty=short -p -S"func synchronizedWriters("
		commit bdfea50cc85161dea41be0fe3381fd98731ff786
		Author: James Bardin <j.bardin@gmail.com>
		
		    remove unused
		[..]
		--- a/synchronized_writers.go
		+++ /dev/null
		[..]
		-func synchronizedWriters(targets ...io.Writer) []io.Writer {
		[..]

		commit 5ac311e2a91e381e2f52234668b49ba670aa0fe5
		Author: Martin Atkins <mart@degeneration.co.uk>
		
		    main: synchronize writes to VT100-faker on Windows
		[..]
		--- /dev/null
		+++ b/synchronized_writers.go
		[..]
		+func synchronizedWriters(targets ...io.Writer) []io.Writer {
		[..]

 Судя по содержимому diff, автором функции *synchronizedWriters* был Martin Atkins, а James Bardin - ее убийцей.
