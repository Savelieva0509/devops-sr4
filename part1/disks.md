# Завдання 3. Структура дисків

## lsblk
```
NAME                       SIZE TYPE FSTYPE      MOUNTPOINTS
sda                         20G disk             
├─sda1                       1M part             
├─sda2                     1.8G part ext4        /boot
└─sda3                    18.2G part LVM2_member 
  └─ubuntu--vg-ubuntu--lv   10G lvm  ext4        /
sr0                       1024M rom              
```

## fdisk -l /dev/sda
```
Disk /dev/sda: 20 GiB, 21474836480 bytes, 41943040 sectors
Disk model: VBOX HARDDISK   
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: gpt
Disk identifier: 38B4E714-B04E-42E3-8080-AE6E5356908D

Device       Start      End  Sectors  Size Type
/dev/sda1     2048     4095     2048    1M BIOS boot
/dev/sda2     4096  3719167  3715072  1.8G Linux filesystem
/dev/sda3  3719168 41940991 38221824 18.2G Linux filesystem
```

## parted /dev/sda print
```
Model: ATA VBOX HARDDISK (scsi)
Disk /dev/sda: 21.5GB
Sector size (logical/physical): 512B/512B
Partition Table: gpt
Disk Flags: 

Number  Start   End     Size    File system  Name  Flags
 1      1049kB  2097kB  1049kB                     bios_grub
 2      2097kB  1904MB  1902MB  ext4
 3      1904MB  21.5GB  19.6GB

```

## Що бачимо

- sda (20 ГБ, розмітка GPT): sda1 — 1 МБ для завантажувача GRUB (bios_grub),
  sda2 — 1,8 ГБ ext4 під /boot, sda3 — 18,2 ГБ під LVM, у ньому логічний том 10 ГБ ext4 під / (система).
- sr0 — віртуальний CD-привід.

## Обмеження fdisk у порівнянні з parted

1. Не вміє змінювати розмір розділу. У fdisk немає такої команди — розділ можна лише видалити й створити заново.
   У parted є resizepart.
2. Тільки інтерактивний режим (діалог із запитаннями) — незручно для скриптів і автоматизації.
   parted працює однією командою: parted -s /dev/sda mkpart ... (для fdisk у скриптах потрібен окремий sfdisk).
3. Одиниці — лише сектори. parted дозволяє задавати розміри в MB, GB, % і сам вирівнює розділи.
4. Старі версії fdisk працювали лише з MBR (msdos): до 4 основних розділів і диски до 2 ТБ.
   parted від початку підтримує GPT (сучасний fdisk з util-linux уже теж уміє GPT).

Важлива різниця в безпеці: fdisk тримає зміни в пам'яті й записує лише після команди w (можна вийти без збереження),
а parted застосовує кожну зміну одразу.
