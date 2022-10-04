Домашнее задание к занятию "3.7. Компьютерные сети, лекция 2"
===
1. Проверьте список доступных сетевых интерфейсов на вашем компьютере. Какие команды есть для этого в Linux и в Windows?
---

		$ ip -c -br link
		lo               UNKNOWN        00:00:00:00:00:00 <LOOPBACK,UP,LOWER_UP> 
		eth0             UP             08:00:27:73:60:cf <BROADCAST,MULTICAST,UP,LOWER_UP> 

 В Windows есть команда **ipconfig**

2. Какой протокол используется для распознавания соседа по сетевому интерфейсу? Какой пакет и команды есть в Linux для этого?
---

Используется протокол *lldp* (пакет *lldpd*)

3. Какая технология используется для разделения L2 коммутатора на несколько виртуальных сетей? Какой пакет и команды есть в Linux для этого? Приведите пример конфига.
---

Используется концепция [VLAN](https://en.wikipedia.org/wiki/Virtual_LAN) (пакет *vlan*).
Пример конфигурации:

		$ sudo vconfig add eth0 2
[ИЛИ](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/sec-configure_802_1q_vlan_tagging_using_the_command_line)

		$ sudo ip link add link eth0 name eth0.4 type vlan id 4 

		$ sudo ip addr add 192.168.1.4/24 dev eth0.4
		$ sudo ip link set eth0.4 up


4. Какие типы агрегации интерфейсов есть в Linux? Какие опции есть для балансировки нагрузки? Приведите пример конфига.
---

В Linux существуют методы аггрегации интерфейсов [*teaming* и *bonding*](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_networking/configuring-network-bonding_configuring-and-managing-networking).
 Пример конфигурации 802.1ad *bonding*:

		# ip link add bond0 type bond
		# ip link set bond0 type bond mode 802.3ad
		# ip link set em1 down
		# ip link set em1 master bond0
		# ip link set em2 down
		# ip link set em2 master bond0
		# ip link set bond0 up

5. Сколько IP адресов в сети с маской /29 ? Сколько /29 подсетей можно получить из сети с маской /24. Приведите несколько примеров /29 подсетей внутри сети 10.10.10.0/24.
---

В сети с префиксом /29 2^(32-29) = 2^3 = 8 адресов.
В сети с префиксом /24 2^(32-24) = 2^8 адресов или 2^(8-3) = 2^5 = 32 подсети с префиксом /29.
Примеры подсетей /29: 10.0.10.0/29, 10.0.10.8/29, 10.0.10.16/29..

6. Задача: вас попросили организовать стык между 2-мя организациями. Диапазоны 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16 уже заняты. Из какой подсети допустимо взять частные IP адреса? Маску выберите из расчета максимум 40-50 хостов внутри подсети.
---

Так как по условию задачи адресное пространство, определенное [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918.html) использовать нельзя и адресное пространство предполагается использовать в непубличной сети, можно обратиться к [RFC 6598](https://www.rfc-editor.org/rfc/rfc6598.html) и из адресного пространства, выделенного для организации Carrier-Grade NAT, использовать блок необходимого размера для размещения  40-50 хостов: потребуется блок не менее 64 адреса или 2^6, например, 100.64.0.0/26.  
 Существует периодически обновляемый список адресов специального назначения: [RFC 6890](https://www.rfc-editor.org/rfc/inline-errata/rfc6890.html).

7. Как проверить ARP таблицу в Linux, Windows? Как очистить ARP кеш полностью? Как из ARP таблицы удалить только один нужный IP?
---

Linux:
 - посмотреть всю таблицу: 	**ip neighbour show**
 - удалить всю таблицу:		**sudo ip neighbour flush dev <IF>**
 - удалить конкретный IP:	**sudo ip neighbour delete <IP> lladdr <MAC> dev <IF>**


Windows: 
 - посмотреть всю таблицу: 	**arp -a**
 - удалить всю таблицу:		**arp -d**
 - удалить конкретный IP:	**arp -d <IP>**
