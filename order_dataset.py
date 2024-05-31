import random


def order_data():
    name = random.choice(['Анна', 'Мария', 'Саша', 'Сергей'])
    surname = random.choice(['Козлевич', 'Романенко', 'Кузьменко', 'Филипович'])
    address = random.choice(['Питер, Фонтанка', 'Москва 245', 'Чита, улица, дом', 'Бобруйск'])
    phone = random.choice(['12345678900', '11111111111', '777777777777', '000000000000'])
    color = random.choice(['black', 'grey'])
    comment = random.choice(['', 'срочно', 'важно', 'красиво'])
    return name, surname, address, phone, color, comment
