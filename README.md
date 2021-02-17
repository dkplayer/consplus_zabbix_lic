# Скрипты для подсчета занятых лицензий интранет версии Консультант+ 

Были написаны, чтобы отслеживать использование лицензий с помощью мониторинга сервера в Zabbix.

Процедура установки:
1. установить zabbix агент на сервер интранет версии Консультант+
2. установить python
3. положить скрипты в папку агента Zabbix
4. Создать пользовательские скрипты в конфигурации агента

UserParameter=cons_lic[*],C:\Python\Python38\python.exe "C:\Zabbix\plugins\check_cons_lic.py"

UserParameter=cons_lic_ltd[*],C:\Python\Python38\python.exe "C:\Zabbix\plugins\opensessions.py" $1

6. Добавить хост и элементы в панели мониторинга Zabbix
