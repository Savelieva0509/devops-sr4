# Команди для демонстрації — Самостійна 4

Усе виконується у VM Ubuntu Server 26.04 (з Windows: `ssh -p 2222 liudmyla@127.0.0.1`).

```bash
cd ~/devops-sr4 && source .venv/bin/activate
```

## Частина 1. Linux-утиліти

### 1. journalctl
```bash
sudo journalctl -n 10 --no-pager                                  # 10 останніх записів
sudo journalctl -u ssh.service --since today --no-pager | tail -n 5   # лише sshd
wc -l part1/logs.txt                                              # вивід збережено у файл
```

### 2. IOPS (iostat) — пояснення в part1/iops.md
```bash
iostat -d sda                                                     # tps = IOPS
dd if=/dev/zero of=~/iotest bs=4k count=3000 oflag=dsync status=none & iostat -dy sda 1 3; wait; rm -f ~/iotest
```

### 3. Диски — fdisk vs parted у part1/disks.md
```bash
lsblk -e7 -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS
sudo fdisk -l /dev/sda
sudo parted /dev/sda print
```

### 4. systemd — part1/mytest.service, роль WorkingDirectory у part1/systemd.md
```bash
systemctl status mytest.service --no-pager
journalctl -u mytest.service -n 3 --no-pager
tail -n 3 /tmp/test.log
```

## Частина 2. Python-пакети

### 1. Пакет (pyproject.toml, src/hello_babenko/)
```bash
python -m build && ls dist
```

### 2. Локальний PyPI: devpi + twine
```bash
nohup devpi-server --host 127.0.0.1 --port 3141 > ~/devpi.log 2>&1 &
sleep 10; devpi use http://localhost:3141/liudmyla/dev
twine upload --repository-url http://localhost:3141/liudmyla/dev/ -u liudmyla dist/*   # пароль вводиться
devpi list hello-babenko
rm -rf /tmp/testenv && python3 -m venv /tmp/testenv
/tmp/testenv/bin/pip install -q -i http://localhost:3141/liudmyla/dev/+simple/ hello-babenko
/tmp/testenv/bin/hello-babenko DevOps                             # Привіт, DevOps!
```

### 3. .deb vs .rpm — part2/deb-vs-rpm.md
```bash
cd /tmp && apt-get download tree && ar t tree_*.deb; cd ~/devops-sr4
```

### 4. CHANGELOG — CHANGELOG.md, навіщо — part2/changelog.md

## Додатково: molotov (loadtest/)
```bash
python loadtest/server.py & sleep 2
curl -s -i http://127.0.0.1:8080/
molotov -w 5 -d 10 -x loadtest/loadtest.py                       # SUCCESSES: … | FAILURES: 0
kill %%
```

## Git
```bash
git log --oneline
```
