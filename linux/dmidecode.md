# dmidecode
Результат выполнения команды dmidecode — записи из таблицы DMI в следующем формате
```
Record Header: Handle {record id}, DMI type {dmi type id}, {record size} bytes  
Record Value: {multi line record value}
```
* *record id* — уникальный идентификатор записи;
* *dmi type id* — тип записи (например MEMORY, BIOS);
* *record size* — размер записи в DMI таблице;
* *multi line record values* — значение записи (самое интересное).
## Пример использования:  

>dmidecode | head -15
```
# dmidecode 2.12
SMBIOS 3.0 present.
# SMBIOS implementations newer than version 2.8 are not
# fully supported by this version of dmidecode.
125 structures occupying 5129 bytes.
Table at 0x000EC9B0.

Handle 0x0000, DMI type 0, 24 bytes
BIOS Information
	Vendor: American Megatrends Inc.
	Version: 2.0
	Release Date: 12/17/2015
	Address: 0xF0000
	Runtime Size: 64 kB
	ROM Size: 8192 kB
```   
>dmidecode -t 1  
```
dmidecode -t 1
# dmidecode 3.2
Getting SMBIOS data from sysfs.
SMBIOS 2.3 present.

Handle 0x0001, DMI type 1, 25 bytes
System Information
        Manufacturer: Microsoft Corporation
        Product Name: Virtual Machine
        Version: 7.0
        Serial Number: 8160-5269-8566-1468-8419-0699-98
        UUID: 320f8664-b4a3-3448-887f-b2b565849aec
        Wake-up Type: Power Switch

```
>dmidecode -t [Type information]  
```
Type    Information
----------------------------------------
    0    BIOS
    1    System
    2    Base Board
    3    Chassis
    4    Processor
    5    Memory Controller
    6    Memory Module
    7    Cache
    8    Port Connector
    9    System Slots
    10   On Board Devices
    11   OEM Strings
    12   System Configuration Options
    13   BIOS Language
    14   Group Associations
    15   System Event Log
    16   Physical Memory Array
    17   Memory Device
    18   32-bit Memory Error
    19   Memory Array Mapped Address
    20   Memory Device Mapped Address
    21   Built-in Pointing Device
    22   Portable Battery
    23   System Reset
    24   Hardware Security
    25   System Power Controls
    26   Voltage Probe
    27   Cooling Device
    28   Temperature Probe
    29   Electrical Current Probe
    30   Out-of-band Remote Access
    31   Boot Integrity Services
    32   System Boot
    33   64-bit Memory Error
    34   Management Device
    35   Management Device Component
    36   Management Device Threshold Data
    37   Memory Channel
    38   IPMI Device
    39   Power Supply
    40   Additional Information
    41   Onboard Devices Extended Information
    42   Management Controller Host Interface
```
# lshw
