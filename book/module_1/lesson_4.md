## STEP 1

<p><strong>URLconf</strong></p>

<p>&nbsp;</p>

<p>В данном уроке мы изучим:</p>

<ul>
	<li>Что такое URL, URI и URN&nbsp;</li>
	<li>Функции файла urls.py</li>
	<li>Настройка urlpatters в приложениях</li>
</ul>

## STEP 2

<p><strong>URL vs URI</strong></p>

<p>Для того, чтобы правильно настраивать пути необходимо понять, что это вообще такое URL. Одна из распространенных точек путаницы заключается в том, должен ли веб-адрес называться <em>Uniform Resource Identifier</em> (URI) или <em>Uniform Resource Locator</em> (URL). Многие люди используют эти два термина взаимозаменяемо, независимо от того, знают ли они разницу.</p>

<p>Для начала давайте расшифруем аббревиатуры:</p>

<ul>
	<li><strong>URI - </strong>Uniform Resource Identifier<strong> </strong>(унифицированный <strong>идентификатор</strong> ресурса)</li>
	<li><strong>URL - </strong>Uniform Resource Locator (унифицированный <strong>определитель местонахождения</strong> ресурса)</li>
	<li><strong>URN - </strong>Unifrorm Resource Name (унифицированное <strong>имя</strong> ресурса)</li>
</ul>

<p>Многие считают, что http://google.com или http://yandex.ru - это просто URL-адреса, но, однако мы можем говорить о них как о URI. Фактически, URI представляет собой расширенный набор URL-адресов и нечто, называемое URN. Таким образом, мы можем с уверенностью заключить, что все URL являются URI. Однако обратное неверно.</p>

<p> </p>

<p style="text-align: center;"><img alt="" name="image.png" src="https://ucarecdn.com/2851e549-417f-4da0-9329-85fd6d75be13/" width="800"></p>

<h3><strong>Рассмотрим примеры:</strong></h3>

<p><strong>URL (Uniform Resource Locator):</strong></p>

<ul>
	<li>https://www.example.com/index.html</li>
	<li>ftp://ftp.example.com/documents/document.pdf</li>
	<li>http://localhost:8000/api/get_data/</li>
</ul>

<p> </p>

<p><strong>URI (Uniform Resource Identifier):</strong></p>

<ul>
	<li>example.com</li>
	<li>mailto:<a href="mailto:user@example.com" rel="noopener noreferrer nofollow" target="_new">user@example.com</a></li>
	<li>spotify:playlist:37i9dQZF1DX5Ejj0EkURtP</li>
</ul>

<p> </p>

<p><strong>URN (Uniform Resource Name):</strong></p>

<ul>
	<li>urn:isbn:0451450523</li>
	<li>urn:uuid:f81d4fae-7dec-11d0-a765-00a0c91e6bf6</li>
	<li>urn:ietf:rfc:2648</li>
</ul>

<p> </p>

<p><strong>URL</strong> (Uniform Resource Locator) для веб-страницы: <em>https://www.example.com/about/</em><br>
В этом примере, URL указывает на веб-страницу "about" на сайте www.example.com. URL включает схему (https), доменное имя (www.example.com) и путь к ресурсу (/about/).</p>

<p><strong>URI</strong> (Uniform Resource Identifier) для той же веб-страницы:<em> https://www.example.com/about/</em><br>
URI - это более общее понятие, которое включает в себя URL. В этом примере, URI также указывает на ту же веб-страницу "about" на сайте www.example.com, но он не обязательно должен указывать на протокол (https), он может также включать параметры запроса и фрагменты.</p>

<p>URN (Uniform Resource Name) для той же веб-страницы: <em>urn:example:about</em><br>
URN - это еще более абстрактное понятие, которое используется для идентификации ресурса по имени, а не по местоположению или схеме. В этом примере, URN указывает на ту же веб-страницу "about", но не указывает на местоположение или протокол. Он может использоваться для идентификации ресурса вне Интернета, например, для идентификации книги по ее ISBN.</p>

## STEP 3

<p>Выберите полный URL</p>

- ftp://example.com/files/file.txt ✅
- https://example.com ✅
- tel:123456789
- example.com?query=string
- mailto:user@example.com
- http://www.example.com/homepage ✅

## STEP 4

<p><strong>URL в Django</strong></p>

<p>URL-адреса в Django - это механизм, который связывает URL-шаблоны с определенными представлениями (views), которые обрабатывают запросы и возвращают ответы. При обработке запроса Django ищет соответствующий URL-шаблон, который наиболее точно соответствует URL-адресу запроса, и вызывает соответствующее представление (view), чтобы обработать запрос и вернуть ответ.</p>

<p>Шаблоны URL представляют собой текстовые строки, содержащие некоторые переменные, которые могут быть заменены на конкретные значения в зависимости от URL-адреса запроса. В Django мы используем специальный язык шаблонов URL, который позволяет определять шаблоны URL с переменными, которые затем могут быть извлечены и использованы в представлениях.</p>

<p>Например, шаблон URL может выглядеть так: <code>/path_to_my_view/&lt;int:pk&gt;/</code></p>

<p>Здесь <code>&lt;int:pk&gt;</code> - это переменная, которая указывает на целочисленный параметр с именем "pk". Этот параметр может быть извлечен из URL-адреса запроса и использован в представлении.<br>
Для пользователя данный URL может выглядеть так </p>

<p><em>https://https:://example.com/path_to_my_view/42/</em></p>

<p><strong>Файл urls.py</strong></p>

<p>Файл <code>urls.py</code> - это файл, который используется в Django для определения маршрутов URL и их сопоставления с функциями представления. Каждое Django-приложение имеет свой файл <code>urls.py</code>, который определяет маршруты URL для этого приложения.</p>

<p>В файле <em>urls.py</em> определяются следующие элементы:</p>

<ol>
	<li>
	<p><code>urlpatterns</code> - список объектов <code>path()</code> или <code>re_path()</code>, которые определяют маршруты URL для приложения.</p>
	</li>
	<li>
	<p><code>path()</code> - функция, которая определяет маршрут URL для приложения.</p>
	</li>
	<li>
	<p><code>re_path()</code> - альтернативная функция, которая позволяет определять маршруты URL с использованием регулярных выражений.</p>
	</li>
	<li>
	<p><code>include()</code> - функция, которая позволяет включать другие файлы <code>urls.py</code> в основной файл <code>urls.py</code>.</p>
	</li>
</ol>

<pre><code>from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]</code></pre>

<p>Подробнее про views мы изучим в следующей главе, но пока что нам достаточно знать, что мы указываем на "функцию", которой будет передан запрос.</p>

<p>Пока что вы можете видеть файл urls.py, который находится в папке проекта. В django принято, что в этом файле необходимо прописывать шаблон url приложения и после чего подключать другие файлы urls.py, находящиеся в папках самих приложений.<br>
Давайте предположим, что у нас есть сайт, в котором есть функционал как для пользователя, так и для разработчика. Для пользователя у нас будет одно приложение(<em>user_app</em>) и одно для разработчика(<em>admin</em>). Весь функционал разработчика будет доступен по ссылке www.example.com/admin/&lt;и т.д&gt;. Вместо того, чтобы прописывать пути ко всем страницам в одном файле urls.py. Мы расширяем главный файл и присоединяем к нему по файлу из каждого приложения.</p>

<pre><code>from django.urls import include, path

urlpatterns = [
    path('', include('user_app.urls')),
    path('admin/', include('admin.urls')),
]</code></pre>

<p>В папках приложений мы создали файлы urls.py</p>

<p>Их содержание выглядит примерно так:</p>

<pre><code># user_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
]</code></pre>

<pre><code># admin/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('developer/', views.developer, name='develop'),
    path('settings/', views.seting, name='settings'),
]</code></pre>

<p>Теперь у нашего сайт есть 4 рабочих ссылки:</p>

<ul>
	<li><em>example.com/ </em>- введет к функции index</li>
	<li><em>example.com/about/</em> - введет к функции about</li>
	<li><em>example.com/admin/developer/</em> - введет к функции developer</li>
	<li><em>example.com/admin/settings/</em> - введет к функции seting</li>
</ul>

## STEP 5
<p><strong>Регулярные выражения</strong></p>

<p>В прошлом шаге мы уже затронули шаблоны, на давайте рассмотрим немного подробнее.</p>

<p>Вот пример URL-шаблона, содержащего параметры:</p>

<pre><code>from django.urls import path
from . import views

urlpatterns = [
    path('blog/&lt;int:year&gt;/', views.year_archive),
]</code></pre>

<p>Этот URL-шаблон соответствует любому URL, начинающемуся с <code>blog/</code> за которым следует целое число, и заканчивающемся /<br>
Этот целочисленный параметр будет передан во <em>view</em> функцию <code>year_archive()</code> в качестве аргумента year.</p>

<p>Кроме <code>int</code>, в Django есть и другие типы параметров, такие как <code>str, slug, uuid, path</code>. Рассмотрим их на примере:</p>

<pre><code>from django.urls import path
from . import views

urlpatterns = [
    path('blog/&lt;int:year&gt;/', views.year_archive),
    path('blog/&lt;int:year&gt;/&lt;int:month&gt;/', views.month_archive),
    path('blog/&lt;int:year&gt;/&lt;int:month&gt;/&lt;slug:slug&gt;/', views.article_detail),
    path('profile/&lt;uuid:user_id&gt;/', views.profile),
    path('category/&lt;path:path&gt;/', views.category),
]</code>
</pre>

<p>Этот файл <code>urls.py</code> содержит несколько URL-шаблонов</p>

<ul>
	<li><code>blog/&lt;int:year&gt;/</code> - целочисленный параметр <code>year</code></li>
	<li><code>blog/&lt;int:year&gt;/&lt;int:month&gt;/</code> - целочисленные параметры <code>year</code> и <code>month</code></li>
	<li><code>blog/&lt;int:year&gt;/&lt;int:month&gt;/&lt;slug:slug&gt;/</code> - целочисленные параметры <code>year</code> и <code>month</code>, и текстовый параметр <code>slug</code> (slug - это короткая метка, состоящая из букв, цифр и дефисов)</li>
	<li><code>profile/&lt;uuid:user_id&gt;/</code> - уникальный идентификатор пользователя в формате UUID</li>
	<li><code>category/&lt;path:path&gt;/</code> - параметр <code>path</code>, который может содержать любую последовательность символов</li>
</ul>

<p><strong>Сопоставление URL-адресов с помощью регулярных выражений:</strong></p>

<pre><code>from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^articles/(?P&lt;year&gt;[0-9]{4})/(?P&lt;month&gt;[0-9]{2})/(?P&lt;slug&gt;[\w-]+)/$', views.article_detail,
name='article_detail'),
]</code></pre>

<p>Этот URL-шаблон использует регулярные выражения для сопоставления URL-адресов вида <code>/articles/2022/02/my-article/</code>. Он использует именованные группы регулярных выражений, чтобы извлечь значения параметров года, месяца и читаемого URL-адреса из URL-адреса</p>

## STEP 6

<p>Дан код, определите какие urls работают в проекте.<br>
Домен: www.example.com/</p>

<pre><code class="language-python"># project/urls.py
from django.urls import path, include

urlpatterns = [
    path('shop/', include('shop.urls')),
    path('user/', include('user.urls')),
]</code></pre>

<pre><code class="language-python"># shop/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('products/&lt;int:product_id&gt;/', views.product_detail, name='product_detail'),
]</code></pre>

<pre><code class="language-python"># user/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.change_password, name='change_password'),
]</code></pre>

- www.exam.com/shop/ ✅
- www.exam.com/shop/about/ ✅
- www.exam.com/
- www.exam.com/user/profile/edit/ ✅
- www.exam.com/shop/products/int:product_id/
- www.exam.com/shop/products/product_25/
- www.exam.com/shop/products/25/ ✅

## STEP 7

<p><strong>Функция reverse()</strong></p>

<p>Функция reverse() в Django - это утилита на языке Python, которая предоставляет возможность преобразовать описание представления и его аргументов в URL, который запустит указанное представление. Функция находится в модуле django.core.urlresolvers.<br>
Функция reverse() принимает до четырех аргументов:</p>

<ul>
	<li>viewname - имя представления, которое будет вызвано, или путь импорта, если имя не указано. Данный аргумент обязателен</li>
	<li>urlconf - путь импорта модуля конфигурации URL для поиска. Это необязательно, и если его нет или он равен None, значение берется из настройки ROOT_URLCONF</li>
	<li>args - кортеж из любых позиционных аргументов, которые будут переданы в представление</li>
	<li>kwargs - словарь любых именованных аргументов, которые будут переданы в представление</li>
</ul>

<p>Приведен пример использования функции reverse() для получения URL для конкретного объекта.</p>

<pre><code>from django.core.urlresolvers import reverse
reverse('library_article_detail', kwargs={'object_id': 1})</code></pre>

<blockquote>
<p>'/articles/1/</p>
</blockquote>

<p><strong>Функция path()</strong></p>

<p><code>path()</code> - это более простой способ определения URL-шаблонов. Он основан на использовании строковых шаблонов и может использовать специальные ключевые слова, такие как <code>&lt;int:variable&gt;</code> и <code>&lt;str:variable&gt;</code>, для извлечения значений из URL. <code>path()</code> работает только с ASCII-символами и не поддерживает регулярные выражения.<br>
Функция принимает 4 аргумента:</p>

<ul>
	<li><code>route</code> - строка, определяющая маршрут URL-адреса.</li>
	<li><code>view</code> - Python функция или класс, обрабатывающий запрос.</li>
	<li><code>kwargs</code> - (необязательный) ключевые аргументы, которые будут переданы в представление.</li>
	<li><code>name</code> - имя для определения URL, которое используется для создания URL-адресов в шаблонах.</li>
</ul>

## STEP 8

<p>Напишите путь, который введет к функции <em>see_author</em> по ссылке: <code>example.com/see_athor/?name=&lt;имя&gt;/</code><br>
Функция see_author принимает строку <em>author_name. </em>Имя у путя должно быть "see_author"</p>

<pre><code>from . import views
from django.urls import path

urlpatterns = [
    ....
]</code></pre>

- path("see_author/?name=<author_name:str>/", views.see_author, name="see_author")


### [Prev lesson](/book/module_1/lesson_3.md)
### [Next lesson](/book/module_1/lesson_5.md)
