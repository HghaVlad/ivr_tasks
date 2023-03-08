## STEP 1

<p><strong>Данный модуль предназначен для повторения синтаксиса языка</strong>. Если вы даже уверены в своих знаниях, рекомендую прочитать небольшую документацию. Возможно, вы узнаете что то интересное)</p>

<p>Модуль будет разделен на 3 урока. В каждом будет присутствовать теория, тесты и задачи.<br>
В данном уроке мы повторим:</p>

<ol>
	<li>Функции, lambda функция.</li>
	<li>Декораторы, конструкция try Except</li>
	<li>Классы</li>
</ol>

<p><br>
P.S. Рекомендую пройти пару тестов и решить задачи, чтобы удостовериться в достаточности своих знаний.</p>

## STEP 2

<p><strong>Функции</strong></p>

<p>Представим, что нам необходимо повторять один и тот же кусок входа несколько раз. Для того, чтобы исключить копирования кода придумали функции. <br>
В питоне функция - это объект принимающий любые  аргументы и возвращающие значения. <br>
Для того, чтобы определить функцию используется оператор def.</p>

<p><code>def function_name(*args, **kargs):</code></p>

<p><code>    # Function code</code></p>

<p><span style="color: #000000;">После def пишется название функции, а в скобочках параметры.</span><br>
Для того, чтобы вызвать функцию, достаточно написать название функции и добавить скобочки. В скобочках можно добавить аргументы.</p>

<p><code>def print_function(text):</code></p>

<p><code>    print(text)</code></p>

<p><code>print_function("Text to be printed")</code></p>

<p><code>print(print_function("Text to be printed"))</code></p>

<blockquote>
<p>Text to be printed<br>
None</p>
</blockquote>

<p>Для того, чтобы функция вернула значения необходимо добавить оператор return</p>

<p><code>def calculate(a: int, b:int):</code></p>

<p><code>    return a + b</code></p>

<p><code><span style="color: #000000;">result = calculate(3, 5)</span></code></p>

<p><code><span style="color: #000000;">print(result)</span></code></p>

<p><span style="color: #000000;">Параметром называется то, что получает функция. Это переменные a и б. Аргументами функции называется то, что передается функции. Это 3 и 5.</span></p>

<p><span style="color: #000000;">Иногда, для удобства работы в IDE в параметрах функции также задают и тип переменной, которую функция получает.</span><br>
Чтобы сделать не обязательным передачу аргумента, параметру можно добавить значения по умолчанию</p>

<p><code>def calculate(a, b = 1):</code></p>

<p><code>    print(a * b)</code></p>

<p><code>print(calculate(5))</code></p>

<p><code>print(calculate(5, 2))</code></p>

<blockquote>
<p>5<br>
10</p>
</blockquote>

<p><strong>lambda функция</strong></p>

<p>Еще один способ записи функции в питоне это создание lambda функции. Лямбды функции анонимны, то есть функция безымянна. В отличии от def, нам не надо писать название функции. Но мы можем присвоить ее как переменную.<br>
Синтаксис выглядит примерно так:<br>
<code>Lambda аргументы: выражение</code></p>

<p>Например</p>

<p><code>mass = [1, 2, 3, 4]</code></p>

<p><code>print(list(map(lambda x: x**2, mass))) </code></p>

<p><code>f = lambda x: x**2</code></p>

<p><code>print(f(2))</code></p>

<blockquote>
<p>[1, 4, 9, 16]<br>
4</p>
</blockquote>

<p>В последнем случае у нас x аргумент функции. А x**2 это то, что возвращает функция.</p>

## STEP 3

<p><code>def square(x):</code></p>

<p><code>    return x * x</code></p>

<p><code>res = square(4)</code></p>

<p><code>print(res)</code></p>

<p>Что в данном коде является аргументом функции?</p>

- x
- 4 ✅
- res
- return x * x

## STEP 4

<p>Выберите в рабочие лямбда функции:</p>

- lambda x : x ✅
- lamda x: x**2
- lambda x: return x**2
- lambda x, y: x+ y ✅
- lambda x, y, z: return (z+y) * x
- lambda x = x: x*10 for x in range(1, 11) ✅

## STEP 5

<p><strong>Декораторы</strong></p>

<p>Допустим, нам надо добавить один и тот же функционал для разных функций. Например посчитать время выполнения той или иной функции. Вместо того, чтобы переписывать несколько уже существующие функции можно их обернуть в одну новую. Для этого, нам могут и пригодиться декораторы.</p>

<p>Декораторы — это обёртки вокруг Python-функций (или классов), которые изменяют работу того, к чему они применяются. </p>

<p>Декоратор создается как функция, в параметры которой приходит функция, к которой мы и будем применять декоратор.<br>
Внутри функции декоратора создается функция обертка, внутри которой мы в определенный момент и вызываем функцию, которая передана как аргумент к функции декоратора. <br>
Проще всего понять это на примере:</p>

<p><code>def decorator_function(func_to_be_called):</code></p>

<p><code>    def wrapper(*args, **kwargs):</code></p>

<p><code>        print("Some text before calling function")</code></p>

<p><code>        func_to_be_called(*args, **kwargs)</code></p>

<p><code>        print("Some text after calling function")</code></p>

<p><code>    return wrapper</code></p>

<p><code>@decorator_function</code></p>

<p><code>def print_function(text):</code></p>

<p><code>    print("Your text is:", text)</code></p>

<p><code>print_function("Hello")</code></p>

<blockquote>
<p>Some text before calling function<br>
Your text is: Hello<br>
Some text after calling function</p>
</blockquote>

<p>Для того, чтобы на функцию применялся декоратор, перед объявлением функции мы добавили @ и название декоратора.<br>
На одну функцию можно применять несколько декораторов.</p>

<p>Например:</p>

<p><code>from datetime import datetime</code><br>
<br>
<code>def decorator_function(func_to_be_called):<br>
    def wrapper(*args, **kwargs):<br>
        print("Some text before calling function")<br>
        func_to_be_called(*args, **kwargs)<br>
        print("Some text after calling function")<br>
    return wrapper<br>
<br>
def time_sum(func):<br>
    def wrapper(text):<br>
        d1 = datetime.now()<br>
        print("Time before calling", d1)<br>
        func(text)<br>
        d2 = datetime.now()<br>
        print("Time after calling", d2)<br>
        print(d2 - d1)<br>
    return wrapper<br>
<br>
@time_sum<br>
@decorator_function<br>
def print_function(text):</code></p>

<p><code>    print("Your text is:", text)</code></p>

<p><code>print_function("Hello")</code></p>

<blockquote>
<p>Time before calling 2023-02-11 16:07:48.526768<br>
Some text before calling function<br>
Your text is: Hello<br>
Some text after calling function<br>
Time after calling 2023-02-11 16:07:48.526843<br>
0:00:00.000075</p>
</blockquote>

<p>Иногда, нам необходимо применить декоратор для функции, которая что то возвращает.<br>
Для этого, при вызове функции в декораторе, результат мы присваиваем переменной и в конце функции обертки возвращаем эту переменную.</p>

<p><code>def decorator_function(func_to_be_called):<br>
    def wrapper(text):<br>
        print("Some text before calling function")<br>
        result = func_to_be_called(text)<br>
        print("Some text after calling function")<br>
        return result<br>
        <br>
    return wrapper</code></p>

<p><br>
<code>@decorator_function<br>
def print_function(text):</code></p>

<p><code>  return "Your text is: " + text</code></p>

<p><code>print(print_function("Hello"))</code></p>

## STEP 6

<p>Определите что выведет данный код:</p>

<p><code>from datetime import datetime</code></p>

<p><code>def dec_func(func):<br>
    def wrapper(arg):<br>
        t1 = datetime.now()<br>
        x = func(arg)<br>
        t2 = datetime.now()<br>
        print("Time of completing this task:", x, end=" ")<br>
        return x<br>
    return wrapper</code></p>

<p><code>@dec_func    <br>
def factorial(n):<br>
    res = 1<br>
    for i in range(1, n+1):<br>
        res = res * i<br>
    return res<br>
fact_100 = factorial(3)<br>
print(fact_100)</code></p>

- 6 Time of completing this task: 6
- x Time of completing this task: x
- 6 Time of completing this task: 0:00:00.000018
- Time of completing this task: 0:00:00.000018 6
- Time of completing this task: 6 6 ✅

## STEP 7 

<p>Время для написания собственных декораторов!<br>
<br>
Напишите функцию, в аргументы которой приходят два целых числа. Функция должна вернуть сумму этих чисел.</p>

<p>Также, напишите функцию декоратор, которая перед выполнением первой функции проверят есть ли среди этих чисел отрицательное число и выводит "YES", если такое число есть.</p>



## STEP 8

<p><strong>Обработка исключений</strong></p>

<p>Во время появления ошибки, программа на питоне сразу останавливается.<br>
Чтобы приложение продолжило работу при возникновении проблем, такие ошибки нужно перехватывать и обрабатывать с помощью блока <code>try/except</code></p>

<p>Допустим, наша программа получает два числа и необходимо вывести частное от деления первого числа на второе.</p>

<p><code>a, b = map(int, input().split())</code></p>

<p><code>print(a / b)</code></p>

<blockquote>
<p><strong><em>4 2</em></strong><br>
2.0</p>
</blockquote>

<p>Но что если мы введем число 0</p>

<blockquote>
<p><strong>4 0</strong><br>
Traceback (most recent call last): ....<br>
ZeroDivisionError: division by zero</p>
</blockquote>

<p>Для того, чтобы наша программа не останавливалась мы можем написать такой код</p>

<p><code>a, b = map(int, input().split())<br>
try:<br>
    print(a / b)<br>
except:<br>
    print("Error") </code></p>

<blockquote>
<p><strong>4 0</strong><br>
Error</p>
</blockquote>

<p>Для того, чтобы вывести саму ошибку мы можем ее получать в виде типа Exception</p>

<p><code>a, b = map(int, input().split())<br>
try:<br>
    print(a / b)<br>
except Exception as ex:<br>
    print("Error", ex)</code></p>

<blockquote>
<p><strong>4 0</strong><br>
Error division by zero</p>
</blockquote>

<p>Если нам требуется разные виды ошибок обрабатывать, то можно указать после except и название ошибки, например:</p>

<p><code>try:<br>
    a, b = map(int, input().split())<br>
    print(a / b)<br>
except ZeroDivisionError:<br>
    print("Error")<br>
except:<br>
    print("Something another")</code></p>

<blockquote>
<p><strong>4 0</strong><br>
Error</p>
</blockquote>

<blockquote>
<p><strong>4 hell</strong><br>
Something another</p>
</blockquote>

## STEP 9

<p><strong>Конструкции finally и else при обработки исключений.</strong></p>

<p style="text-align: center;"><strong>Finally</strong></p>

<p>При обработке исключений можно после блока try использовать блок finally. Он похож на блок except, но команды, написанные внутри него, выполняются обязательно. Если в блоке try не возникнет исключения, то блок finally выполнится так же, как и при наличии ошибки, и программа возобновит свою работу.</p>

<p><code>try:<br>
    a, b = int(input()), int(input())<br>
    print(a +b)<br>
except:<br>
    print("error")<br>
finally:<br>
    print("end")</code></p>

<blockquote>
<p><strong>1<br>
2</strong><br>
3<br>
end</p>
</blockquote>

<blockquote>
<p><strong>1<br>
hello</strong><br>
error<br>
end</p>
</blockquote>

<p style="text-align: center;"><strong>Else</strong></p>

<p>Иногда нужно выполнить определенные действия, когда код внутри блока try не вызвал исключения. Для этого используется блок else.</p>

<p><code>try:<br>
    a, b = int(input()), int(input())<br>
    print(a +b)<br>
except:<br>
    print("error")<br>
else:<br>
    print("end")</code></p>

<blockquote>
<p><strong>1<br>
2</strong><br>
3<br>
end</p>
</blockquote>

<blockquote>
<p><strong>1<br>
hello</strong><br>
error</p>
</blockquote>

<p style="text-align: center;"><strong>Raise Exception</strong></p>

<p>Также мы можем сами вызывать ошибки, для этого используется блок raise.</p>

<p><code>a, b = int(input()), int(input())<br>
if a + b == 3:<br>
    raise RuntimeError("Oops, sum is 3")<br>
else:<br>
    print(a + b)</code></p>

<blockquote>
<p><strong>1<br>
2</strong><br>
RuntimeError: Oops, sum is 3</p>
</blockquote>

<blockquote>
<p><strong>1<br>
5</strong><br>
6</p>
</blockquote>

<p>После raise мы пишем вид ошибки, в аргументах которой вводится комментарий.</p>

## STEP 10

<p>Что выведет данный код:</p>

<p><code>try:<br>
    a = input()<br>
    b = int(input())<br>
    print(a + b)<br>
except ValueError:<br>
    print(a)<br>
except TypeError:<br>
    print(b)<br>
except:<br>
    print("Else")</code></p>

<p><strong>Входные данные:</strong><br>
Случай 1:</p>

<blockquote>
<p><strong>12<br>
5</strong></p>
</blockquote>

<p>Случай 2: </p>

<blockquote>
<p><strong>hello<br>
world</strong></p>
</blockquote>

- 5 <br>hello ✅
- Else<br>5
- 17<br>Else
- 17<br>world

## STEP 11

<p><strong>Классы</strong></p>

<p>В Python можно сказать все сущности является объектами. Начиная от переменный и заканчивая классами и функциями.<br>
<code>x = "simple string"</code></p>

<p><code>print(type(x))</code></p>

<p><code>print(type(print), type(</code>x.find<code>))</code></p>

<blockquote>
<p>&lt;class 'str'&gt;<br>
&lt;class 'builtin_function_or_method'&gt; &lt;class 'builtin_function_or_method'&gt;</p>
</blockquote>

<p>Переменная x - это объект, точно также как и функция print и метод find строки. <br>
Как вы можете заметить, все все эти объекты разные типы классов. Таким образом, создать класс значит создать новый тип объекта а позже и создать новый экземпляр этого класса.</p>

<p>Для создания класса достаточно написать оператор class и название класса.</p>

<p><code>class Person:<br>
    pass</code></p>

<p>Перед вами новый пустой класс Person. Пока что он ничего не делает. Но мы можем создать экземпляр класса.<br>
<code>person_1 = Person()<br>
 print(type(person_1), person_1)</code></p>

<blockquote>
<p>&lt;class '__main__.Person'&gt;  &lt;__main__.Person object at 0x00000288CC85B0A0&gt;</p>
</blockquote>

<p>Внутри класса могут быть функции, они называются методами.</p>

<p><code>class Person:<br>
    def say_hi():<br>
         print("Hi!")</code></p>

<p><code>Person.say_hi()</code></p>

<blockquote>
<p>Hi!</p>
</blockquote>

<p>Если же мы попробуем вызвать функцию у экземпляра, то мы получим ошибку <samp>TypeError</samp></p>

<p><samp><code>person_1.say_hi()</code></samp></p>

<blockquote>
<p><samp>TypeError: say_hi() takes 0 positional arguments but 1 was given</samp></p>
</blockquote>

<p>Дело в том, что когда экземпляр вызывает метод класса, то в аргументах функции он передает самого себя(self).<br>
Поэтому необходимо добавить параметр self в функцию<br>
Мы можем создавать переменные в классе. </p>

<p><code>class Person:<br>
    name = "default name"<br>
    second_name = "default second name"<br>
    def say_hi(self):<br>
        print("Hi!")<br>
    def set_second_name(self, name):<br>
        second_name = name</code></p>

<p>Мы можем обратиться к переменной name.<br>
<code>print(person_1.name)</code></p>

<p><code>person_1.name = "new name"</code></p>

<p><code>print(person_1.name)</code></p>

<blockquote>
<p>default name<br>
new name</p>
</blockquote>

<p>Переменные name и second_name статические. Доступ к ним можно также получить и из самого класса.</p>

<p><code>Person.name = "new person name"<br>
person_2 = Person()<br>
print(person_2.name, person_1.name, sep=", ")</code></p>

<blockquote>
<p>new person name, new name</p>
</blockquote>

<p>Мы создали новый объект person_2, но так как мы изменили атрибут name у самого класса, то по умолчанию и у новых объектов меняется этот атрибут.<br>
<code>print(p1.second_name)</code></p>

<p><code>p1.set_second_name("new second name")</code></p>

<p><code>print(p1.second_name)</code></p>

<blockquote>
<p>default second name</p>
</blockquote>

<p>Как видите изменить статический атрибут внутри объекта нельзя.</p>

<p>Но если мы немного измени функцию. То тогда мы успешном сможем изменить переменную second_name.</p>

<p><code>def set_second_name(self, name):</code></p>

<p><code>        self.second_name = name</code></p>

<p>При использования self не обязательно определять статическую переменную.</p>

<p><code>class Person:</code></p>

<p><code>    def set_name(self, newname):</code></p>

<p><code>        self.name = newname</code></p>

<p><code>    def set_second_name(self, new_secondname):</code></p>

<p><code>        self.second_name = new_secondname</code></p>

<p><code>person_1 = Person()</code></p>

<p><code>person_1.set_name("Bill")</code></p>

<p><code>print(person_1.name)</code></p>

<blockquote>
<p>Bill</p>
</blockquote>

## STEP 12

<p><strong>Конструкторы и наследование классов.</strong></p>

<p>В Питоне существуют конструкторы классов. Метод __init__() вызывается каждый раз, когда вы создаете новый объект данного класса.</p>

<p><code>class Person:<br>
     def __init__(self, name, second_name):<br>
         self.name = name<br>
         self.second_name = second_name</code></p>

<p><code>person_1 = Person("Elon", "Musk")<br>
print(person_1.name)</code></p>

<p>Когда мы создаем объект person_1, у него сразу появляется атрибут name и second_name.</p>

<p>В отличии от других языков программирования в питоне нельзя создавать несколько конструкторов, поэтому приходится использовать значения по умолчанию.<br>
<code>def __init__(self, name, second_name, age=None):<br>
         self.name = name<br>
         self.second_name = second_name<br>
         self.age = age</code></p>

<p><code>person_1 = Person("Elon", "Musk")</code></p>

<p><code>print(person_1.name, person_1.age)</code></p>

<p><code>person_2 = Person("Bill", "Gates", 67)</code></p>

<p><code>print(person_2.name, person_2.age)</code></p>

<blockquote>
<p>Elon, None<br>
Bill 67</p>
</blockquote>

<p style="text-align: center;"><strong>Наследование</strong></p>

<p>Бывают ситуации, когда некоторые классы могут брать одни те же свойства другого класса. Вместо того, чтобы повторять один и тот же код, можно сделать класс, который будет наследовать свойства других классов.</p>

<p><code>class Person:<br>
    def __init__(self, name, second_name, age =None):<br>
        self.name = name<br>
        self.second_name = second_name<br>
        self.age = age<br>
    def print_name(self):<br>
        print("Your name is", self.name, "\nYour second name is", self.second_name)</code></p>

<p><code>class PoliceOfficer(Person):<br>
     Job = "Police department"</code></p>

<p>При создании второго класса, в скобках мы указали класс который мы наследуем. Наследуются как и функции, так и атрибуты. </p>

<p><code>person_1 = PoliceOfficer("Chuck", "Noris")</code></p>

<p>Функция __init__ присутствует у класса Person, значит и есть у класса PoliceOfficer/p>

<p>Мы можем переписать функцию __init__</p>

<p><code>class PoliceOfficer(Person):<br>
    Job = "Police department"<br>
    def __init__(self, name, second_name, age, has_gun):<br>
         self.name = name<br>
         self.second_name = second_name<br>
         self.age = age<br>
         self.has_hun = has_gun<br>
    def print_info(self):<br>
         print_name()<br>
         print("Your age is", self.age)<br>
         if self.has_gun == True:<br>
            print("You have gun")<br>
         else:</code></p>

<p><code>           print("You have not gun")</code></p>

<p><code>person_1 = PoliceOfficer("Chuck", "Noris", 67, True)</code></p>

<p>Мы можем вызвать функцию <code>print_name</code></p>

<p><code>person_1.print_name()</code></p>

<blockquote>
<p>Your name is Chuck<br>
Your second name is Noris</p>
</blockquote>

<p>Но если мы попробуем вызвать функцию print_name из самого класса, мы получим ошибку.</p>

<p><code>person_1.print_info()</code></p>

<blockquote>
<p>NameError: name 'print_name' is not defined</p>
</blockquote>

<p>Для того, чтобы обращаться к функциям класса, который мы наследуем используется функция super().</p>

<p><code>def print_info(self):<br>
         <strong>super()</strong>.print_name()<br>
         print("Your age is", self.age)<br>
         if self.has_gun == True:<br>
            print("You have gun")<br>
         else:</code></p>

<p><code>           print("You have not gun")</code></p>

<p><code>person_1.print_info()</code></p>

<blockquote>
<p>Your name is Chuck<br>
Your second name is Noris<br>
Your age is 67<br>
You have gun</p>
</blockquote>

<p>Таким образом функцию __init__ можно было бы сократить</p>

<p><code>class PoliceOfficer(Person):<br>
    Job = "Police department"<br>
    def __init__(self, name, second_name, age, has_gun):<br>
         super().__init__(name, second_name, age)<br>
         self.has_hun = has_gun</code></p>

<p> </p>

<p><strong>Подробнее про классы вы узнаете в модуле про модели..</strong></p>

## STEP 13

<p>Как называется функция, которая запускается сразу же при создании объекта класса?<br>
<br>
<br>
<em>Напишите просто название функции, без скобок и def</em></p>

- `__init__`

## STEP 14

<p>Сколько конструкторов может быть у класса в Питоне?</p>

- 1 ✅
- 2
- Бесконечно много
- Зависит от того, наследуется ли класс или нет


### [Prev lesson](/book/module_0/lesson_2.md)
