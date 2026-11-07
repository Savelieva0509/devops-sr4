# hello-babenko

Навчальний Python-пакет із самостійної роботи №4 з DevOps: функція `hello(name)` повертає привітання, а команда `hello-babenko` друкує його в терміналі.
Пакет збирається через `python -m build` і публікується в локальний PyPI (devpi).

Встановлення з локального PyPI:

    pip install -i http://localhost:3141/liudmyla/dev/+simple/ hello-babenko

Перевірка: `python -c "from hello_babenko import hello; print(hello('Людмила'))"`.

Папка `part1/` — Частина 1 роботи (journalctl, iostat, lsblk, systemd).
