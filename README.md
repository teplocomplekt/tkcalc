
# Калькулятор Теплокомплект

## Сборка:

Есть проблемы что .exe файлы запакованные при помощи pyinstaller
иногда дают ложно-положительное срабатывание антивирусов.
Антивирусы не блокируют приложение, если версии:
python==3.10
pyinstaller==4.10


### windows

* Установить `python3.10.exe` (кажется работает для версий 3.8 - 3.11)
* `pip install -r requirements.txt`(кажется работает и для pyinstaller>=5.10)
* `build.bat`

Готовая программа будет лежать в `./dist/`

### linux

Также можно собрать проект в .exe в докер-контейнере.

основано на контейнере **batonogov/docker-pyinstaller**

[https://gitlab.com/batonogov/docker-pyinstaller](https://gitlab.com/batonogov/docker-pyinstaller)

Запустить `build.sh`

Готовая программа будет лежать в `./dist/`
