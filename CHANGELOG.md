# Changelog

Усі помітні зміни пакета hello-babenko. Формат — Keep a Changelog, версії — Semantic Versioning.

## [0.1.0] - 2026-11-07

### Added
- Функція `hello(name)` — повертає привітання «Привіт, {name}!».
- Консольна команда `hello-babenko [ім'я]`.
- `pyproject.toml` (setuptools), збирання `python -m build` у wheel і sdist.
- Публікація в локальний PyPI devpi (індекс `liudmyla/dev`) через twine.
- README з описом і командою встановлення.

### Fixed
- Артефакти збирання (`dist/`, `build/`, `*.egg-info`) і `.venv` виключені з git через `.gitignore`.

### Security
- Завантажувати пакети в індекс `liudmyla/dev` може лише користувач `liudmyla` (`acl_upload`).
- devpi-server слухає тільки `127.0.0.1` — недоступний ззовні.
- Пароль devpi не зберігається в репозиторії (у документації — `<пароль>`).
