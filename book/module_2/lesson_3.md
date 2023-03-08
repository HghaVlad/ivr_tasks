## STEP 1

<p><strong>Шаблонизатор в django</strong></p>

<p> </p>

<p>В данном уроке мы изучим:</p>

<ul>
	<li>Что такое шаблонизатор и какой шаблонизатор в django </li>
	<li>Как передавать переменные в html код</li>
	<li>Язык шаблонов Django</li>
	<li>Написание собственных фильтров и тегов</li>
</ul>

## STEP 2

<p><strong>Что такое шаблонизатор</strong></p>

<p><strong>Шаблонизатор</strong> - это инструмент, который позволяет создавать динамические шаблоны для генерации текстовых документов, HTML-страниц и других типов документов. Он работает на основе простой и интуитивно понятной системы тегов, которые заменяются на соответствующие данные или динамически сгенерированный контент.</p>

<p><br>
В Django используется шаблонизатор jinja2.<br>
Jinja2 построен на основе концепции, что шаблон должен быть максимально простым и легко читаемым, а весь сложный код должен быть вынесен в контроллер приложения.</p>

<p>Основные особенности Jinja2:</p>

<ul>
	<li>Имеет простой и интуитивно понятный синтаксис, похожий на синтаксис языка Python.</li>
	<li>Позволяет использовать множество фильтров и расширений для более гибкой обработки данных и контроля визуального представления.</li>
	<li>Поддерживает наследование шаблонов, что позволяет создавать общие элементы различных страниц сайта.</li>
	<li>Поддерживает автоэскейпинг, что помогает избежать проблем с безопасностью исходного кода.</li>
</ul>

<p>Пример использования шаблона в Django</p>

<pre><code>&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;meta charset="UTF-8"&gt;
    &lt;title&gt;{% block title %}{% endblock %}&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;header&gt;
        &lt;h1&gt;{% block heading %}{% endblock %}&lt;/h1&gt;
    &lt;/header&gt;
    &lt;main&gt;
        {% block content %}{% endblock %}
    &lt;/main&gt;
    &lt;footer&gt;
        &lt;p&gt;{{ company_name }}&lt;/p&gt;
    &lt;/footer&gt;
&lt;/body&gt;
&lt;/html&gt;</code>
</pre>

<p>Помимо html тегов, здесь также присутствуют и шаблонные теги, которые заключены в {{ }} или в {% %}</p>

## STEP 3

<p><strong>Передаем переменные в шаблоны</strong></p>

<p>Как вам уже известно, для того, чтобы вернуть пользователю шаблон, используется функция render()<br>
В качестве 3 аргумента она принимает context(словарь из переменных)</p>

<pre><code>def hello(request, user_name):
    context = {
        'name': user_name
    }
    return render(request, "hello.html", context)</code></pre>

<p>Для того, чтобы в шаблоне нам получить эту переменную используются {{ }}. Внутри фигурных скобок идет сама переменная</p>

<p><code>&lt;h1&gt; Hello, {{ name }}&lt;/h1&gt;</code></p>

<p>Если данная переменная не передает в context, то шаблонизатор просто выведет пустоту. </p>

<p>Помимо строк, мы можем передавать и другие типы данных. Например</p>

<pre><code>context = {
    "weekdays": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "weekend": {
        6: "Saturday",
        7: "Sunday"
    },
    'request': request
}</code></pre>

<p>К спискам можно обратиться через точку. </p>

<pre><code>{{ weekdays.1 }}
{{ weekend.Saturday }}
{{ request.method }}</code></pre>

## STEP 4

<p>C помощью какого тега передают значения на страницу?</p>

- {{ }}
- { }
- {%  %}
- {& &}

## STEP 5

<h3><strong>Основные теги в Шаблонах</strong></h3>

<p>На предыдущем шаге мы узнали про передачу переменных, но что если нам требуется как то изменять верстку в зависимости от этих переменных? Сейчас мы узнаем основные теги, которые используются в шаблонах</p>

<p><strong>Оператор for</strong></p>

<pre><code>&lt;ul&gt;
{% for user in users %}
    &lt;li&gt;{{ user.name }}&lt;/li&gt;
{% endfor %}
&lt;/ul&gt;</code></pre>

<p><strong>Ветвление(if, else and elif)</strong></p>

<pre><code>{% if user.name == "Developer" %}
&lt;h1&gt; Welcome back! &lt;/h1&gt;
{% elif user.name == "Admin" %}
&lt;h1&gt; Ready to work &lt;/h1&gt;
{% else %}
&lt;he&gt; Hello, {{ user.name }}
{% endfor %}</code></pre>

<p><strong>CSRF_TOKEN</strong><br>
Как уже говорилось ранее, используется для защиты CSRF</p>

<pre><code>&lt;form&gt;
&lt;input name="value"&gt;
{% csrf_token %}
&lt;/form&gt;</code></pre>

<p> <strong>URL</strong><br>
Возвращает ссылку на абсолютный путь (URL без имени домена), соответствующий представлению и необязательным параметрам</p>

<pre><code>{% url 'some-url-name' v1 v2 %}</code></pre>

<p>Первый параметр - это имя шаблона URL . Это может быть буквальная строка в кавычках или контекстная переменная. Дополнительные параметры являются необязательными и предоставляются в виде значений, разделенных пробелами, которые будут использоваться в качестве параметров URL-адреса. В приведенном выше примере показано, как передавать позиционные параметры.<br>
Для того, чтобы url что то вернул необходимо, чтобы имя принадлежало какому то пути.<br>
 <code>path("some_url/&lt;str:var1&gt;/&lt;int:var2&gt;/", views.someurl, name="some-url-name")</code></p>

<p><strong>BLOCK and EXTENDS</strong></p>

<p>Самая мощная, но и самая сложная часть шаблонизатора Django - это наследование шаблонов. Это наследование позволяет вам создать базовый «скелетный» шаблон, содержащий все общие элементы вашего сайта, и определить блоки<strong>,</strong> которые дочерние шаблоны могут переопределить.</p>

<p>Давайте рассмотрим наследование шаблонов на примере:</p>

<pre><code>&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
    &lt;link rel="stylesheet" href="style.css"&gt;
    &lt;title&gt;{% block title %}My amazing site{% endblock %}&lt;/title&gt;
&lt;/head&gt;

&lt;body&gt;
    &lt;div id="sidebar"&gt;
        {% block sidebar %}
        &lt;ul&gt;
            &lt;li&gt;&lt;a href="/"&gt;Home&lt;/a&gt;&lt;/li&gt;
            &lt;li&gt;&lt;a href="/blog/"&gt;Blog&lt;/a&gt;&lt;/li&gt;
        &lt;/ul&gt;
        {% endblock %}
    &lt;/div&gt;

    &lt;div id="content"&gt;
        {% block content %}{% endblock %}
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>

<p>Этот шаблон, который мы назовем, <code>base.html</code> определяет скелет HTML-документа, который можно использовать для страницы с двумя столбцами. Задача «дочерних» шаблонов - заполнить пустые блоки содержимым.</p>

<p>В этом примере тег <code>block</code> определяет три блока, которые могут заполняться дочерними шаблонами. Тег <code>block</code> только сигнализирует механизму шаблонов, что дочерний шаблон может переопределить эти части шаблона.</p>

<p>Дочерний шаблон может выглядеть так:</p>

<pre><code>{% extends "base.html" %}

{% block title %}My amazing blog{% endblock %}

{% block content %}
{% for entry in blog_entries %}
    &lt;h2&gt;{{ entry.title }}&lt;/h2&gt;
    &lt;p&gt;{{ entry.body }}&lt;/p&gt;
{% endfor %}
{% endblock %}</code></pre>

<p>Тег <code>extends</code> является здесь ключевым. Он сообщает механизму шаблонов, что этот шаблон «расширяет» другой шаблон. Когда механизм шаблонов оценивает его, он сначала получает родительский объект, в данном случае «base.html».</p>

<p>На данный момент, шаблон двигатель замечает три метки <code>block</code> из <code>base.html</code> и заменяет эти блоки с содержимым шаблона ребенка.</p>

<p><strong>WITH</strong><br>
Помещает результат сложного выражения под более простое имя.</p>

<pre><code>{% with total=business.employees.count %}
    {{ total }} employee
{% endwith %}</code></pre>

<p>Также поддерживается и старый формат</p>

<pre><code>{% with business.employees.count as total%}
    {{ total }} employee
{% endwith %}</code></pre>

## STEP 6

<p>Какого оператора не существует в шаблонах Django?</p>

- for
- while ✅
- else
- block
- csrf_token

## STEP 7

<p><strong>Основные фильтры</strong><br>
Django поддерживает множество встроенных фильтров. Знать их всех избыточно, но некоторые все же полезно знать.<br>
Но что же такое фильтры?</p>

<p>Фильтры шаблонов - это инструкции, которые позволяют преобразовывать данные внутри шаблонов Django. Они позволяют изменять, форматировать и фильтровать данные перед их выводом на веб-страницу.</p>

<p> </p>

<p><strong>SAFE</strong><br>
По умолчанию, django преобразует HTML строки  в соответствующие их HTML-сущности, чтобы предотвратить возможность XSS-атак. То-есть:</p>

<ul>
	<li><code>&lt;</code> конвертируется в  <code>&amp;lt;</code></li>
	<li> <code>&gt;</code> конвертируется в <code>&amp;gt;</code></li>
	<li><code>'</code> (одинарная кавычка) конвертируется в <code>&amp;#x27;</code></li>
	<li><code>"</code> (двойная кавычка) конвертируется в <code>&amp;quot;</code></li>
	<li><code>&amp;</code> конвертируется в <code>&amp;amp;</code></li>
</ul>

<p>Для того, чтобы избежать такого изменения, можно использовать фильтр <code>safe</code></p>

<pre><code>{{ var|safe}}</code></pre>

<p><strong>Date</strong><br>
Преобразует дату в заданный формат</p>

<pre><code>{{ value|date:"D d M Y" }}</code></pre>

<p><strong>TIME</strong><br>
Аналогично также и с временем.</p>

<pre><code>{{ value|time:"H:i" }}</code></pre>

<p><strong>LENGTH</strong><br>
Возвращает количество элементов в списке</p>

<pre><code>{{ value|length }}</code></pre>

<p><strong>TRUNCATECHARS</strong><br>
Обрезает строку до заданного количества символов</p>

<pre><code>{{ value|truncatechars:7 }}</code></pre>

<p><strong>UPPER</strong><br>
Преобразуют строку в верхний регистр</p>

<pre><code>{{ value|upper }}</code></pre>

<p><strong>LOWER</strong><br>
Преобразуют строку в нижний регистр</p>

<pre><code>{{ value|lower }}</code></pre>

<p><strong>JOIN</strong><br>
Объединяет элементы списка в одну строку, разделяя их указанным разделителем.</p>

<pre><code>{{ value|join:" // " }}</code></pre>

<p><strong>SLICE</strong><br>
Позволяет выбрать определенный срез списка.</p>

<pre><code>{{ some_list|slice:":2" }}</code></pre>

<p>С остальными фильтрами вы по желанию можете <a href="https://docs.djangoproject.com/en/4.1/ref/templates/builtins/#built-in-filter-reference" rel="noopener noreferrer nofollow">ознакомиться самостоятельно</a></p>

<ul>
</ul>

## STEP 8

<p>Какой фильтр нужно использовать, чтобы передать строку в шаблон в точности без изменений ни при каких обстоятельствах?</p>

- safe

## STEP 9

<p><strong>Создание собственных фильтров и тегов</strong></p>

<p>Django позволяет на создавать собственные фильтры и теги, которые позволяют изменять данные перед их отображением. Создание собственных фильтров в шаблонах может быть полезным для форматирования данных или применения других преобразований к контенту перед отображением на веб-странице.</p>

<p>Создадим папку <code>templatetags</code> в директории нашего приложения, также создайте пустой файл <code>__init__.py</code> чтобы получился пакет. Очень важно, чтобы приложение было импортировано в <code>INSTALLED_APPS,</code> иначе наши фильтры просто не будут доступны.<br>
Наши собственные фильтры и теги будут находиться в созданной ранее папке.</p>

<p><strong>Фильтры</strong></p>

<p>Создадим новый файл(называть его можно как угодно). Этот файл будет нашей собственной библиотекой тегов.</p>

<pre><code>#templatetags/library_name.py
from django import template

register = template.Library()

@register.filter(name="splitl")
def splitl_func(value: str): # Из hello_world получаем Hello World
    return value.replace("_", " ")</code></pre>

<p>Каждай библиотека тегов должна содержать переменную уровня модуля с именем <code>register,</code> которая является объектом класса <code>Library.</code> Создадим функцию, которая будет принимать один аргумент, и возвращать строку, измененный аргумент. Эта функция и есть нашим фильтром.<br>
Осталось теперь только ее зарегистрировать. Регистрация происходит 2 способами.</p>

<ul>
	<li>Использования декоратора</li>
	<li>Регистрация напрямую через метод класса</li>
</ul>

<p><code>@register.filter("splitl")</code></p>

<p><code>register.filter("splitl", splitl_func)</code></p>

<p>Для того, чтобы применить наш фильтр в шаблоне необходимо подключить библиотеку в шаблон.</p>

<p>В начале шаблона пропишем<code>{% load &lt;library_name&gt; %}</code></p>

<pre><code>#templates/my_temaplte.html
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
  &lt;meta charset="UTF-8"&gt;
  &lt;meta http-equiv="X-UA-Compatible" content="IE=edge"&gt;
  &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
  &lt;title&gt;Document&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  {% load library_name %}
  &lt;h1&gt; Hello {{ some_value|splitl }} &lt;/h1&gt;
  
&lt;/body&gt;
&lt;/html&gt;</code></pre>

<p>Наши фильтры могут принимать несколько аргументов.</p>

<pre><code>#templatetags/library_name.py
from django import template

register = template.Library()

@register.filter(name="splitl")
def splitl_func(value: str): # Из hello_world получаем Hello World
    return value.replace("_", " ")


def splitlvl_func(value: str, rplv: str): # Из hello/world, / получаем Hello World
    return value.replace(rplv, " ")

register.filter("split_vl", splitlvl_func)</code></pre>

<pre><code>&lt;body&gt;
  {% load library_name %}
  &lt;h1&gt; Hello {{ some_value|split_vl:'/' }} &lt;/h1&gt;
  
&lt;/body&gt;</code></pre>

<p><strong>Теги</strong></p>

<p>Помимо фильтров, мы можем создавать более сложные конструкции, такие как теги.</p>

<p><strong>Simple tags</strong></p>

<p>Многие шаблоны используют теги, которые принимают несколько аргументов и возвращают значения. Например, текущее время. <code>{% now %}</code> уже встроен в стандартную библиотеку. Но что если нам требуется выбрать формат?</p>

<p>Создание простого тега очень похоже с созданием фильтра, только получения аргументов не обязательно.</p>

<pre><code>import datetime
from django import template

register = template.Library()

@register.simple_tag(name="current_time")
def current_time(format_string):
    return "Текущее время" + str(datetime.datetime.now().strftime(format_string))

def now_time():
    return datetime.datetime.now()

register.simple_tag(now_time, name="now")</code></pre>

<pre><code>&lt;body&gt;
  {% load library_name %}
  &lt;h1&gt; {% current_time "%D" %}&lt;/h1&gt;
  &lt;h1&gt; {% now %}&lt;/h1&gt;
  
&lt;/body&gt;</code></pre>

<blockquote>
<p>Текущее время 03/05/23</p>

<p>2023-03-05 12:53:58.189086</p>
</blockquote>

<p>Также мы можем передать<code>context</code>(словарь, который мы передаем в render) прямо в шаблон. Для этого в аргументах функции <code>simple_tag</code> надо передать <code>takes_context=True.</code>А первым параметром нашей функции и будет этот <code>context</code></p>

<pre><code># templatetags/library_name.py
@register.simple_tag(takes_context=True, name="digit_square")
def square_value(context):
  return context['digit']**2</code></pre>

<pre><code># views.py
return render("page.html", {"digit": 2})</code></pre>

<pre><code># templates/page.html
&lt;body&gt;
  {% load library_name %}
  &lt;h3&gt; {% digit_square %} &lt;/h3&gt;
&lt;/body&gt;</code></pre>

<p> Результатом же будет</p>

<blockquote>
<p>4</p>
</blockquote>

<p><strong>Inclusion tag</strong></p>

<p>Другой вид тегов, это <code>inclusion_tag</code> С помощью него мы можем отображать данные, рендеря их в определенном html файле.<br>
Наша функция возвращает новый <code>context </code>для файла, который будет создавать часть шаблона и  передавать результат в итоговый html файл, в котором и вызывается тег.</p>

<pre><code># templatetags/library_name.py
@register.inclusion_tag("red.html", name="red" )
def red_text(text):
    return {'text': text}</code></pre>

<pre><code># templates/page.html
&lt;body&gt;
  {% load library_name %}
  &lt;h3&gt; {% red "some_text" %}&lt;/h3&gt;
&lt;/body&gt;</code></pre>

<pre><code># templates/red.html
&lt;p style='color: red'&gt;  {{ text }} &lt;/p&gt;</code></pre>

<p>Результатом будет та же страница <code>page.html,</code> в которой присутствует "some_text" красного цвета.</p>

<p>Данный вид тегов также может принимать <code>context</code></p>

<pre><code># views.py
return render("page.html", {"color": "green"})</code></pre>

<pre><code># templatetags/library_name.py
@register.inclusion_tag("colored.html", takes_context=True, name="make_color" )
def clr_text(context, text):
    return {'text': text, 'color': context['clolor'}</code></pre>

<pre><code># templates/colored.html
{% if color == 'red' %}
&lt;p style='color: red'&gt;  {{ text }} &lt;/p&gt;
{% elif color == 'green' %}
&lt;p style='color: green'&gt;  {{ text }} &lt;/p&gt;
{% endif%}</code></pre>

<pre><code># templates/page.html
&lt;body&gt;
  {% load library_name %}
  &lt;h3&gt; {% make_color "some_text" %}&lt;/h3&gt;
&lt;/body&gt;</code></pre>

## STEP 10

<p>Как надо называть переменную объекта <code>Library()</code>?</p>

- register


### [Prev lesson](/book/module_1/lesson_2.md)
### [Next lesson](/book/module_1/lesson_4.md)
