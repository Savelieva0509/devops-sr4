# Завдання 4. systemd-сервіс mytest.service

Файли: part1/mytest.service (юніт), part1/mytest.sh (скрипт).
Встановлення: скрипт → /opt/mytest/mytest.sh, юніт → /etc/systemd/system/mytest.service,
далі sudo systemctl daemon-reload && sudo systemctl enable --now mytest.service.

Як працює: Type=simple, скрипт у нескінченному циклі раз на 60 секунд дописує рядок у /tmp/test.log
і дублює його у stdout — тому той самий рядок видно в journalctl -u mytest.service.

## Роль WorkingDirectory=

WorkingDirectory= задає робочу (поточну) папку процесу служби — аналог команди cd перед запуском.
За замовчуванням systemd запускає службу з кореня /, тож без цього параметра:
- ExecStart=/bin/bash mytest.sh не знайшов би скрипт (bash шукав би /mytest.sh);
- будь-які відносні шляхи у скрипті (файли конфігурації, логи) рахувалися б від /.

У нашому юніті WorkingDirectory=/opt/mytest, тому:
- скрипт викликається коротким іменем mytest.sh;
- $(pwd) у кожному рядку логу показує /opt/mytest — це доказ, що параметр діє.

## Перевірка

- systemctl status mytest.service → active (running), enabled; у CGroup процеси bash mytest.sh і sleep 60.
- journalctl -u mytest.service → рядки щохвилини.
- cat /tmp/test.log → ті самі рядки з інтервалом 1 хвилина.
