<h2>Установка файлов</h2>
Создайте папку проекта
<br>

Через терминал перейдите в папку проекта
```
 cd <путь_к_папке_с_проектом>
```

Создайте виртуальную среду
```
 python3 -m venv <название_вашей_виртуальной_среды>
```

Запустите виртуальную среду
<be>
Закиньте в папку проекта файлы из архива или клонируйте репозиторий в вашу папку
<br>
Установите зависимости, находясь в папке с проектом
```
 pip install -r requirements.txt
```
В config.py запишите токен вашго бота, который вы получили у BotFather
<br><br>
Запустите main.py
<br>
<h2>Функционал бота</h2>
<ul>
  <li>Отправка поздравления от бота в Новый год</li>
  <li>Игра в монетку</li>
  <li>Отправка поздравлений друзьям, запустившим бота и имеющим @username</li>
  <li>Просмотр пользователей, кому были отправлены поздравления</li>
  <li>Удаление отправленных поздравлений</li>
</ul>
