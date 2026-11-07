# Завдання 2.2. Локальний PyPI на devpi

Версії: devpi-server 6.21.0, devpi-client 7.3.0, twine 7.0.0.

## Запуск сервера

    devpi-init                                             # один раз: створює ~/.devpi/server і користувача root
    nohup devpi-server --host 127.0.0.1 --port 3141 > ~/devpi.log 2>&1 &
    devpi use http://localhost:3141

## Користувач та індекс

    devpi user -c liudmyla password=<пароль>
    devpi login liudmyla --password=<пароль>
    devpi index -c dev bases=root/pypi                     # власний індекс поверх звичайного PyPI
    devpi use liudmyla/dev

## Завантаження пакета через twine

    python -m build
    twine upload --repository-url http://localhost:3141/liudmyla/dev/ -u liudmyla -p <пароль> dist/*
    devpi list hello-babenko                               # на сервері .whl і .tar.gz

## Встановлення з локального PyPI (у чистому venv)

    python3 -m venv /tmp/testenv
    /tmp/testenv/bin/pip install -i http://localhost:3141/liudmyla/dev/+simple/ hello-babenko
    /tmp/testenv/bin/python -c "import hello_babenko as h; print(h.hello('Людмила'), h.__version__)"
    # Привіт, Людмила! 0.1.0
    /tmp/testenv/bin/hello-babenko DevOps
    # Привіт, DevOps!
