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