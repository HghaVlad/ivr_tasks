## STEP 1

<p><strong>Советы при написании</strong></p>

<p>Мы изучили некоторые базовые навыки(за исключением моделей), теперь у вас есть все для написания некоторых небольших, но уже что-то выполняющих проектов. Давайте вспомним, что нам необходимо делать и в каком порядке, чтобы создать правильно функционирующее приложение.</p>

<ol>
	<li>Установить Django и создать проект(<code>startproject</code>). После чего создаем приложение.</li>
	<li>Меняем файл settings.py, добавляем в настройки наше приложение</li>
	<li>Создаем файл urls.py в нашем приложении и настраиваем urls.py в директории самого проекта</li>
	<li>Пишем представления</li>
	<li>Создаем файлы шаблонов в папке templates</li>
	<li>Связываем url c представлениями</li>
	<li>Запускаем наш проект</li>
	<li>Тестируем и проверяем на баги</li>
</ol>

<p>Конечно, все эти шаги субъективны и вы можете их выполнять в разном порядке. Но этот список вам поможет ничего не забыть. В начале возможно будут какие-то трудности, даже на самом первом этапе. Но это не повод сдаваться, будьте готовы гуглить что-то и не бойтесь обращаться к создателям курса или таким же как вы ученикам в комментариях курса.</p>

## STEP 2

<p><strong>Онлайн редактор</strong></p>

<p>Когда вы впервые запустите свой рабочий проект, вы получите ссылку по которой можно обратиться к вашему приложению. Но данная ссылка работает только локально. Но что если вы хотите похвастаться перед другом или знакомыми?</p>

<p>Думаю, многие знаю, что существуют онлайн компиляторы кодов, например <code>onlinegdb.com</code> Такие редакторы позволяют запускать код, но они очень ограничены встроенным в языки функционалом. </p>

<p>Но помимо этого существуют редакторы, которые могут запускать ваш проект в сеть. Один из таких replit.com. Его бесплатный функционал позволяет запускать небольшие приложения на время. <br>
После чего ваш сайт будет доступен по определенной ссылке.</p>

<p>Для чего же это вам сейчас? Чуть позже вы узнаете о способах проверки практических заданий. Одним из них является автоматическая проверка, которая требует только ссылку на рабочий сайт. Вместо того, чтобы самостоятельно деплоить проект на сервере, вам предлагается воспользоваться этим сайтом(или другим).</p>

<p>Инструкция по запуску проекта:</p>

<li>Откройте главную страницу <a href="https://replit.com/" rel="noopener noreferrer nofollow">https://replit.com/</a> Возможно вам потребуется перед этим авторизоваться

<p style="text-align: center;"><img alt="" name="image.png" src="https://ucarecdn.com/959bbde1-2e4e-4bce-a390-058a6c20d07b/" ></p>
</li>
<li>Справа вверху нажмите на плюсик. В поиске шаблонов напишите <code>Django</code> Нажмите Create Repl<br>
 
<p style="text-align: center;"><img alt="" name="image.png" src="https://ucarecdn.com/c1dfecca-9e80-47cc-ad9d-fa38ec1553d1/"></p>
</li>
<li>Подождав некоторое время у вас появятся все файлы. Первое что вам надо сделать это изменить <strong>SECRET_KEY</strong> в настройках проекта<br>
 
<p style="text-align: center;"><img alt="" name="Снимок экрана 2023-03-07 в 21.39.34.png" src="https://ucarecdn.com/b5e67eec-bf7e-4f99-8eb6-1c59155b6c1f/"></p>
</li>
<li>После чего вы можете нажать RUN. Ваш проект запуститься. Получить ссылку вы можете в окошке браузера.<br>
 
<p style="text-align: center;"><img alt="" name="Снимок экрана 2023-03-07 в 21.42.06.png" src="https://ucarecdn.com/6c5556bc-e831-4e45-b188-1f3f71c04d34/" ></p>
</li>
<li>Вы можете менять файлы или писать прямо на сайте</li>