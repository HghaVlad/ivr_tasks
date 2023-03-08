## STEP 1

<p><strong>Данный модуль предназначен для повторения синтаксиса языка</strong>. Если вы даже уверены в своих знаниях, рекомендую прочитать небольшую документацию. Возможно, вы узнаете что то интересное)</p>

<p>Модуль будет разделен на 3 урока. В каждом будет присутствовать теория, тесты и задачи.<br>
В данном уроке мы повторим:</p>

<ol>
	<li>Конструкция if, else, match case.</li>
	<li>Циклы for, while</li>
	<li>Срезы и функция range()</li>
</ol>

<p><br>
P.S. Рекомендую пройти пару тестов и решить задачи, чтобы удостовериться в достаточности своих знаний.</p>

## STEP 2

<p><strong>Конструкции if, else, match case</strong></p>

<p>Как и во многих языка в питоне существует условная конструкция if.</p>

<p><span style="color: #000000;">if 5 &gt; 3:</span><br>
<span style="color: #000000;">    print("5 is more than 3")</span></p>

<p>Если нам требуется несколько частей, то используется условный оператор elif. А для обработки не выполняющегося условия оператор else</p>

<p><span style="color: #000000;">a = 5</span></p>

<p><code>if a &gt; 5:<br>
    print("more than 5")<br>
elif a == 4:<br>
    print("is equal 4")<br>
else:<br>
    print("less than 4")</code></p>

<p>Для того, чтобы вставить несколько условий можно воспользоваться скобками, or, and.</p>

<p><span style="color: #000000;">if a &gt; 5 and a != 6:<br>
<code>    print("a &gt; 6")</code></span></p>

<p>Начиная с версии python 3.10 появилась новая конструкция match case</p>

<p><code>language = "ru"</code></p>

<p><code>match language:<br>
    case "en":<br>
        print("English")<br>
    case "fr":<br>
        print("French")<br>
    case "ru":<br>
        print("Russian")<br>
    case _:<br>
         print("another language")</code></p>

<p>Нижние подчеркивание _ объявляет блок кода, который будет выполняться в том случае, если иные не выполнились<br>
 </p>

## STEP 3

<p>Что выведет данный код?</p>

<p><code>age = 19</code></p>

<p><code>gender = "male"</code></p>

<p><code>if age &lt; 18<br>
print("too young")<br>
elif age &gt; 19 and gender == "male":<br>
    print("young man")<br>
else:<br>
    print("young woman")</code></p>

- too young
- young man
- young woman ✅
- Появится ошибка

## STEP 4

<p>Представьте вам подается переменная name. Создайте конструкцию match case, которая будет обрабатывать это имя.</p>

`match name:`<br>
`case`<br>
`"Simon"`<br>
`:`<br>
`print("he is Simon")`<br>
`case _ :`<br>
`print("he is not Simon")`

## STEP 5

<p><strong>Циклы</strong></p>

<p>В Питоне существуют 2 типа циклов. Цикл while и for</p>

<p>Цикл while имеет следующий синтаксис:</p>

<p><span style="color: #000000;">i = 3<br>
<code>while i &lt; 5:<br>
    print(i)<br>
    i = i + 1</code></span></p>

<blockquote>
<p>3<br>
4</p>
</blockquote>

<p>Циклу for необходимо что то перебирать. Это может быть массив или строка, или range</p>

<p><code>mass = [1, 2, 3, 4, 5]</code></p>

<p><code>for value in mass:<br>
    print(value)</code></p>

<blockquote>
<p>1<br>
2<br>
3<br>
4<br>
5</p>
</blockquote>

<p><code>for i in range(5):<br>
    print(i)</code></p>

<blockquote>
<p>0<br>
1<br>
2<br>
3<br>
4</p>
</blockquote>

<p>Для того, чтобы перебирать сразу несколько списков можно объединить их с помощью функции zip</p>

<p><code>names = ['Ann', 'Alex', 'Bob']<br>
ages = [12, 15, 18]<br>
for name, age in zip(names, ages):<br>
    print("Name is", name, "Age is", age)</code></p>

<blockquote>
<p>Name is Ann <br>
Age is 12<br>
Name is Alex <br>
Age is 15<br>
Name is Bob <br>
Age is 18</p>
</blockquote>

<p> </p>

<p style="text-align: center;"><strong>Подробнее про range</strong></p>

<p>В цикле for очень часто используется функция range. Но что она вообще из себя представляет?</p>

<p>Как говорилось уже ранее, range - это тип данных. Но также это и функция, которая возвращает одноименный тип. </p>

<p><code>x = range(2)</code></p>

<p><code>print(x)</code></p>

<p><code>print(type(x))</code></p>

<blockquote>
<p>range(0, 2)<br>
&lt;class 'range'&gt;</p>
</blockquote>

<p>Сама функция это генератор целых чисел. В качестве аргументов она получает 3 числа(start, stop, step). Если передать только одно число, то оно будет восприниматься как stop. А start по умолчанию принимает 0, а step - 1. Если передать больше 1 значения, то порядок аргументов будет такой: Число с которого начинаем отсчет, Число перед котором заканчиваем отсчет, Шаг(необязательный аргумент). Важно заметить, что если у нас stop = 2, то функция не включает stop,  и последним числом будет 1.</p>

<p><code>for i in range(1, 5):</code></p>

<p><code>    print(i, end=" ")</code></p>

<p><code>print()</code></p>

<p><code>for i in range(1,6,2):</code></p>

<p><span style="color: #000000;">    <code>print(i, end=" ")</code></span></p>

<blockquote>
<p>1 2 3 4<br>
2 4</p>
</blockquote>

<p>Помимо циклов range можно также использовать как замену списку или картежу. Преимущество range перед list и tuple в том, что range всегда занимает одинаковое(меньше) количество памяти, независимо от самих аргументов.</p>

<p><code>r = range(2, 100000, 2)</code></p>

<p><code>print(19488 in r)</code></p>

<p><code>print(r.index(488188))</code></p>

<p> </p>

<p>Range тип можно распаковать или применить даже срезы</p>

<p><code>r = range(3, 31, 3)</code></p>

<p><code>print(*r)</code></p>

<p><code>print(r[0:5])</code></p>

<p><code>print(*r[0:5])</code> </p>

<blockquote>
<p>3 6 9 12 15 18 21 24 27 30<br>
range(3, 18, 3)<br>
3 6 9 12 15</p>
</blockquote>

## STEP 6

<p>Заполните пропуски, чтобы получился цикл while, который работает если i меньше 10. В переменную digit производится ввод целого числа, после чего к переменной summa прибавляется это число.</p>

PASSED

## STEP 7

<p>Что выведет данный код?</p>

<p><code>digits = [43, 5189, 53, 214, 98, 18, 4012, 601, 45, 520]</code></p>
<code>summа = 0</code>
<code>for i in range(0, len(digits), 3):</code>
<code>&nbsp; &nbsp; while digits[i] &gt;0:</code>
<code>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;summа = summа + digits[i] % 10</code>
<code>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;digits[i] = digits[i] // 10</code>
<p><code>print(summa)</code></p>

- 52
- 28 ✅
- 101
- 10793
- 14

## STEP 8

<p>Напишите программу, которая выводит сумму списка.<br>
На вход с подается число n. Дальше с новой строчки подаются n целых чисел.<br>
На выход ожидается одно целое число сумма введенных чисел.</p>

## STEP 9

<p style="text-align: center;"><strong>Срезы</strong></p>

<p>Для того, чтобы обратиться к определенному элементу списка, строки, кортежа в питоне, как и во многих языках используются индексы.</p>

<p><code>string = "Hello"</code></p>

<p><code>print(string[0], string[2]</code></p>

<p>Также существует такая вещь как срезы. Срез - это объект, который позволяет получить часть переменной.</p>

<p>Синтаксис срезов выглядит примерно так:</p>

<p><code>string[&lt;start&gt;:&lt;end&gt;:&lt;step&gt;]</code></p>

<p>Например </p>

<p><code>print(string[0:2])</code></p>

<blockquote>
<p>Hel</p>
</blockquote>

<p>В срезах нет обязательных "аргументов". Поэтому данный код будет работать</p>

<p><code>print(string[::])</code></p>

<blockquote>
<p><code>​​​​</code>Hello</p>
</blockquote>

<p>Срезы также могут принимать отрицательные значения</p>

<p><code>print(string[-1], string[-3:], string[::-1])</code></p>

<blockquote>
<p>o llo olloeh</p>
</blockquote>

<p>Если значение передаваемое в скобках больше длины строки выйдет пустая строка.</p>

<p>Но если срез применяется на список, то появится ошибка IndexError.</p>

## STEP 10

<p>Что выведет данный код?</p>

<p><code>string = "Hello!"</code></p>

<p><code>for i in range(1, len(string)):</code></p>

<p><code>    if i % 2 == 0:</code></p>

<p><code>        print(string[0:i])</code></p>

<p><code>    else:</code></p>

<p><code>        print(string[0:i], end=", ")</code></p>

<p>Введите ответ, соблюдая все пробелы и переходы на новую строчку</p>

- H, He<br>
Hel, Hell<br>
Hello, 

## STEP 11

<p>Что выведет данный код?</p>

<p><code>authors = [&#39;Пушкин&#39;, &#39;Достоевский&#39;, &#39;Лермонтов&#39;]</code></p>

<p><code>print(authors[1:], end=&quot; &quot;)</code></p>

<p><code>simple_string = &quot;I love Python&quot;</code></p>

<p><code>print(simple_string[-3:-1], simple_string[::2])</code></p>

- ['Достоевский', 'Лермонтов'] ho Ilv yhn ✅
- 'Достоевский', 'Лермонтов' hon Ilv yhn
- 'Достоевский', 'Лермонтов' ho Ilv yhn
- 'Достоевский', 'Лермонтов' ho I love Python


### [Prev lesson](/book/module_0/lesson_1.md)
### [Next lesson](/book/module_0/lesson_3.md)
