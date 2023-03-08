## STEP 1

<p><strong>Привет!</strong></p>

<p>Урок про представления получился очень большой, поэтому было решено разделить его на 2 части. Это вторая часть, в который ты узнаешь:</p>

<ol>
	<li>Что такое request</li>
	<li>Как подключить представление к URL</li>
	<li>Как написать представление в виде классов</li>
	<li>Как обрабатывать POST запросы</li>
</ol>

## STEP 2

<p><strong>​​​​​Объект HttpRequest </strong></p>

<p>Как говорилось ранее, обязательным аргументом любого представления является запрос пользователя (request). Функции получает объект класса HttpRequest. Давайте подробнее познакомимся с ним.</p>

<p>Когда страница запрашивается, Django создает объект <code>HttpRequest</code>, содержащий метаданные о запросе. Затем Django загружает соответствующее представление, передавая этот объект.</p>

<p>Основные атрибуты класса:</p>

<ul>
	<li><code>request.GET</code> - словарь, содержавший все параметры запроса, переданные в строке запроса. Например, ссылка <a href="http://example.com/?name=John/" rel="noopener noreferrer nofollow">http://example.com/?name=John</a> <code>request.GET</code> будет возвращать {"name": "John"}</li>
	<li><code>request.POST</code> - словарь, содержащий данные, отправленные с помощью метода POST. Данные могут быть в виде формы или JSON. Например, если пользователь заполнил форму с именем и паролем и отправил ее на сервер, то <code>request.POST</code> будет содержать {'username': 'user', 'password': 'pass'}</li>
	<li><code>request.method</code>- строка, содержащая HTTP-метод, который был использован для запроса. Это может быть GET, POST, PUT, DELETE и т.д.</li>
	<li><code>request.META</code> -словарь, содержащий метаданные запроса, такие как IP-адрес клиента, информация о браузере и т.д. Например <code>request.META.get('HTTP_X_FORWARDED_FOR') </code>вернет ip клиента</li>
	<li><code>request.path </code> - строка, содержащая путь запроса без параметров. Например, если URL запроса имеет вид <code>http://example.com/blog/1/edit/</code>, то <code>request.path</code> будет содержать <code>/blog/1/edit/</code></li>
	<li><code>request.user</code> - объект пользователя, который сделал запрос. Если пользователь не аутентифицирован, то <code>request.user</code> будет равен <code>AnonymousUser</code>. Подробнее про пользователей мы узнаем в следующих главах</li>
</ul>

<p>HttpRequest также имеет ряд методов, которые могут быть использованы для работы с запросом. Например:</p>

<ul>
	<li>
	<p><code>request.is_secure()</code> - возвращает True, если запрос был отправлен через защищенное соединение (HTTPS).</p>
	</li>
	<li>
	<p><code>request.is_ajax()</code> - возвращает True, если запрос был отправлен с помощью JavaScript-фреймворка, такого как jQuery или Prototype.</p>
	</li>
	<li>
	<p><code>request.get_host()</code> - возвращает имя хоста, к которому был отправлен запрос.</p>
	</li>
	<li>
	<p><code>request.get_full_path()</code> - возвращает полный путь запроса с параметрами.</p>
	</li>
</ul>

## STEP 3

<p><strong>Подключение представлений к определенному URL</strong></p>

<p>В прошлой главе мы затрагивали тему urlpatterns. Именно там мы и можем связывать наши представленияю.</p>

<pre><code># urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
]</code>
</pre>

<p>Как вы заметили мы импортируем весь файл views, и в аргументах <code>path </code>передаем функцию hello. Это та самая функция из предыдущего шага.<br>
Мы можем подключать одну и ту же функцию несколько раз.</p>

<pre><code># urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('hello', views.hello, name='hello2'),
    path('', views.hello, name='index'),
]</code>
</pre>

<p><strong>Передача регулярных выражений</strong><br>
В предыдущей главе мы передавали параметры через url.</p>

<pre><code># urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('hello/?name=&lt;str:user_name&gt;', views.hello, name='hello'),
]</code>
</pre>

<p>Для того, чтобы функция приняла user_name, необходимо добавить его в качестве параметров функции.</p>

<pre><code># views.py
from django.shortcuts import render

def hello(request, user_name):
    context = {'name': user_name}
    return render(request, 'hello.html', context)
</code>
</pre>

<p>Этот аргумент обязателен и если функция не будет его принимать, может появиться ошибка.</p>

## STEP 4

<p>Как получить данные, отправленные POST запросом?</p>

- request.get
- request.data
- request.POSTReq
- request.post
- request.POST ✅
- request.META

## STEP 5

<p><strong>Представления в виде классов</strong></p>

<p>Представления, написанные в виде классов, являются более гибкими и могут использоваться для обработки более сложных запросов. Вот как можно написать представление в виде класса</p>

<pre><code>from django.views import View
from django.http import HttpResponse

class GreetingView(View):
    def get(self, request):
        return HttpResponse("Hello, World!")</code>
</pre>

<p>В этом примере мы определили класс <code>GreetingView</code>, который наследуется от класса <code>View</code>, который является базовым классом для всех представлений в Django. Метод <code>get()</code> вызывается, когда клиент делает запрос типа GET.</p>

<p>Метод <code>get()</code> принимает объект <code>request</code> и возвращает объект <code>HttpResponse</code>, который отправляет строку "Hello, World!" в ответ на запрос клиента.</p>

<p>После того, как мы определили класс <code>GreetingView</code>, мы можем зарегистрировать его в файле urls.py:</p>

<pre><code>from django.urls import path
from .views import GreetingView

urlpatterns = [
    path('hello/', GreetingView.as_view(), name='greeting'),
]
</code>
</pre>

<p>Здесь мы зарегистрировали <code>GreetingView</code> с помощью метода <code>as_view()</code>. Это создает экземпляр представления и регистрирует его в системе URL-адресов.</p>

<p>Когда клиент делает запрос на /hello/, Django вызывает метод <code>get()</code> представления <code>GreetingView</code>, который возвращает <code>HttpResponse</code> с содержимым "Hello, World!".</p>

## STEP 6

<p><strong>Обработка POST запросов</strong></p>

<p>Очень часто у нас есть необходимость обработки POST запросов. Например при заполнении пользователем какой-либо формы.</p>

<p>Вот пример кода, созданного для создания отзывов от пользователей:</p>

<pre><code># views.py
from django.shortcuts import HttpResponse, render

def feedback(request):
    if request.method == "GET":
        return render(request, "feedback.html")
    else:
        data = request.POST
        name = data['name']
        review = data['user_feedback']
        print(name, review)
        return HttpResponse("Thank your for your answer")
</code></pre>

<pre><code># feedback.html
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;Форма отзыва&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;h1&gt;Форма отзыва&lt;/h1&gt;
    &lt;form method="POST" action=""&gt;

        &lt;label for="name"&gt;Имя:&lt;/label&gt;
        &lt;input type="text" id="name" name="name" required&gt;
        &lt;br&gt;
        &lt;label for="review"&gt;Отзыв:&lt;/label&gt;
        &lt;textarea name="user_feedback" required&gt;&lt;/textarea&gt;
        &lt;br&gt;
        &lt;input type="submit" value="Отправить"&gt;
        {% csrf_token %}
    &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>

<p> </p>

<p>Как вы видите сначала мы проверяем какой метод запроса у пользователя так как после заполнения формы запрос отправляется на эту же страницу(<code>action = ""</code>). Если бы <code>action</code> был иной, но не обязательно было бы проверять метод. Если у нас POST запрос мы получаем словарь с результатами формы. Ключами словаря являются переменные <code>name</code> в <code>input </code>и <code>textarea</code>. <br>
Обратите внимание на использование атрибута <code>csrf_token</code>, который генерирует токен защиты от подделки межсайтовых запросов (CSRF).</p>

<p><strong>Что такое csrf_token?</strong></p>

<p><code>csrf_token</code> (или "токен защиты от подделки межсайтовых запросов", Cross-Site Request Forgery) - это механизм защиты от атак, при которых злоумышленник пытается отправить запрос от имени аутентифицированного пользователя.</p>

<p>В Django этот механизм реализован путем включения токена в форму, который генерируется каждый раз, когда генерируется HTML-страница, содержащая форму. Токен передается в форме и затем проверяется при обработке запроса на сервере.</p>

<p>Для включения токена в форму в Django используется шаблонный тег <code>{% csrf_token %}</code>. Вот пример использования этого тега в HTML-форме.</p>

<p>При отправке этой формы браузер автоматически добавит токен защиты в заголовок запроса. При обработке запроса на сервере Django автоматически проверит наличие этого токена и отклонит запрос, если он отсутствует или некорректен.</p>

<p>Этот механизм защиты является важным элементом безопасности веб-приложений и должен использоваться везде, где используются формы для отправки данных на сервер.</p>

<p>Этот атрибут обязательно вставлять в каждую форму, иначе будет вызываться ошибка.</p>

## STEP 7

<p>Какой токен по умолчанию необходим, чтобы заполнение формы пользователем произошло успешно?</p>

- csrf_token

## STEP 8

<p>Выведет ли ошибку такой код, если пользователь перейдет по адресу <code>/calculate/12/5</code></p>

<pre><code>from django.shortcuts import HttpResponse

def calculate(request):
    return HttpResponse(1 + 2)

def calculate_digits(request, digit1, digit2):
    return HttpResponse(digit1 + digit2)</code>
</pre>

<pre><code>from django.urls import path
from views import calculate, calculate_digits
urlpatters = [
    path("", calculate),
    path("calculate/&lt;str:digit1&gt;/&lt;str:digit2&gt;", calculate_digits, name="calculate_digits")
]</code></pre>

- ДА ✅
- НЕТ


### [Prev lesson](/book/module_1/lesson_1.md)
### [Next lesson](/book/module_1/lesson_3.md)
