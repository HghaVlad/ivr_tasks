## STEP 1

<p><strong>Файловая система</strong><strong> </strong></p>

<p> </p>

<p>В данном уроке мы изучим:</p>

<ul>
	<li>Где хранятся статические файлы </li>
	<li>Где находятся файлы медиа</li>
	<li>Как загрузить файлы пользователя</li>
</ul>

## STEP 2

<p><strong>Static files</strong></p>

<p>В Django папка <code>static</code> используется для хранения статических файлов, таких как CSS-файлы, JavaScript-файлы, изображения и т.д., которые не изменяются динамически в процессе работы приложения.</p>

<p>При настройке проекта Django, вы можете определить одну или несколько папок для хранения статических файлов. По умолчанию, Django ищет статические файлы в папке <code>static</code> в каждом приложении, которое вы создали. Таким образом, если вы создали приложение <code>blog</code>, то статические файлы для этого приложения должны находиться в папке <code>blog/static/blog</code>.</p>

<p>Если вам нужно определить другую папку для хранения статических файлов, вы можете настроить эту опцию в файле настроек проекта Django <code>settings.py</code>. Например, вы можете добавить следующие строки в <code>settings.py</code>, чтобы указать, что статические файлы должны искаться в папке <code>staticfiles</code> вашего проекта:</p>

<pre><code>STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'staticfiles']</code>
</pre>

<p>Здесь <code>STATIC_URL</code> указывает URL-адрес, по которому статические файлы будут доступны в браузере. По умолчанию, это <code>/static/</code>.</p>

<p><code>STATICFILES_DIRS</code> указывает путь к папке <code>static</code> в вашем Django-проекте. Обычно, путь к этой папке указывается относительно корневой директории проекта. В приведённом выше коде мы использовали <code>os.path.join(BASE_DIR, 'static')</code> для указания абсолютного пути к папке <code>static</code></p>

<p><strong>Использование STATIC в шаблонах</strong></p>

<p>В HTML-шаблонах вашего приложения используйте тег <code>{% static %}</code> для подключения статических файлов. Например, для подключения файла <code>style.css</code> используйте следующий код:</p>

<pre><code>&lt;link rel="stylesheet" type="text/css" href="{% static 'blog/css/style.css' %}"&gt;</code></pre>

<p>Здесь <code>blog</code> - это имя вашего приложения, а <code>css/style.css</code> - это относительный путь к файлу <code>style.css</code> в папке <code>static/blog</code>.</p>

<p>Это позволит Django находить и обслуживать статические файлы в вашем приложении.</p>

<p> </p>

<ol>
</ol>

## STEP 3

<p><strong>Media files</strong></p>

<p>В Django <code>media</code> - это папка, в которой хранятся пользовательские файлы, такие как изображения, аудио и видео. Примерами могут быть загруженные пользователем аватары, фотографии, видео, аудиозаписи и другие файлы.<br>
Отличие между <code>static</code> и <code>media</code> заключается в том, что <code>static</code> содержит файлы, которые не принадлежат ни одному конкретному пользователю, в то время как <code>media</code> содержит файлы, которые принадлежат конкретным пользователям.</p>

<p>Вы можете настроить маршрутизацию для обработки запросов к папкам <code>static</code> и <code>media</code>. Например, вы можете добавить следующие строки в файл <code>urls.py</code> вашего приложения:</p>

<pre><code>from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... ваши URL-шаблоны здесь ...
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)</code></pre>

<p>Эти строки настраивают обработку запросов к папке <code>media</code> во время разработки, чтобы обеспечить правильное отображение пользовательских файлов, которые хранятся в этой папке.</p>

<p>В HTML-шаблонах вашего приложения используйте тег <code>{% url %}</code> для отображения файлов пользователей. Например:</p>

<pre><code>&lt;img src="{{ user.avatar.url }}" alt="User Avatar"&gt;</code></pre>

<p>Здесь <code>user.avatar.url</code> - это URL-адрес, по которому можно получить доступ к файлу изображения. Метод <code>url</code> возвращает URL-адрес, который используется для доступа к файлу.</p>

<p>В Django также есть готовые вьюшки и формы для загрузки файлов пользователей в папку <code>media</code>. Подробнее о них можно узнать в официальной документации Django.</p>

## STEP 4 

<p>В какой папке хранятся файлы пользователей?</p>

- media ✅
- static
- userfiles

## STEP 5

<p>Какой тег используется в шаблонах для обращения к static файлам?</p>

- static

## STEP 6

<p><strong>Загрузка файлов</strong></p>

<p>Иногда нам необходимо, чтобы пользователь загрузил некоторые файлы. Предположим, нам надо принимать какое-то изображение и сохранять его в папку media. Для этого вам потребуется:</p>

<ol>
	<li>В шаблоне HTML-страницы создайте форму, которая будет содержать элемент <code>input</code> типа <code>file</code>. Например:

	<pre><code>&lt;form method="post" enctype="multipart/form-data"&gt;
  {% csrf_token %}
  &lt;input type="file" name="myfile"&gt;
  &lt;button type="submit"&gt;Upload&lt;/button&gt;
&lt;/form&gt;</code></pre>
	Здесь мы создали форму, которая содержит элемент <code>input</code> типа <code>file</code>. Атрибут <code>name</code> указывает имя, которое будет использоваться в Django для доступа к загруженному файлу.<br>
	<code>enctype="multipart/form-data"</code> - это атрибут формы, который указывает, как данные формы должны быть закодированы при их отправке на сервер. Этот атрибут должен использоваться в формах, содержащих элементы <code>&lt;input&gt;</code> типа <code>file</code>.</li>
	<li>В вашем Django-приложении создайте представление (view), которое будет обрабатывать запрос на загрузку файла. В этом представлении нужно проверить, что был отправлен файл, и сохранить его в папку <code>media</code>. Например:
	<pre><code>from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def upload_file(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload.html')</code></pre>

	<p>Здесь <code>request.FILES</code> содержит файлы, загруженные пользователем. Мы проверяем, что запрос метода POST, создаем экземпляр формы и проверяем ее на валидность. Если форма действительна, мы сохраняем файл в папку <code>media</code>. Если запрос метода GET, мы просто возвращаем шаблон с формой для загрузки файла.</p>

	<p>В папке появится новый файл. В дальнейшем вы можете записывать названия файла и получать его по ссылке</p>
	</li>
</ol>

## STEP 7

<p>Какой атрибут объекта <code>request</code> позволяет обратиться к файлам?</p>

- GET
- FILES
- POST
- data
