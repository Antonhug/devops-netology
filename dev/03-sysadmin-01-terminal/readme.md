Домашнее задание к занятию "3.1. Работа в терминале, лекция 1"
===
4. С помощью базового файла конфигурации запустите Ubuntu 20.04 в VirtualBox посредством Vagrant:
---

    >mkdir vagrant
    >cd vagrant
    >vagrant init
Сгенерированный по умолчанию файл _Vagrantfile_ отсылает за образами в [Vagrant Cloud](https://vagrantcloud.com/search). Ищем там наименование требуемого заданием образа (*bento/ubuntu-20.04*), соответствующим образом редактируем _Vagrantfile_, запускаем 

>vagrant up
    
5.  Ознакомьтесь с графическим интерфейсом VirtualBox, посмотрите как выглядит виртуальная машина, которую создал для вас Vagrant, какие аппаратные ресурсы ей выделены. Какие ресурсы выделены по-умолчанию?
---
  **Vagrant** по-умолчанию создал виртуальную машину с 
 - двумя виртуальными процессорами
 - 1 Гб ОЗУ
 - 64 Гб HDD
 - одним сетевым интерфейсом, подключенным к публичной сети, с редиректом 127:0.0.1:2222 на порт 22 интерфейса виртуальной машины
 - пользователем vagrant/vagrant с аутентификацией по открытому ключу. Открытый ключ уже находился в файле *~/.ssh/authorized_keys* виртуальной машины, закрытый ключ нашелся в файле *.vagrant\machines\default\virtualbox\private_key* хоста.

6. Как добавить оперативной памяти или ресурсов процессора виртуальной машине?
---
Согласно [документации](https://www.vagrantup.com/docs/providers/virtualbox/configuration), следующие строки в _Vagrantfile_ добавляют ОЗУ и виртуальных процессоров виртуальной машине:

    config.vm.provider "virtualbox" do |v|
      v.memory = 1024
      v.cpus = 2
    end

8. Ознакомиться с разделами man bash, почитать о настройках самого bash:
---
 - Какой переменной можно задать длину журнала history, и на какой строчке manual это описывается?
    >HISTSIZE
    >The number of commands to remember in the command history (see HISTORY below). The default value is 500
    **bash(1)**, line 1178
 - Что делает директива ignoreboth в bash?
    эта директива предотвращает попадание в список *history* команд, начинающихся с пробелов (видимо, любых разделителей) и дублей команд, уже сохраненных в списке ранее:
    >HISTCONTROL
    >A colon-separated list of values controlling how commands are saved on the history list. If the list of values includes *ignorespace*, lines which begin with a space character are not saved in the history list. A value of *ignoredups* causes lines matching the previous history entry to not be saved. A value of *ignoreboth* is shorthand for *ignorespace* and *ignoredups*.

9. В каких сценариях использования применимы скобки {} и на какой строчке man bash это описано?
---
 Применение *{}* описано в разделе *Brace Expansion* **bash(1)**, line 1508:
 
>Brace expansion is a mechanism by which arbitrary strings may be gener
>ated. Patterns to be brace expanded take the
>form of an optional preamble, followed by either a series of commasep‐
>arated strings or a sequence expression between a pair of braces,  fol‐
>lowed  by  an  optional  postscript.   The preamble is prefixed to each
>string contained within the braces, and the postscript is then appended
>to each resulting string, expanding left to right.
  [..]
> A  sequence expression takes the form {x..y[..incr]}, where x and y are
>either integers or single characters, and incr, an optional  increment,
>is  an  integer.  When integers are supplied, the expression expands to
>each number between x and y, inclusive.
    
  Скобки применяются для генерации составных выражений из *преамбулы*+*переменной части*+*заключения*, причем *"переменные части"* как раз и представлены в виде спиcка через запятую, заключенного между фигурными скобками. Например, команда
  
        ls /{,usr}/{,s}bin
        
выведет содержимое каталогов /bin, /sbin, /usr/bin, /usr/sbin.

10. Основываясь на предыдущем вопросе, как создать однократным вызовом touch 100000 файлов? А получилось ли создать 300000? Если нет, то почему?
---
        $touch {1..100000}; echo $?
        0

Успешно.

        $ touch {1..300000}; echo $?
        -bash: /usr/bin/touch: Argument list too long
        126

Неуспешно. [StackOverflow](https://stackoverflow.com/questions/11289551/argument-list-too-long-error-for-rm-cp-mv-commands) подсказывает, что неуспех связан с превышением максимальной длины массива символов ARG_MAX, предназначенным для хранения аргументов программы, запускаемой на выполнение посредством системного вызова [execve(2)](http://manpages.ubuntu.com/manpages/bionic/man2/execve.2.html):

>Most UNIX implementations impose some limit on the total size of the command-line argument
> (argv) and environment (envp) strings that may be passed to a new program.  POSIX.1 allows
> an  implementation  to  advertise this limit using the ARG_MAX constant
    
11. В man bash поищите по */\[\[*. Что делает конструкция *[[ -d /tmp ]]* ?
---
Двойные прямые скобки обрамляют условное выражение, **bash(1)** line 359:

>[[ expression ]]
>           Return a status of 0 or 1 depending on  the  evaluation  of  the
>           conditional  expression expression.  Expressions are composed of
>           the primaries described  below  under  CONDITIONAL  EXPRESSIONS.

Выражение *[[ -d /tmp ]]* проверяет на существование каталог */tmp*

12. Добейтесь в выводе *type -a bash* в виртуальной машине наличия первым пунктом в списке **bash is /tmp/new_path_directory/bash**
---
Исходное состояние:
        
        $type -a bash
         bash is /usr/bin/bash
         bash is /bin/bash

Команды:

        $mkdir /tmp/new_path_directory
        $ln -s /usr/bin/bash /tmp/new_path_directory/bash
        $export PATH="/tmp/new_path_directory/:$PATH"
        
Результат:

        $ type -a bash
         bash is /tmp/new_path_directory/bash
         bash is /usr/bin/bash
         bash is /bin/bash

13. Чем отличается планирование команд с помощью *batch* и *at*?
---
**at(1)**:

>**at** and **batch** read commands from standard  input  or  a  specified  file
>which are to be executed at a later time, using /bin/sh.
>
>**at**      executes commands at a specified time.
>**batch**   executes commands when system  load  levels  permit;  in  other
>            words,  when  the  load  average  drops below 1.5, or the value
>            specified in the invocation of atd.
   
    Команда **at** посволяет указать время единократного запуска задания, команда **batch** запустит задание при определенном уровне загрузки системы (количестве запущенных процессов и процессов, готовых к запуску или ожидающих ввода/вывода за период времени 1 минута). По умолчанию, **batch** звпустит задание, если загрузка системы будет ниже 1.5
