import math

Pi = 3.14  # внешние константы НЕ переносятся в case, там создадутся новые переменные с таким же именем


def pi_func(x):
    match x:
        case pi if pi == Pi:  # нельзя передать одну переменную, будет аналогично wildcard. гард должен выполнить проверку чтобы работало.
            # создастся новая переменная pi и в нее запишется переданное значение x. затем гард сравнит ее со значением pi из глобальной области
            print(f'1.1) {pi}')
        case math.pi:  # если вводятся имена с точкой, то будет не создание новой переменной, а поиск в верхних областях видимости и модулях
            print(f'1.2) {x:=.5f}')
        case _:
            print(f'1.3) Wrong value {x}')

# if __name__ == '__main__':
#     pi_func(Pi)
#     pi_func(math.pi)
#     pi_func(3.141)

    # ------------------------------------------------------------------------------------------------------------------------------------------------


def mail_validation(s):
    s = s.lower()
    new_s = s.split('@')[0], s.split('@')[1].split('.')[0], s.split('.')[-1]
    match new_s:
        case name, 'yandex', 'ru' | 'com' | 'ua' | 'kz' | 'by' as domain if len(name) > 0:
            return f'2.1) {name}@ya.{domain}'
        case name, 'ya' | 'yandex-team', 'ru' if len(name) > 0:
            return f'2.2) Name {s} is TRUE'
        case _:
            return f'2.3) Wrong name for {s}!'

# if __name__ == '__main__':
    # print(mail_validation('Yandex@yandex.ua'))
    # print(mail_validation('User.yandex@ya.ru'))
    # print(mail_validation('User@yandex-team.com'))

    # ------------------------------------------------------------------------------------------------------------------------------------------------


def calculate(x: int | float, y: int | float, operator: str) -> str | int | float:  # pattern matching - сопоставление шаблонов
    match operator:  # похоже на switch case из других языков. это механизм проверки данных, распаковки данных и управления потоком выполнения.
        case '+':  # при совпадении одного шаблона остальные уже не проверяются. пустых блоков быть не должно, хотя бы pass
            _ = x + y  # нет return, поэтому переход в основной return. остальные шаблоны не проверяются если этот возвращает True
        case '-':
            _ = x - y
        case _:  # wildcard, выполняется если не совпали шаблоны выше
            return '3.2) Unknown operation'
    return f'3.1) {_}'  # выполняется если нет return в case, который вернул True. например если вместо return вызывается print, прописан pass.
    # сюда попадают переменные из УСПЕШНОГО case, условия в котором вернули True, тогда сохранились переменные из этого case

# if __name__ == '__main__':
    # print(calculate(3, 5, '-'))
    # print(calculate(2.4, 1.1, '+'))
    # print(calculate(6, 2, '*'))

    # ------------------------------------------------------------------------------------------------------------------------------------------------


def run_action(user_input: str) -> None:
    match user_input.lower().split():
        case 'left' | 'right' | 'top' | 'bottom' as action, value:  # с помощью as можно сохранить любое из значений, перечисленных через ИЛИ
            print(f'4.1) Go to {action} to {value}')
        case 'shoot', *coordinates:  # запакованные значения возвращаются в виде списка, из которого можно брать индексы
            print(f'4.2) Shoot by coordinates {coordinates[-1]}')
        case 'quit', :  # если передается не строка, а список (есть .split()), то проверка 'quit' вернет 'False', так как проверяется не первое
            # значение, а весь список сразу. либо нужно убрать .split() и передавать строку из одного слова, либо после 'quit' поставить запятую
            # при этом _ ставить не нужно, так как передается список только с одним значением
            print('4.3) Exit')
        case _:
            print('4.4) Wrong command')


# if __name__ == '__main__':
#     run_action('left 100')
#     run_action('shoot 100 200 3 444')
#     run_action('quit')
#     run_action('left100')

    # ------------------------------------------------------------------------------------------------------------------------------------------------


class UserInput:
    __match_args__ = ('action', 'value')  # если прописан этот метод, то при проверке в case атрибуты будут проверяться именно в таком порядке.

    # тогда проверку можно заменить на "case UserInput('left' | 'right' as action, value):"
    # если атрибут всего один, то для создания кортеже нужна запятая, например ('action',)
    def __init__(self, action: str, value: int):
        self.action = action
        self.value = value


def run(user_input: UserInput | dict) -> None:  # ожидается объект класса или словарь. возвращает None, так как нет return
    match user_input:
        case UserInput(value=value, action='left' | 'right' as action):  # проверка, что пришел объект класса UserInput с атрибутами action и value.
            # расстояние сохраняется в value, а направление проверяется и сохраняется в action. при этом новый экземпляр НЕ создается.
            # это разные value. первое это название атрибута экземпляра класса. второе - это переменная для сохранения и передачи значения дальше
            print(f'5.1) Moving {action} on {value} px')
        case UserInput('left' | 'right' | 'forward' as action, value):  # если прописан метод __match_args__, то при проверке в case
            # атрибуты будут проверяться именно в таком порядке. указывать их названия action и value уже не нужно
            print(f'5.2) Moving {action} on {value} px')
        case {'action': 'left' | 'right' as action, 'value': value}:  # проверка, что пришел словарь, в котором есть определенные ключи
            # проверяется направление и сохраняется в action. расстояние сохраняется в value.
            print(f'5.3) Moving {action} on {value} px')
        case _:  # в атрибутах пришедшего класса нет 'top' поэтому вызывается wildcard
            print('5.4) Wrong input')


input1 = UserInput('left', 150)
input2 = UserInput('forward', 666)
input3 = {'action': 'right', 'value': 300}
input4 = UserInput('top', 50)


# if __name__ == '__main__':
#     run(input1)
#     run(input2)
#     run(input3)
#     run(input4)

# ------------------------------------------------------------------------------------------------------------------------------------------------


def parse_response(value):  # функция проверки ответа от сети, их обработка
    match value:
        case {'key': 1000, **rest}:  # в словаре должен быть ключ 'key' со значением 1000 и какие-то еще значения,
            # которые будут распакованы в словарь rest. из него уже выводится значение ключа 'id'.
            # нельзя использовать '**_', это переменная, а не словарь. для распаковки словаря нужно использовать например rest (так в документации).
            # то есть выводим 'id' только в том случае, если в исходном словаре есть еще и ключ 'key'
            return rest['id']
        case ('error', message) | ('error', message, *_):  # ждем или последовательность из 2 элементов, первый это 'error', второй это сообщение.
            # или последовательность из любого числа элементов, первый из которых 'error', второй - сообщение. остальные элементы неважны.
            # ВАЖНО при использовании ИЛИ (|) использовать одинаковые имена в шаблонах. первый шаблон в данном примере не важен, его можно удалить.
            raise ValueError(message)
        case {'meta': val, **rest} if not rest:  # приходит словарь с ключом 'meta' и любым числом других ключей. они запаковываются в rest
            # гард выполняется только если rest пустой, то есть в исходном словаре должен быть только указанный ключ 'meta'
            return val['id']
        case {'meta': {'code': _, 'error': error}, 'info': [{'allowed': allowed}, _]}:  # на входе mapping, например JSON
            # в исходном словаре должен быть ключ 'meta' в значении которого есть другой словарь.
            # в нем должен быть ключ 'code', значение которого должно игнорироваться и ключ 'error' со значением в виде переменной error.
            # а также ключ 'info' со значением в виде списка, на первом месте в котором стоит словарь с ключом 'allowed' и значением allowed.
            # в списке должно быть еще ровно один объект. если заменить на '*_', то число объектов может быть любым, или их может вообще не быть
            return f'{error}, {allowed}'
        case (set() as x, _) if len(x) == 2:  # должна прийти последовательность из 2 элементов, первый их которых должен быть множеством.
            # второй элемент игнорируется. после проверки на то, что первый элемент именно set, он присваивается в переменную x.
            # проверку можно заменить на set(x), без использования as x, результат будет таким же в match case.
            # гард проверяет, что в этом множестве ровно два элемента
            return max(x)
        case _:
            raise ValueError(f'Unknown value: {value}')


# if __name__ == '__main__':
#     a = {'key': 1000, 'id': 999}
#     b = ['error', 'Slow network connection']
#     c = {'meta': {'id': 999}}
#     d = {'meta': {'code': 200, 'error': 'no'}, 'info': [{'allowed': 'yes'}, 300]}
#     e = ({10, 11}, 5)
#     print('6)', parse_response(d))

# ------------------------------------------------------------------------------------------------------------------------------------------------


def check(value: tuple):
    match value:
        case name, _, salary if name in ('John', 'Anna'):  # последовательность из трех элементов, второй игнорируется.
            # гард проверяет наличие имени name в списке разрешенных имен
            return salary
        case 'Helen', age, _:  # из кортежа из 3 элементов, первый из которых равен 'Helen' вернуть второй элемент age
            return age
        case _, _, _, _, str(something):  # в последовательности из 5 значений первые 4 игнорируются, а последнее должно быть строкой
            return f'c is {something}'
        case *_, some if len(value) == 6:  # в последовательности из любого числа значений все кроме последнего игнорируются.
            # при этом гард проверяет, чтобы в последовательности было ровно 6 элементов
            return f'd is {some}'
        case tuple():  # приходит кортеж, не подходящий под все проверки выше
            return f'Unknown content {value}'
        case _:  # приходит не кортеж
            raise ValueError('Expected a tuple!')


# if __name__ == '__main__':
#     a = ('Anna', 22, 100_000)
#     b = ('Helen', 21, 100_000)
#     c = (1, 2, 3, 4, 'Something')
#     d = (1, 2, 3, 4, 5, 'Something else')
#     print('7)', check(c))

# ------------------------------------------------------------------------------------------------------------------------------------------------


def names(value: str | list | tuple | dict) -> str:
    match value:
        case name, surname:  # для объектов класса collections, последовательности (list, tuple), принимает СТРОГОЕ число аргументов
            pass
        case {'name': name, 'surname': surname} if len(value) == 2:  # для объектов класса mapping (dict), с ключами и значениями.
            # принимает ЛЮБОЕ число аргументов, проверяет чтобы среди них были искомые ключи. гард if нужен если должно быть строго 2 ключа.
            # гард (ограничитель) проверяется если остальной блок case вернул True. без блока if последний assert прошел бы без вывода 'Error'
            pass
        case str() if len(lst := value.split()) == 2:  # проверка типа, аналог isinstance(value, str), если True, то проверяется гард.
            # если гард возвращает False, то есть если не 2 слова в values, то весь case возвращает False
            name, surname = lst
        case _:  # wildcard или любой другой набор символов
            return 'Error'
    return f'Name: {name}, surname: {surname}'  # выполняется если нет return в case, который вернул True.
    # например если вместо return вызывается print или pass.
    # сюда попадают переменные из УСПЕШНОГО case, условия в котором вернули True, тогда сохранились переменные из этого case


assert names(('John', 'Doe')) == 'Name: John, surname: Doe'
assert names(['John', 'Doe']) == 'Name: John, surname: Doe'
assert names({'name': 'John',
              'surname': 'Doe'
              }) == 'Name: John, surname: Doe'
assert names('John Doe') == 'Name: John, surname: Doe'
assert names(['Doe']) == 'Error'
assert names(('John', 'Doe', 'Doe')) == 'Error'
assert names({'a': 'John', 'b': 'Doe'}) == 'Error'
assert names('John Doe Doe') == 'Error'
assert names({'surname': 'Doe',
              'name': 'John',
              'salary': 100_000}) == 'Error'


# if __name__ == '__main__':
#     print('8)', names('John Doe'))

# ------------------------------------------------------------------------------------------------------------------------------------------------


def request_validation(request):
    match request:
        case {'url': str() as url, 'method': str(method)} if len(request) < 3:  # проверка, что приходит словарь, содержащий менее 3 ключей.
            # ключи должны быть именно url и method с любыми значениями. но значения должны быть в формате строки (два варианта проверки).
            # наличие или отсутствие других ключей не проверяется. значения заносятся в соответствующие переменные
            print(f'9.1) Request URL: {url}, method: {method}')
        case {'url': url, 'method': method, 'timeout': 1000 | 2000 as timeout}:  # аналогично, но без проверки на тип данных и длины словаря.
            #  дополнительно проверяется значение ключа timeout, которое должно быть равно 1000 или 2000
            print(f'9.2) Request URL: {url}, method: {method}, timeout: {timeout}')
        case {'timeout': 100 as timeout, **rest} | {'timeout': 200 as timeout, **rest}:  # проверяется наличие ключа timeout.
            # аналогичная проверка значения ключа timeout (100 или 200), но через два отдельных шаблона. переменные в шаблонах должны совпадать!
            # все остальные ключи запаковываются в словарь rest. при выводе словарь распаковывается через генератор списков
            print(f'9.3) Timeout is {timeout} for', *[f'{i.upper()}: {j}' for i, j in rest.items() if i == 'url'])
        case {'url': url, 'method': method, **rest} if not rest:  # проверка, что приходит словарь, содержащий только указанные ключи.
            #  гард проверяет, что словарь, в которые запаковываются все остальные ключи, пустой
            print(f'9.4) Request URL: {url}, method: {method}')
        case {'url': url, **rest} if len(rest) > 2:  # проверяется наличие ключа url остальные ключи запаковываются в словарь.
            #  гард проверяет, что в запакованном словаре должны быть не менее 2 ключей. перед выводом словарь распаковывается через генератор списков
            temp = f'9.5) Request URL: {url}, ', *[f'{i}: {j}, ' for i, j in rest.items()]
            print(''.join(temp[:-1]), temp[-1][:-2], sep='')  # временная переменная нужна только для того, чтобы убрать запятую в конце при выводе
        case {'id': _, 'data': [_, {'login': user}, *_]}:  # проверка, что пришел словарь, в котором есть ключ data с любым значением,
            # ключ data с вложенным списком. в нем на втором месте лежит вложенный словарь с ключом login, значение которого сохраняется в переменную.
            # остальные значения вложенного и исходного словарей не имеют значения. для списка важен порядок значений, но не их общее количество
            print(f'9.6) Username is {user}')
        case set(keys) if len(keys) == 3:  # проверка, что пришло множество из 3 значений.
            # фигурными скобками проверить не получится, так как это будет проверка на словарь dict, а не множество set
            print(f'9.7) {keys}')
        case _:
            print(f'9.8) Wrong request: {request}')


if __name__ == '__main__':
    request_validation({'url': 'https://ya.ru', 'method': 'GET'})
    request_validation({'url': 'https://ya.ru', 'method': None, 'timeout': 1000})
    request_validation({'url': 'https://ya.ru', 'method': None, 'timeout': 200})
    request_validation({'url': 'https://ya.ru', 'method': None})
    request_validation({'url': 'https://ya.ru', 'method': None, 'timeout': 10, 'date': None})
    request_validation({'id': 1, 'method': None, 'data': [2023, {'url': 'https://ya.ru', 'login': 'Login'}], 'timeout': 10})
    request_validation({'mail', 'login', 'password'})
