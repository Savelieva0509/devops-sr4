# Команди для демонстрації — Самостійна 4

Усе виконується у VM Ubuntu Server 26.04 (підключення з Windows: `ssh -p 2222 liudmyla@127.0.0.1`).
**Один блок = одна команда.** Копіюю блок цілком, вставляю, натискаю Enter і чекаю `$`.

---

## 0. Підготовка (до запису відео)

**0.1** Перейти в проєкт і увімкнути venv
```bash
cd ~/devops-sr4 && source .venv/bin/activate
```

**0.2** Запустити локальний PyPI devpi у фоні (стартує ~20 секунд)
```bash
nohup devpi-server --host 127.0.0.1 --port 3141 > ~/devpi.log 2>&1 &
```

**0.3** Через 20 секунд перевірити, що devpi працює (має бути `current devpi index`)
```bash
devpi use http://localhost:3141/liudmyla/dev
```

**0.4** Ввести пароль sudo заздалегідь і очистити екран
```bash
sudo true && clear
```

---

## Частина 1. Linux-утиліти

### 1. journalctl

**1.1** 10 останніх записів системного журналу
```bash
sudo journalctl -n 10 --no-pager
```

**1.2** Лише записи служби sshd (в Ubuntu служба називається ssh.service)
```bash
sudo journalctl -u ssh.service --since today --no-pager | tail -n 5
```

**1.3** Вивід збережено у файл part1/logs.txt
```bash
wc -l part1/logs.txt
```

### 2. IOPS (iostat) — пояснення в part1/iops.md

**2.1** Диск у спокої: колонка tps = IOPS
```bash
iostat -d sda
```

**2.2** Диск під навантаженням дрібними записами по 4 кБ
```bash
dd if=/dev/zero of=~/iotest bs=4k count=3000 oflag=dsync status=none & iostat -dy sda 1 3; wait; rm -f ~/iotest
```

### 3. Диски — порівняння fdisk і parted у part1/disks.md

**3.1** Дерево дисків і розділів
```bash
lsblk -e7 -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS
```

**3.2** Таблиця розділів через fdisk
```bash
sudo fdisk -l /dev/sda
```

**3.3** Та сама таблиця через parted
```bash
sudo parted /dev/sda print
```

### 4. systemd — юніт part1/mytest.service, WorkingDirectory пояснено в part1/systemd.md

**4.1** Стан служби
```bash
systemctl status mytest.service --no-pager
```

**4.2** Журнал служби
```bash
journalctl -u mytest.service -n 3 --no-pager
```

**4.3** Файл, у який служба пише щохвилини
```bash
tail -n 3 /tmp/test.log
```

---

## Частина 2. Python-пакети

### 1. Пакет (pyproject.toml, src/hello_babenko/)

**5.1** Зібрати пакет (wheel + sdist)
```bash
python -m build
```

**5.2** Подивитися зібрані файли
```bash
ls dist
```

### 2. Локальний PyPI: devpi + twine (сервер уже запущено в 0.2)

**6.1** Завантажити пакет через twine (пароль devpi вводиться вручну)
```bash
twine upload --repository-url http://localhost:3141/liudmyla/dev/ -u liudmyla dist/*
```

**6.2** Пакет є на сервері
```bash
devpi list hello-babenko
```

**6.3** Створити чисте віртуальне середовище
```bash
rm -rf /tmp/testenv && python3 -m venv /tmp/testenv
```

**6.4** Встановити пакет з локального PyPI
```bash
/tmp/testenv/bin/pip install -q -i http://localhost:3141/liudmyla/dev/+simple/ hello-babenko
```

**6.5** Перевірити команду пакета (має бути «Привіт, DevOps!»)
```bash
/tmp/testenv/bin/hello-babenko DevOps
```

### 3. .deb vs .rpm — порівняння в part2/deb-vs-rpm.md

**7.1** Що всередині .deb-пакета
```bash
cd /tmp && apt-get download tree && ar t tree_*.deb; cd ~/devops-sr4
```

### 4. CHANGELOG — файл CHANGELOG.md, навіщо він — part2/changelog.md

---

## Додатково: molotov (loadtest/)

**8.1** Запустити тестовий сервер у фоні
```bash
python loadtest/server.py &
```

**8.2** Ручна перевірка: код 200 і JSON
```bash
curl -s -i http://127.0.0.1:8080/
```

**8.3** Навантажувальний тест: 5 воркерів, 10 секунд (має бути FAILURES: 0)
```bash
molotov -w 5 -d 10 -x loadtest/loadtest.py
```

**8.4** Зупинити тестовий сервер
```bash
kill %%
```

---

## Git

**9.1** Історія комітів
```bash
git log --oneline
```
