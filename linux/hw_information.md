# dmidecode
Вывод информации об оборудовании на низком уровне  
Результат выполнения команды dmidecode — записи из таблицы DMI в следующем формате
```
Record Header: Handle {record id}, DMI type {dmi type id}, {record size} bytes  
Record Value: {multi line record value}
```
* *record id* — уникальный идентификатор записи;
* *dmi type id* — тип записи (например MEMORY, BIOS);
* *record size* — размер записи в DMI таблице;
* *multi line record values* — значение записи (самое интересное).
### Пример использования:  

> dmidecode | head -15
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
> dmidecode -t 1  
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
> dmidecode [-t ($Type | $Information)]
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
Вывод информации об оборудовании в human-readable формате  
Примерная структура общего вывода  
```
system information
   motherboard information
     cpu information
	cache, logical cpu
     memory
	capacity, total size, individual bank information
     pci slot information
     ide slot information
	disk information
		total size, partition,
     usb slot information
    network
```
### Пример использования:  
> lshw | head -n 15
```
lshw | head -n 15
webserver1.com
    description: Computer
    product: KVM
    vendor: Red Hat
    version: RHEL 7.5.0 PC (i440FX + PIIX, 1996)
    width: 64 bits
    capabilities: smbios-2.8 dmi-2.8 smp vsyscall32
    configuration: boot=normal family=Red Hat Enterprise Linux uuid=0F88B4EF-B0D8-8343-81FE-7A72726BE280
  *-core
       description: Motherboard
       physical id: 0
     *-firmware
          description: BIOS
          vendor: SeaBIOS
          physical id: 0
```
> lshw -C disk
```
  *-virtio1
       description: Virtual I/O device
       physical id: 0
       bus info: virtio@1
       logical name: /dev/vda
       size: 80GiB (85GB)
       capabilities: partitioned partitioned:dos
       configuration: driver=virtio_blk logicalsectorsize=512 sectorsize=512 signature=0009c288
```
> lshw [-class|C ($classname)] [-short] 
```
Classnames
------------------------------------------------
address, bridge, bus, communication, disk, display, generic, input, memory, multimedia, network, power, printer, processor, storage, system, tape
```