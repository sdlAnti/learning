# iotop  
Утилита позволяющая узнать, кто использует диск и как сильно
```
Total DISK READ:         0.00 B/s | Total DISK WRITE:         0.00 B/s
Current DISK READ:       0.00 B/s | Current DISK WRITE:       0.00 B/s
    TID  PRIO  USER     DISK READ  DISK WRITE  SWAPIN     IO>    COMMAND
      1 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % init auto noprompt
      2 be/4 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [kthreadd]
      3 be/0 root        0.00 B/s    0.00 B/s  0.00 %  0.00 % [rcu_gp]
```
| Заголовок  | Описание                                                                                                                |
| :--------: | :---------------------------------------------------------------------------------------------------------------------- |
|    TID     | thread ID                                                                                                               |
|    PRIO    | класс приоритета у процесса, приоритет процесса по операциям ввода-вывода (I/O). Как и NI, управляется командой ionice. |
|    USER    | пользователь, от имени которого запущен процесс                                                                         |
| DISK READ  | запрашиваемые процессом данные на чтение.                                                                               |
| DISK WRITE | запрашиваемые процессом данные на запись.                                                                               |
|   SWAPIN   | количество данных, отправляемых в swap.                                                                                 |
|    IO>     | ожидание I/O процессом.                                                                                                 |
|  COMMAND   | команда, работающая в процессе                                                                                          |

# iftop  
Утилита для монитринга нагрзки сетевых устройств
>iftop -i eth1

-n – не преобразовывать IP адреса в имена хостов;  
-P – отображать порт  
-N – не преобразовывать № порта в имя сервиса  
-B – отображать график в байтах/сек, а не битах/сек  
```
$ sudo iftop
interface: ens33
IP address is: 192.168.124.157
MAC address is: 00:0c:29:25:aa:67
 Display paused               12.5Kb               25.0Kb                         37.5Kb                50.0Kb                   62.5Kb
└─────────────────────────────┴────────────────────┴──────────────────────────────┴─────────────────────┴──────────────────────────────
ubuntu                                                => 192.168.124.1                                          1.59Kb  1.12Kb   853b
                                                      <=                                                        1.16Kb   570b    262b
192.168.124.255                                       => 192.168.124.1                                             0b      0b      0b
                                                      <=                                                           0b      0b     14b
```
## Пример использования
> Вывести весь трафик интерфейсе eth0:
```
iftop -i eth0
```
> Трафик между локальным интерфейсом и хостом 8.8.8.8/портом 22/http/icmp
```
iftop -i eth0 -f “dst 8.8.8.8”
iftop -i eth0 -f “dst port 22″
iftop -i eth0 -f “dst port http”
iftop -i eth0 -f “icmp”
```
# vmstat  

```
$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0  21096 308308 127624 2311604    0    0     1     6   14   14  0  0 100  0  0

```
### Procs
r – количество процессов в очереди на выполнение процессором (если значение > 0 – налицо нагрузка на процессор);  
b – количество процессов, ожидающих операций I/O (если значение > 0 – налицо нагрузка на диски и/или файловую систему).  
### Memory
swpd – количество блоков, перемещённых в swap;  
free – свободная память (без учёта памяти, занятой буферам и кэшом);  
buff – буферы памяти;  
cache – кеш;  
### Swap
si (swap in) – количество блоков в секунду, которое система считывает из раздела или файла swap в память;  
so (swap out) – и наоборот, количество блоков в секунду, которое система перемещает из памяти в swap.
> Чем ближе к 0 тем лучше  
### IO
bi (blocks in) – количество блоков в секунду, считанных с диска;  
bo (blocks out) – количество блоков в секунду, записанных на диск;
### System
in (interrupts) – количество прерываний в секунду;  
cs (context switches) – количество переключений между задачами;
### CPU
us (user time) – % времени CPU, занятый на выполнение “пользовательских” (не принадлежащих ядру) задач;  
sy (system time) – % времени CPU, занятый на выполнение задач ядра (сеть, I/O задачи, прерывания и т.п.);  
id (idle) – % времени в бездействии (ожидании задач);  
wa – % времени CPU, занятый на ожидание операций I/O;  
st - время, украденное из виртуальной машины.

# lsof
>LiSt Open Files  
```
$ sudo lsof | head
lsof: WARNING: can't stat() fuse.gvfsd-fuse file system /run/user/1000/gvfs
      Output information may be incomplete.
COMMAND      PID    TID TASKCMD               USER   FD      TYPE             DEVICE SIZE/OFF       NODE NAME
systemd        1                              root  cwd       DIR                8,5     4096          2 /
systemd        1                              root  rtd       DIR                8,5     4096          2 /
systemd        1                              root  txt       REG                8,5  1620224     169091 /usr/lib/systemd/systemd
```
| Заголовок | Описание                                                                                                            |
| :-------: | :------------------------------------------------------------------------------------------------------------------ |
|  COMMAND  | команда, запущенная в процессе. Указывается без параметров запуска, но по PID можно найти через htop                |
|    PID    | идентификатор процесса                                                                                              |
|    TID    | идентификатор треда. В рамках одного процесса может быть запущенно несколько тредов                                 |
|  TASKCMD  | присутствует только в тредах, так как в рамках каждого треда может быть запущена другая команда                     |
|   USER    | пользователь, от имени которого запущен процесс/тред                                                                |
|           |                                                                                                                     |
|    FD     | файловый дескриптор. Записывает файлопроцесса:                                                                      |
|    cwd    | текущая рабочая директория процесса (зависит от того, где запущен процесс)                                          |
|    txt    | текстовый файл (хотя на самом деле, может быть и бинарный файл, который запускается)                                |
|    mem    | файл с отображенной памятью (по факту - загруженные в память данные представленные для программы в псевдофайлы)     |
|           |                                                                                                                     |
|   TYPE    | тип файла:                                                                                                          |
|    REG    | обычный файл в системе                                                                                              |
|    DIR    | директория в каталоге                                                                                               |
|   FIFO    | устройство типа pipe ( в pipe скриптах)                                                                             |
| IPv(4/6)  | сетевое подключение по протоколу IP версии 4 или 6 соответственно                                                   |
|   unix    | сетевой сокет (как правило, используется именно при подключении к сокетам)                                          |
|   sock    | открываемый сокет для подключения со стороны внешнего мира (об этом мы будем рассказывать в более поздних заданиях) |
|  a_inode  | anonymous inodes - по факту, временные файлы, которые не должны в конце работы оставаться в системе                 |
## Пример использования
> Перечислить все процессы, которые открыли файл

```
lsof path_to_file
```
> Cписка файлов откртых конкретным пользователем/всеми кроме   

```
lsof -u sd--anti
```  
```
lsof -u ^sd--anti
```
> Список всех файлов, открытых командой
```
lsof -c process_name
```
> Какие файлы открыты в дирректории и ее поддиректориях
```
lsof +d /usr/bin
```
> Файлы открытые процессом
```
lsof -p PID
```
> Найти открытый пользователем и командой или процессом  
> -a позволяет комбинировать условия по принципу логического "И" (без -a работает по принципу "ИЛИ")
```
lsof -a -u user_name -c command_name
```
> Cетевые соединения и порты
```
lsof -i
```
# atop
Позволяет смотреть историческое состояние системы, записывает состояние о каждом процессе, информацию о использовании диска/сети/процессора/системы.  

```
ATOP - fast                    2022/03/30  12:27:09                    -----------------                    5d0h18m24s elapsed
PRC | sys    2h24m | user   7h58m | #proc    177 | #trun      1 |  #tslpi   344 | #tslpu     0 | #zombie    0 | #exit      0 |
CPU | sys       4% | user     36% | irq       0% | idle    552% |  wait      1% | steal     7% | guest     0% | curf 2.10GHz |
cpu | sys       1% | user      7% | irq       0% | idle     91% |  cpu004 w  0% | steal     1% | guest     0% | curf 2.10GHz |
cpu | sys       1% | user      7% | irq       0% | idle     91% |  cpu002 w  0% | steal     1% | guest     0% | curf 2.10GHz |
cpu | sys       1% | user      6% | irq       0% | idle     92% |  cpu003 w  0% | steal     1% | guest     0% | curf 2.10GHz |
cpu | sys       1% | user      5% | irq       0% | idle     92% |  cpu001 w  0% | steal     1% | guest     0% | curf 2.10GHz |
cpu | sys       1% | user      6% | irq       0% | idle     92% |  cpu005 w  0% | steal     1% | guest     0% | curf 2.10GHz |
cpu | sys       1% | user      4% | irq       0% | idle     94% |  cpu000 w  0% | steal     1% | guest     0% | curf 2.10GHz |
CPL | avg1    0.44 | avg5    0.51 | avg15   0.60 |              |  csw 397555e3 | intr 40768e4 |              | numcpu     6 |
MEM | tot     5.7G | free  594.1M | cache   1.8G | dirty   7.0M |  buff    0.1M | slab  535.5M | shrss   0.0M | numnode    1 |
SWP | tot     4.0G | free    1.8G | swcac  45.1M |              |               |              | vmcom   5.4G | vmlim   6.8G |
PAG | scan 45678e3 | steal 4262e4 | stall  77885 | compact 9047 |  numamig    0 | migrate 33e5 | swin 1041568 | swout 1458e3 |
DSK |          vda | busy      3% | read 9401792 | write 1163e4 |  KiB/w     18 | MBr/s    0.4 | MBw/s    0.5 | avio 0.61 ms |
NET | transport    | tcpi 19507e3 | tcpo 60282e3 | udpi  352141 |  udpo  356518 | tcpao 264820 | tcppo 583649 | tcprs 626212 |
NET | network      | ipi 20121773 | ipo 19142489 | ipfrw      0 |  deliv 1986e4 |              | icmpi   4312 | icmpo     13 |
NET | eth0    ---- | pcki 18538e3 | pcko 17323e3 | sp    0 Mbps |  si   62 Kbps | so 1453 Kbps | erri       0 | erro       0 |
NET | lo      ---- | pcki 1831960 | pcko 1831960 | sp    0 Mbps |  si  144 Kbps | so  144 Kbps | erri       0 | erro       0 |
NET | docker0 ---- | pcki       1 | pcko       3 | sp    0 Mbps |  si    0 Kbps | so    0 Kbps | erri       0 | erro       0 |
                      *** System and Process Activity since Boot ***     Unrestricted view (privileged)
  PID SYSCPU  USRCPU  RDELAY   VGROW   RGROW   RDDSK   WRDSK  RUID     EUID      ST  EXC   THR  S  CPUNR   CPU  CMD        1/5
 1387 51m49s   2h36m  97m23s    4.7G    2.0G   42.4G  103.6G  mysql    mysql     N-    -    54  S      3    3%  mysqld
13735  6m05s  46m35s   3m03s  599.1M  114.8M    1.1G  670.6M  www-root www-root  N-    -     1  S      1    1%  php-fpm
 2512  6m05s  46m18s   3m02s  601.1M  112.9M    1.3G  566.4M  www-root www-root  N-    -     1  S      1    1%  php-fpm
```
|       |                                                                                                                            |
| :---: | :------------------------------------------------------------------------------------------------------------------------- |
|  PRC  | отображает метрики по процессам - сколько запущенно процессов, сколько процессорного времени используется и другие метрики |
|  CPU  | метрики по использованию процессорного времени.                                                                            |
|  CPL  | нагрузка системы, прерывания, количество ядер                                                                              |
|  MEM  | использование памяти                                                                                                       |
|  SWP  | использование swap                                                                                                         |
|  DSK  | использование дисков (не файловых систем)                                                                                  |
|  NET  | метрики по сетевым устройствам                                                                                             |
  
## Пример использования
> Снимок нагрузки с 04-00 до 0600 (формат YYYYMMDDHHMM)
```
atop -r /var/log/atop/atop_20220330 -b 0400 -e 0600
```
> Нагрузка на память
```
atop -r /var/log/atop/atop_20220330 -b 0400 -e 0600 -m
```
# timedatectl
Утилита для управления временем на сервере
```
# timedatectl
               Local time: Tue 2022-04-05 17:51:03 MSK
           Universal time: Tue 2022-04-05 14:51:03 UTC
                 RTC time: Tue 2022-04-05 14:51:03
                Time zone: Europe/Moscow (MSK, +0300)
System clock synchronized: yes
              NTP service: active
          RTC in local TZ: no

```
## Пример использования
> Получить список доступных часовых поясов
```
# timedatectl list-timezones
```
> Установить часовой пояс
```
timedatectl set-timezone Europe/Moscow
```
> Установыить дату и время
```
timedatectl set-time "2020-04-01 12:00:00"
```
> Выключить NTP 
```
timedatectl set-ntp false
```
> Вывести орпделенную дату
```
date --date='TZ="Europe/Moscow" 00:00 2019-12-01'
```
Можно использовать переменную окружения *TZ* с которой будет работать date - export TZ=":/usr/share/zoneinfo/Europe/Moscow"  
# ifconfig (net-tools) / ip (iproute2)
Инструмент командной строки для диагностика и настрйки сетевых интерфейсов  
[Cheat file](https://access.redhat.com/sites/default/files/attachments/rh_ip_command_cheatsheet_1214_jcs_print.pdf)
| NET-TOOLS COMMANDS                                        | IPROUTE COMMANDS                                     |
| :-------------------------------------------------------- | :--------------------------------------------------- |
| arp -a                                                    | ip neigh                                             |
| arp -v                                                    | ip -s neigh                                          |
| arp -s 192.168.1.1 1:2:3:4:5:6                            | ip neigh add 192.168.1.1 lladdr 1:2:3:4:5:6 dev eth1 |
| arp -i eth1 -d 192.168.1.1                                | ip neigh del 192.168.1.1 dev eth1                    |
| ifconfig -a                                               | ip addr                                              |
| ifconfig eth0 down                                        | ip link set eth0 down                                |
| ifconfig eth0 up                                          | ip link set eth0 up                                  |
| ifconfig eth0 192.168.1.1                                 | ip addr add 192.168.1.1/24 dev eth0                  |
| ifconfig eth0 netmask 255.255.255.0                       | ip addr add 192.168.1.1/24 dev eth0                  |
| ifconfig eth0 mtu 9000                                    | ip link set eth0 mtu 9000                            |
| ifconfig eth0:0 192.168.1.2                               | ip addr add 192.168.1.2/24 dev eth0                  |
| netstat                                                   | ss                                                   |
| netstat -neopa                                            | ss -neopa                                            |
| netstat -g                                                | ip maddr                                             |
| route                                                     | ip route                                             |
| route add -net 192.168.1.0 netmask 255.255.255.0 dev eth0 | ip route add 192.168.1.0/24 dev eth0                 |
| route add default gw 192.168.1.1                          | ip route add default via 192.168.1.1                 |
## Пример использования
> Получение базовой информации по интерфейсам
```
ip addr
```
> Получение базовой информации по определенному интерфейсу
```
ip addr show rbr0
```
> Задать основной ip интерфейса
```
ifconfig eth0 192.168.1.1
```
> Задать маску подсети
```
ifconfig eth0 netmask 255.255.255.0  
```
> Добавить дополнительный IPv4-адрес на основной интерфейс из той же подсети.
```
ifconfig eth0:0 192.168.124.190
```
> Создать интерфейс с именем dum0 и типом dummy
```
ip link add dum0 type dummy
```
> Включить интерфейс dum0
```
ip link set dum0 up
```
> Задать основной Ip интерфейса
```
ip addr add 192.168.1.20/24 dev dum0
```
> Задать MTU для интерфейса
```
ip link set dum0 mtu 1462
```
# netstat
Утилита, показывающая базовую статистику по всем сетевым операциям и отображающая информацию о том, какие порты и адреса используются для сетевых подключений как входящих, так и исходящих.
```
$ netstat -ta
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State
tcp        0      0 0.0.0.0:http            0.0.0.0:*               LISTEN
tcp        0      0 localhost:domain        0.0.0.0:*               LISTEN
tcp        0      0 0.0.0.0:ssh             0.0.0.0:*               LISTEN
tcp        0      0 localhost:ipp           0.0.0.0:*               LISTEN
tcp        0      0 localhost:6010          0.0.0.0:*               LISTEN
tcp        0     48 ubuntu:ssh              192.168.124.1:64873     ESTABLISHED
tcp6       0      0 [::]:9100               [::]:*                  LISTEN
tcp6       0      0 [::]:http               [::]:*                  LISTEN
tcp6       0      0 [::]:ssh                [::]:*                  LISTEN
tcp6       0      0 ip6-localhost:ipp       [::]:*                  LISTEN
tcp6       0      0 ip6-localhost:6010      [::]:*                  LISTEN
```
* -t | --tcp: TCP сокеты
* -u | --udp: UDP сокеты
* -a | --all: Показать все сокеты
* -l | --listening: Показывать только сокеты, которые слушают
* -n | --numeric: Отображение цифрового адреса вместо разрешения имени хоста
* -c | --continuous: Непрерывный вывод информации 
* -g | --gropus: Показать информацию о членстве в многоадресной группе IGMP для IPv4 и IPv6
## Пример использования

> Показать все прослушивающие TCP-порты;
```
netstat -tl
```
> Получить список всех сетевых соединений и связанных с ними программ.
```
netstat -ap
```
> Перечислить все TCP порты.
```
netstat -at
```
> Перечислить все UDP порты.
```
netstat -au
```
> Показать все прослушивающие TCP и UDP порты с выводом номера процесса и IP-адреса (не имени).
```
$ netstat -tulpn
```
> Показать все прослушивающие UNIX-сокеты.
```
$ netstat -lx
```

# ss
Утилита, показывающая базовую статистику по всем сетевым операциям и отображающая информацию о том, какие порты и адреса используются для сетевых подключений как входящих, так и исходящих., **более бытрая и удобная чем netstat**
```
$ ss -ta
State       Recv-Q      Send-Q             Local Address:Port              Peer Address:Port       Process
LISTEN      0           511                      0.0.0.0:http                   0.0.0.0:*
LISTEN      0           4096               127.0.0.53%lo:domain                 0.0.0.0:*
LISTEN      0           128                      0.0.0.0:ssh                    0.0.0.0:*
LISTEN      0           5                      127.0.0.1:ipp                    0.0.0.0:*
LISTEN      0           128                    127.0.0.1:6010                   0.0.0.0:*
ESTAB       0           48               192.168.124.157:ssh              192.168.124.1:64873
LISTEN      0           4096                           *:9100                         *:*
LISTEN      0           511                         [::]:http                      [::]:*
LISTEN      0           128                         [::]:ssh                       [::]:*
LISTEN      0           5                          [::1]:ipp                       [::]:*
LISTEN      0           128                        [::1]:6010                      [::]:*
```
## Пример использования
> Получить список сокетов в режиме прогслушивания сети
```
ss -l
```
> Получить все TCP сокеты (в том числе и ожидающие подключений -a)
```
ss -t -a
```
> Показать все TCP-соединения, где порт источника или получателя - 22, без имени, только с IP;
```
ss -atn '( dport = :22 or sport = :22 )
```
> Показать все соединения для IPv4 со всеми возможными статусами, за исключением статусов listen и closed;
```
ss -4a state connected
```
> Показать все прослушивающие TCP и UDP порты с выводом номера процесса и IP-адреса (не имени);
```
ss -tulnp
```
# iptables
Файрвол, брандмауэр или межсетевой экран  
```
iptables -L
Chain INPUT (policy ACCEPT)
target     prot opt source               destination

Chain FORWARD (policy DROP)
target     prot opt source               destination
DOCKER-USER  all  --  anywhere             anywhere
DOCKER-ISOLATION-STAGE-1  all  --  anywhere             anywhere
ACCEPT     all  --  anywhere             anywhere             ctstate RELATED,ESTABLISHED
DOCKER     all  --  anywhere             anywhere
ACCEPT     all  --  anywhere             anywhere
ACCEPT     all  --  anywhere             anywhere

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination
```
[## Примеры использования](https://www.digitalocean.com/community/tutorials/iptables-essentials-common-firewall-rules-and-commands)
> получить список текущих правил с нумерацией
```
iptables -L --line-numbers
```
> Разрешить уже установленныe и связанныe входящие соединения  
```
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
```
**-A INPUT** — эта часть команды, которая сообщает iptables, что мы хотим добавить новое правило в конец цепочки INPUT.  
**-m conntrack** — iptables имеет набор основных функциональных возможностей, но также имеет набор расширений или модулей, которые предоставляют дополнительные возможности. И в этой части команды мы говорим, что хотим иметь доступ к функциональности, предоставляемой модулем conntrack. Этот модуль предоставляет доступ к командам, которые могут использоваться для принятия решений на основе отношения пакета к предыдущим соединениям.  
**–ctstate** — это одна из команд, доступных при вызове модуля conntrack, которая позволяет нам сопоставлять пакеты в зависимости от того, как они связаны с пакетами, которые мы видели ранее. Мы передаем ему значение ESTABLISHED, чтобы разрешить пакеты, являющиеся частью существующего соединения. А также передаем значение RELATED, чтобы разрешить пакеты, которые связаны с установленным соединением.  
**-j ACCEPT** — указывает цель сопоставления пакетов, то есть тут мы говорим, что пакеты, которые соответствуют предыдущим критериям, должны быть приняты и пропущены.

> Разрешить подключения на 22 порт
```
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
```
> Разрешить подключения на 22 порт с определенного источника 
```
iptables -A INPUT -p tcp -s 203.0.113.0/24 --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
```
**-p tcp** — эта опция указывает на пакеты TCP-протокола.  
**–dport** — данная опция доступна только, если задана предыдущая -p tcp, и указывает на то, что TCP-пакет должен соответствовать порту назначения, в нашем случае - 22 порт.

> Разрешить все пакеты на сетевом интерфейсе lo (если пакет использует интерфейс lo, то любой пакет использующий lo должен быть разрешен )
```
iptables -I INPUT 1 -i lo -j ACCEPT
```
-I INPUT 1 — правило необходимо вставить в цепочку INPUT, первой строкой.
-i lo — укзывает интерфейс
> Изменить политику по уполчанию (`Chain INPUT (policy ACCEPT)`) на DROP
```
iptables -P INPUT DROP
```
> Добавить запрещающее правило
Как правило добавляется в конец цепочки после разрешающих, если политика по умолчанию - ACCEPT
```
iptables -A INPUT -j DROP
```
> Заблокировать сетевые подключения с 203.0.113.51
```
iptables -A INPUT -s 203.0.113.51 -j DROP
```
> Отклонить сетевые подключения с 203.0.113.51
Может использоваться с флагом --reject-with причина отклонения  
- icmp-net-unreachable — сеть недоступна;
- icmp-host-unreachable — узел недоступен;
- icmp-port-unreachable — порт недоступен;
- icmp-proto-unreahable — неподдерживаемый протокол;
- icmp-net-prohibited — сеть запрещена;
- icmp-host-prohibited — узел запрещен;
- tcp-reset - отправляет RST- сообщения отправителю. TCP RST пакеты используются для закрытия TCP соединений.
```
iptables -A INPUT -s 203.0.113.51 -j REJECT
iptables -A INPUT -s 203.0.113.51 -j REJECT --reject-with icmp-port-unreachable
iptables -A INPUT -s 203.0.113.51 -p tcp -j REJECT --reject-with tcp-reset 
iptables -A INPUT -p udp -j REJECT --reject-with icmp-port-unreachable
```
> 
# ufw
По своей сути пакет ufw, является просто надстройкой над iptables, но более прост в управлении и конфигурировании.
```
ufw status verbose
Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), deny (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
80,443/tcp (Nginx Full)    ALLOW IN    Anywhere                   # web server
80,443/tcp (Nginx Full (v6)) ALLOW IN    Anywhere (v6)              # web server
```
## Примеры использования.
> Включение.отключение
```
ufw enable
ufw disable
```
> Сброс правил
```
ufw reset
```
> Политика по умолчанию входящих соединений — запрещено, исходящих - разрешено.
Иначе работает правило как для iptables - "сверху разрешили что нужно, а снизу запретили все"
```
ufw default allow outgoing
ufw default deny incoming
```
> Получить список приложений 
```
ufw app list
Available applications:
  CUPS
  Nginx Full
  Nginx HTTP
  Nginx HTTPS
  OpenSSH
  Postfix
  Postfix SMTPS
```
> Разрешить доступ используя имя приложения с комментарием
```
ufw allow 'Nginx Full' comment 'web server'
```
> Разрешить доступ используя порт и протокол
```
ufw allow 22/tcp
```
> Разрешить все с 9.9.9.9
```
ufw allow from 9.9.9.9
```
> Разрешить все с 9.9.9.9 только на порт 3306
```
ufw allow from 9.9.9.9 to any port 3306
```
> Разрешить доступ только для IP 9.9.9.9, по протоколу tcp на порт 3306, только на входящий интерфейс и его IP-адрес.
```
ufw allow in on ens33 from 9.9.9.9 to 192.168.124.157 port 3306 proto tcp comment MySQL
```
> Разрешить несколько портов tcp
```
ufw allow 15000:15017/tcp
```
> Запретить все подключения с 9.9.9.9
```
ufw deny from 9.9.9.9
```
> Список правил с нумерацией и правлиами по умолчанию
```
ufw status numbered verbose
```
> Удалить правило № 3 или http или 80
```
ufw delete 3
ufw delete allow http
ufw delete allow 80
```
# journalctl
Инструмент для анализа логов поставляемый вместе с systemd
```
$ journalctl
Oct 28 18:56:00 ubuntu kernel: KERNEL supported cpus:
Oct 28 18:56:00 ubuntu kernel:   Intel GenuineIntel
Oct 28 18:56:00 ubuntu kernel:   AMD AuthenticAMD
Oct 28 18:56:00 ubuntu kernel:   Hygon HygonGenuine
Oct 28 18:56:00 ubuntu kernel:   Centaur CentaurHauls
Oct 28 18:56:00 ubuntu kernel:   zhaoxin   Shanghai
Oct 28 18:56:00 ubuntu kernel: x86/fpu: Supporting XSAVE feature 0x001: 'x87 floating point registers'
Oct 28 18:56:00 ubuntu kernel: x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers'
Oct 28 18:56:00 ubuntu kernel: x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers'
Oct 28 18:56:00 ubuntu kernel: x86/fpu: xstate_offset[2]:  576, xstate_sizes[2]:  256
Oct 28 18:56:00 ubuntu kernel: x86/fpu: Enabled xstate features 0x7, context size is 832 bytes, using 'compacted' format.
```
## Примеры использования.  
> Вывести все записи из всех журналов
```
journalctl
```
> Вывести все записи из всех журналов во времени UTC
```
journalctl --utc
```
> Просмотр ошибок по уровню важности
  
Доступны другие уровни важности, *journalctl выведет все сообщения с этим кодом и выше*

0. emergency (неработоспособность системы)
1. alerts (предупреждения, требующие немедленного вмешательства)
2. critical (критическое состояние)
3. errors (ошибки)
4. warning (предупреждения)
5. notice (уведомления)
6. info (информационные сообщения)
7. debug (отладочные сообщения)

```
journalctl -p 2
```
> Просмотр всех журналов загрузки  
```
journalctl --list-boots
```
Для просмотра определенного журнала используется ключ -b и идентификатор журнала из --list-boots
```
journalctl -b 0
```
> Просмотр журнала за определенный период времени  
С определенной даты и времени:
```
journalctl --since "2022-04-26 02:00:00"
```
С определенной даты и по определенное дату и время:
```
journalctl --since "2022-04-26 02:00:00" --until "2022-04-27 05:00:00"
```
Со вчерашнего дня:
```
journalctl --since yesterday
```
С 9 утра и до момента, час назад:
```
journalctl --since 09:00 --until "1 hour ago"
```
> Просмотр сообщений ядра
```
journalctl -k
```
> Просмотр журналов определенного сервиса
```

```