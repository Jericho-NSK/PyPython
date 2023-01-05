string = 'DFn.dex@yandex-team.ru'


def enter(s):
    s = s.lower()
    new_s = s.split('@')[0], s.split('@')[1].split('.')[0], s.split('.')[-1]
    match new_s:
        case name, 'yandex' | 'yandex-team', 'ru' | 'com' | 'ua' | 'kz' | 'by' as domain if len(name) > 0:
            return f'{name}@ya.{domain}'
        case name, 'ya' | 'yandex-team', 'ru' if len(name) > 0:
            pass
        case _:
            return f'Wrong name for {s}'
    return f'Name {s} is TRUE'


print(enter(string))
