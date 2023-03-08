## STEP 1

<p><strong>Данный модуль предназначен для повторения синтаксиса языка</strong>. Если вы даже уверены в своих знаниях, рекомендую прочитать небольшую документацию. Возможно, вы узнаете что то интересное)</p>

<p>Модуль будет разделен на 3 урока. В каждом будет присутствовать теория, тесты и задачи.<br />
В данном уроке мы повторим:</p>

<ol>
	<li>Вывод данных, print, аргументы sep, end</li>
	<li>Вывод данных, input, map</li>
	<li>Основные типы данных, арифметические действия, сравнение</li>
</ol>

<p><br />
P.S. Рекомендую пройти пару тестов и решить задачи, чтобы удостовериться в достаточности своих знаний.</p>

## STEP 2

<p><strong>Вывод данных </strong></p>

<p>Для вывода в консоль используется оператор print(). <br>
Внутри круглых скобок пишем, что хотим вывести на экран. Если это текст, то обязательно указываем его внутри кавычек. Кавычки могут быть одинарными или двойными. Только обязательно ставим одинаковые до и после текста</p>

<p>Например:</p>

<p><code>print("Hello, World!")</code></p>

<p>В результате мы получим:</p>

<blockquote>
<p>Hello, World!</p>
</blockquote>

<p>Оператор может принимать несколько аргументов(то что мы пишем в скобках), разных типов.</p>

<p><code>print("Hello", "World", "!) </code></p>

<blockquote>
<p>Hello World !</p>
</blockquote>

<p><code>print("My name is", "Bob", "I am", 20)</code></p>

<blockquote>
<p>My name is Bob I am 20</p>
</blockquote>

<p>Оператор print может принимать необязательный аргумент sep и end</p>

<p>Аргумент sep является разделителем всех аргументов оператора . По умолчанию он равен пробелу " ". </p>

<p><code>print("a", "b", "c", sep="\")</code></p>

<blockquote>
<p>a/b/c</p>
</blockquote>

<p>Аргумент end определяет что будет выводиться после вывода всех аргументов. По умолчанию он равен перевода на новую строке "\n".</p>

<p><code>print("a", "b", "c", end="")</code></p>

<p><code>print("d", "e", "f")</code></p>

<blockquote>
<p>a b cd e f</p>
</blockquote>

<p>Вы можете также запустить print без каких либо аргументов, тогда произойдет просто переход на новую строчку<br>
<br>
<code>print("Hello")</code></p>

<p><code>print()</code></p>

<p><code>print("World")</code></p>

<blockquote>
<p>Hello<br>
<br>
World</p>
</blockquote>

<p>Оператор print часто используют с f-строками.</p>

<p><code>name = 'Alex"</code></p>

<p><code>age = 12</code></p>

<p><code>print(f"My name is {name}\n I am {age} years old")</code></p>

<blockquote>
<p>My name is Alex<br>
I am 12 years old</p>
</blockquote>

## STEP 3

<p>Какой оператор используется для вывода значения в консоль?</p>

- input
- print ✅
- sep
- end

## STEP 4

<p>Как получить такой результат:</p>

<blockquote>
<p>Hello, World!</p>
</blockquote>

- print("Hello, World!") ✅
- print("Hello, World!\n")
- print("Hello", "World")
- print("Hello,", "World") ✅
- print("Hello", ',', 'World', sep="")
- print("Hello", ",", ' ', 'World!', sep="", end="\n") ✅

## STEP 5

<p><strong>Ввод данных с консоли</strong></p>

<p>Для получения данных от пользователя в питоне существует функция input()</p>

<p><code>name = input()</code></p>

<p>В качестве единственного аргумента оператор может принимать строку, которая появится при вводе.</p>

<p><code>name = input("Enter your name, please: ")</code></p>

<p><code>print("Your name is ", name)</code></p>

<blockquote>
<p>Enter your name, please: <strong>Bob</strong><br>
Your name is Bob</p>
</blockquote>

<p>По умолчанию в функция input возвращает строку(то что ввел пользователь) независимо от того, что он ввел.<br>
Для того, чтобы превратить введенное число в тип int, необходимо "обернуть" результат функцией int</p>

<p><code>name = input("Enter your name ")</code></p>

<p><code>age = int(input("Enter your age "))</code></p>

<p>Переменная name - строка, даже если мы введем строка. А переменная age - число целого типа. Но если мы введем, что то иное, то мы получим ошибку ValueError.</p>

<p>Иногда, нам требуется считать несколько переменных с одной строки. Для этого, мы можем разделить строку, используя метод split(). <br>
<code>name, age = input().split()</code></p>

<p>В данном случае мы считали имя и возраст, но оба переменные являются строкой.</p>

<p>Если нам необходимо считать несколько переменных одного типа и обработать их, то мы можем воспользоваться функцией map или генератором.</p>

<p><code>day, month, year = map(int, input("Enter your date of the birth: ").split("."))</code></p>

<blockquote>
<p><strong>Enter your date of birth:</strong> 01.01.2023</p>
</blockquote>

<p><code><span style="color: #000000;">day, month, year = [int(x) for x in input("</span>Enter your date of the birth: <span style="color: #000000;">").split()]</span></code></p>

<blockquote>
<p><strong>Enter your date of birth:</strong> 01 01 2023</p>
</blockquote>

## STEP 6

<p>Какой оператор используется для ввода с консоли?</p>

- input ✅
- print
- map
- split

## STEP 7

<p>Как получить число от пользователя?</p>

- int(input()) ✅
- input().split()
- print(int(input())

## STEP 8

<p>Напишите программу, которая считывает от пользователя его имя и возраст. И выводит информацию о нем в виде одной строки. В виде <em>Your name is &lt;имя&gt;. You are &lt;возраст&gt;</em></p>

<p><strong>Входные данные:</strong></p>

<blockquote>
<p>Alex<br>
12</p>
</blockquote>

<p><strong>Выходные данные:</strong></p>

<blockquote>
<p>Your name is Alex. You are 12</p>
</blockquote>

## STEP 9

<p><strong>Типы данных</strong></p>

<p>В питоне все типы данных делятся на изменяемые и неизменяемые.<br>
Чтобы получить все типы данных программным способом достаточно ввести 2 строчки:<br>
<code>import builtins as b</code></p>

<p><code>print(*[x for x in b.__dict__.values() if isinstance(x, type)], sep="\n")</code></p>

<p><br>
Основные из них это:</p>

<ul>
	<li>bool</li>
	<li>int</li>
	<li>float</li>
	<li>range</li>
	<li>complex</li>
	<li>str</li>
	<li>list</li>
	<li>dict</li>
	<li>set</li>
	<li>tuple</li>
	<li>frozenset</li>
</ul>

<p style="text-align: center;"><strong>Неизменяемые типы</strong></p>

<p>Неизменяемые типы это самая многочисленная группа. К ним относятся все числовые типы(int, float, complex), строки(str), tuple, bool и range.<br>
Каждый объект, в том числе и переменная имеет свою ячейку в памяти. Когда мы создаем переменную, мы выделяем ей ячейку памяти и присваем ей свой id. Для просмотра id, можно использовать одноименную функцию id()<br>
<code>a = 12</code></p>

<p><code>print(id(a))</code></p>

<blockquote>
<p>139987536233040</p>
</blockquote>

<p>Мы получили уникальный id переменной. Но если присвоим ей новое значение, то id поменяется</p>

<p><code>a = 12</code></p>

<p><code>print(id(a))</code></p>

<p><code>a = 15</code></p>

<p><code>print(id(a))</code></p>

<blockquote>
<p>139987536233040<br>
140580439933616</p>
</blockquote>

<p>С каждым изменением переменной мы выделяем новую ячейку памяти. </p>

<p style="text-align: center;"><strong>Изменяемые типы</strong></p>

<p>К изменяемым типам относятся lists, dicts и sets.<br>
Данные типы являются контейнерами. <br>
Если мы создадим список и добавим в него новый элемент, то id списка до добавления не будет отличаться от id после добавления.</p>

<p><code>a = [1, 2, 5]</code></p>

<p><code>print(id(a))</code></p>

<p><code>a.append(6)</code></p>

<p><code>print(id(a))</code></p>

<blockquote>
<p>139698798957888<br>
139698798957888</p>
</blockquote>

<p>После добавления в список сама переменная не меняется.</p>

## STEP 10

<p><strong>Основные методы и операторы переменных</strong></p>

<p style="text-align: center;"><strong>Числа</strong></p>

<p>Так как Python динамический язык, то у чисел нет ограничений в размерах, как во многих других языках.<br>
<code>print(10**100)</code></p>

<p>Данная строчка успешно выведет результат</p>

<blockquote>
<p>10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000</p>
</blockquote>

<p><strong>int - </strong>целое число, например <em>1</em>,<em> 5</em>,<em> -2</em><br>
<strong>float - </strong>вещественное число, например <em>1.02</em>,  <em>0.5, -10.7</em><br>
<u>Обратите внимание!</u> Десятичная часть разделяется от целой точкой.<br>
<strong>complex - </strong>комплексное число, например <em>12 + 6j</em>,<em> 0.5 + 0.2j</em>, -2 + 0.2j</p>

<p style="text-align: center;"><strong>Основные операции:</strong></p>

<p>В Python используются различные арифметические операции: сложение, вычитание, умножение, деление, целая часть от деления, остаток от деления, возведение в степень и другие</p>

<p><strong>Сложение: </strong>a + b</p>

<p><code>print(12 + 5)</code></p>

<p><code>print(12.5 + 6</code></p>

<blockquote>
<p>17<br>
18.5</p>
</blockquote>

<p><strong>Вычитание: </strong>a - b</p>

<p><code>print(12 - 5)</code></p>

<p><code>print(14.5-6.2)</code></p>

<blockquote>
<p>7<br>
8.3</p>
</blockquote>

<p><strong>Умножение: </strong>a * b</p>

<p><code>print(12 * 5)</code></p>

<p><code>print(2.5 * 5)</code></p>

<blockquote>
<p>60<br>
12.5</p>
</blockquote>

<p><strong>Деление: </strong>a / b</p>

<p><code>print(12 / b)</code></p>

<p><code>print(2 / 0.5)</code></p>

<blockquote>
<p>2.4<br>
0.4</p>
</blockquote>

<p><strong>Целая часть от деления: a // b</strong></p>

<p><code>print(16 // 5)</code></p>

<p><code>print(12.4 // 2.5)</code></p>

<blockquote>
<p>3<br>
4.0</p>
</blockquote>

<p><strong>Остаток от деления: a % b</strong></p>

<p><code>print(16 % 5)</code></p>

<p><code>print(14.2 % 3.1)</code></p>

<blockquote>
<p>1<br>
1.799999999999999</p>
</blockquote>

<p> </p>

<p style="text-align: center;"><strong>Списки(lists)</strong></p>

<p><strong>​​​​​​</strong>Во многих ЯП существует такой тип данных как массив. В питоне же он называется списком.</p>

<p>Список представляет собой последовательность элементов(иногда разных типов), пронумерованных от 0. </p>

<blockquote>
<p><code>mass = [1, 2, 3, "hello", 2.5, [5, 7]]</code></p>
</blockquote>

<p>Для того, чтобы получить элемент по индексу используются квадратные скобки []</p>

<p><code>print(mass[0])</code></p>

<p><code>print(mass[3], mass[5][1])</code></p>

<blockquote>
<p>1<br>
hello 7</p>
</blockquote>

<p>Также можно изменить значение списка обратившитс к нему по индексу.</p>

<p><code>mass[1] = 5</code></p>

<p><code>print(mass)</code></p>

<blockquote>
<p>[1, 5, 3, "hello", 2.5, [5, 7]]</p>
</blockquote>

<p><strong>Основные методы списка:</strong></p>

<ul>
	<li>append(val) - добавить в конец</li>
	<li>insert(val, index) - добавить по индексу</li>
	<li>remove - удалить первый элемент по значению</li>
	<li>pop - удалить по индексу</li>
	<li>clear - очистить список</li>
</ul>

<p>Функция len() позволяет узнать размер списка, строки, словаря, кортежа и сета</p>

<p><code>print(len(mass))</code></p>

<blockquote>
<p>6</p>
</blockquote>

<p>Для того, чтобы вывести список без квадратных скобок, можно его распаковать, используя звездочку *</p>

<p><code>print(*mass)</code></p>

<blockquote>
<p>1 2 3 hello 2.5 [5, 7]</p>
</blockquote>

<p style="text-align: center;"><strong>Кортежи (tuples)</strong></p>

<p>Кортеж очень похожий на список тип данных. Но он не изменяется. Если попробовать изменить элемент по индексу или применить методы списка, то выйдет ошибка.</p>

<p>Кортеж объявляется с помощью круглых скобок ()</p>

<p><code>tup = (1, 2,3)</code></p>

<p><code>print(tup)</code></p>

<blockquote>
<p>(1, 2, 3)</p>
</blockquote>

<p style="text-align: center;"><strong><em>Словари(dicts)</em></strong></p>

<p>Словари позволяют записывать значения используя ключ. Для записи и обращения в квадратных скобках [] пишут ключ, который является неизменяемым типом(чаще всего строкой или числом).</p>

<p>Для создания словаря используются фигурные скобки {}</p>

<p><code>slov = {}</code></p>

<p><code>slov['key'] = 'value'</code></p>

<p><code>print(slov)</code></p>

<p><code>print(slov['key'])</code></p>

<blockquote>
<p><span style="color: #000000;">{'slov: 'value'}</span><br>
<span style="color: #000000;">value</span></p>
</blockquote>

<p><span style="color: #000000;"><strong>Основные методы словарей:</strong></span></p>

<ul>
	<li><span style="color: #000000;">values - получить список всех значений</span></li>
	<li><span style="color: #000000;">keys - получить список всех ключей</span></li>
	<li><span style="color: #000000;">items - получить все элементы в виде кортежей</span></li>
	<li><span style="color: #000000;">update - обновляет словарь</span></li>
	<li><span style="color: #000000;">pop - удаляет по ключу</span></li>
</ul>

<p style="text-align: center;"><span style="color: #000000;"><strong>Множества(sets)</strong></span></p>

<p>Множества - это массив, который содержит неупорядоченные элементы. Множество не содержит дубликаты элементов. Множество изменяемый тип, но содержать оно может только не изменяемые типы.</p>

<p>Для создания множества используются фигурные скобки(точно такие же как и в словаре) {}. По умолчанию фигурные скобки питон воспринимает как словарь, поэтому необходимо добавить сразу несколько элементов.</p>

<p><span style="color: #000000;">st = {1, 2, "bob", 2.0}</span></p>

<p>Для того, чтобы создать пустое множество можно ввести set()</p>

<p><code>st = set()</code></p>

<p><strong>Основные методы множеств:</strong></p>

<ul>
	<li>add - добавить элемент</li>
	<li>remove - удалить элемент</li>
	<li>pop - удалить элемент и вернуть его</li>
</ul>

## STEP 11

<p>Что выведет данный код:</p>

<p><code>print(15 % 3, 15 // 3, 16 % 3, 16 // 3)</code></p>

- 0 5 1 5 ✅
- 5 0 5 1
- 0 5 0 5
- 45 5 48 5.3

## STEP 12

<p>Что выведет данный код?</p>

<p><code>print(-5 % 3, -5 // 3)</code></p>

- -1 -2
- 1 -2 ✅
- -2 -1
- 1 2

## STEP 13

<p>Что выведет данный код?</p>

<p><code>ls = [1, 5, 8, 2.0, [3, 4, 0, [2], 4], 7]</code></p>

<p><code>print(ls[1], ls[3], ls[4][2])</code></p>

- 5 2.0 0 ✅
- 1 8 4
- 5 2 0
- 1 8 0


### [Next lesson](/book/module_0/lesson_2.md)
