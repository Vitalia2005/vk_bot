from func import *

user = User(221787814)
user_without_town = User(293219277)


def test1_pp():
    assert get_weather('Москва') == pp('Погода Москва')


def test2_pp():
    assert 'Такого города не существует' == pp('Погода ываваываыфва')


def test3_pogoda():
    assert 'Выберите город на клавиатуре' == pogoda(user)[1]
    assert (None, 'Введите город') == pogoda(user_without_town)


def test4_pogoda_drygoi():
    assert 'Такого города не существует' == send_weather(user, 'фывуцукцук')
    assert get_weather('Москва') == send_weather(user, 'Москва')

def test5_pogoda_na_period():
    assert 'Выберите город' == pogoda_na_period(user)[1]
    assert (None, 'Введите город') == pogoda_na_period(user_without_town)

def test6_period_drygoi():
    assert 'Выберите период' == period_drygoi_button(user, 'Москва')[1]
    assert 'Такого города не существует' == period_drygoi_button(user, 'qweqweqweqweqweqweqw')[1]
    assert 'Выберите период' == period_drygoi_button(user_without_town, 'Москва')[1]
    assert 'Такого города не существует' == period_drygoi_button(user_without_town, 'qweqweqweqweqweqweqw')[1]

def test7_choose_period():
    user.per_city = 'Москва'
    assert ('\n').join(get_many_weather('Москва')[0:3]) == choose_period(user, '3 дня')[1]
    assert ('\n').join(get_many_weather('Москва')[0:7]) == choose_period(user, '7 дней')[1]
    assert (None, 'Введите число дней (макс. 10)') == choose_period(user, 'Другой')
    assert 'Неверный период' == choose_period(user, 'dqdqweqweqw')[1]
    user_without_town.per_city = 'Москва'
    assert ('\n').join(get_many_weather('Москва')[0:3]) == choose_period(user_without_town, '3 дня')[1]
    assert ('\n').join(get_many_weather('Москва')[0:7]) == choose_period(user_without_town, '7 дней')[1]
    assert (None, 'Введите число дней (макс. 10)') == choose_period(user_without_town, 'Другой')
    assert 'Неверный период' == choose_period(user_without_town, 'dqdqweqweqw')[1]


def test8_drygoi_period():
    assert 'Это не число' == drygoi_period(user, '1das')[1]
    assert 'Число должно быть от 1 до 10' == drygoi_period(user, 11)[1]
    user.per_city = 'Москва'
    assert ('\n').join(get_many_weather('Москва')[0:5]) == drygoi_period(user, 5)[1]
    user.per_city = 'skffegjrguewg'
    assert 'Такого города не существует' == drygoi_period(user, 5)[1]

    assert 'Это не число' == drygoi_period(user_without_town, '1das')[1]
    assert 'Число должно быть от 1 до 10' == drygoi_period(user_without_town, 11)[1]
    user_without_town.per_city = 'Москва'
    assert ('\n').join(get_many_weather('Москва')[0:5]) == drygoi_period(user_without_town, 5)[1]
    user_without_town.per_city = 'skffegjrguewg'
    assert 'Такого города не существует' == drygoi_period(user_without_town, 5)[1]

def test9_timer():
    assert 'Выберите город' == timer_vr(user, '7:00')[1] and timer_vr(user, '7:00')[0]
    assert 'Выберите город' == timer_vr(user, '12:00')[1] and timer_vr(user, '12:00')[0]
    assert (None, 'Введите город') == timer_vr(user_without_town, '7:00')
    assert (None, 'Введите город') == timer_vr(user_without_town, '12:00')
    assert (None, 'Введите время в формате чч:мм в московском часовом поясе') == timer_vr(user, 'Другой')
    assert 'Неверный формат данных' == timer_vr(user, 'qwfwqr')[1]


def test10_timer_city():
    assert 'Выберите город' == timer_city(user, '13:00')[1]
    assert (None, 'Введите город') == timer_city(user_without_town, '14:00')
    assert 'Ошибка. Неверный формат.' == timer_city(user, 'sjjasdoa')[1]

