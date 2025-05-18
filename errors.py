class CourierErrors:
    REQUIRED_FIELDS_MISSING = 'Недостаточно данных для создания учетной записи'
    LOGIN_ALREADY_EXISTS = 'Этот логин уже используется. Попробуйте другой.'
    COURIER_NOT_FOUND = 'Курьера с таким id нет.'
    LOGIN_REQUIRED_FIELDS_MISSING = 'Недостаточно данных для входа'
    ACCOUNT_NOT_FOUND = 'Учетная запись не найдена'

class OrderErrors:
    REQUIRED_FIELDS_MISSING = 'Недостаточно данных для поиска'
    COURIER_NOT_FOUND = 'Курьера с таким id не существует'
    ORDER_NOT_FOUND = 'Заказ не найден'
    INVALID_ORDER_ID = 'Заказа с таким id не существует'
