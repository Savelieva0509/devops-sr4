# Завдання 2.3. Відмінності пакетів .deb і .rpm

| | .deb | .rpm |
|---|---|---|
| 1. Дистрибутиви | Debian, Ubuntu, Linux Mint | Red Hat (RHEL), Fedora, CentOS/Rocky, openSUSE |
| 2. Інструменти | низький рівень dpkg, високий — apt | низький рівень rpm, високий — dnf/yum (zypper в openSUSE) |
| 3. Будова файлу | ar-архів із трьох частин: debian-binary, control.tar (опис, залежності, скрипти), data.tar (самі файли) | один бінарний файл: заголовок (опис, залежності, підписи) + cpio-архів із файлами |

Ще відмінності:
- Як збирають: для .deb — папка debian/ (control, rules, changelog) і dpkg-buildpackage;
  для .rpm — один файл .spec і rpmbuild.
- Назва файлу: name_version-revision_arch.deb (amd64) проти name-version-release.arch.rpm (x86_64).

Перевірка на Ubuntu: apt-get download tree → ar t tree_*.deb показує debian-binary, control.tar.*, data.tar.*.

Висновок: обидва формати виконують одну роль — доставляють програму з описом і залежностями, —
але несумісні між собою: .deb ставиться через dpkg/apt, .rpm — через rpm/dnf (конвертувати можна утилітою alien).
