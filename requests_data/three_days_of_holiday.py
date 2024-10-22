# Выведите три ближайших праздника и через сколько дней они будут.

import requests                # Импорт необходимого модуля для отправки HTTP-запросов
from datetime import datetime  # Импорт классов datetime из модуля datetime для работы с датами и временем

# Определение типов для словаря праздников и списка праздников:
DICT_HOLIDAY = dict[str, str]      # Тип словаря для хранения информации о празднике
LIST_HOLIDAY = list[DICT_HOLIDAY]  # Тип списка для хранения словарей праздников

CURRENT_DATA: datetime.date = datetime.now().date() # Получение текущей даты


def get_list_of_available_holiday() -> LIST_HOLIDAY:
    """
    Получает список доступных праздников из API.
    Возвращает список словарей, где каждый словарь содержит информацию о празднике.
    """
    url: str = 'https://date.nager.at/api/v3/NextPublicHolidaysWorldwide'  # URL API для получения праздников
    res: list = requests.get(url=url).json()    # Отправляем GET запрос к API и получаем ответ в формате JSON
    return res  # Возвращаем список праздников из ответа API


def get_dict_of_available_three_days_of_holiday(holidays: LIST_HOLIDAY) -> DICT_HOLIDAY:
    """
    Создает словарь с тремя ближайшими праздниками.

    Параметры:
    holidays (LIST_HOLIDAY): Список всех доступных праздников.
    Возвращает словарь, где ключ - название праздника, значение - информация о празднике.
    """
    print(f"Текущая дата: {CURRENT_DATA}")

    result: DICT_HOLIDAY = {}  # Инициализируем пустой словарь для хранения результатов
    count: int = 0  # Счетчик для отслеживания количества найденных праздников

    # Проходим по каждому празднику в списке
    for holiday in holidays:
        # Преобразуем строку даты в объект datetime и извлекаем только дату
        holiday_date: datetime.date = datetime.strptime(holiday['date'], '%Y-%m-%d').date()
        # Вычисляем количество дней до праздника
        days_until: int = (holiday_date - CURRENT_DATA).days

        # Проверяем, не прошел ли праздник
        if days_until >= 0:
            # Добавляем праздник в результат, если он еще не прошел
            result[holiday['name']] = f"через {days_until} дней ({holiday['date']}) | Страна: {holiday['countryCode']}"
            count += 1

            # Если нашли три праздника, прерываем цикл
            if count == 3:
                break

    return result   # Возвращаем словарь с тремя ближайшими праздниками


def main() -> None:
    """
    Вызывает вспомогательные функции для получения списка праздников и создания словаря с тремя ближайшими праздниками,
    а затем выводит результаты.
    """
    list_of_holiday: LIST_HOLIDAY = get_list_of_available_holiday()
    dict_of_holiday: DICT_HOLIDAY = get_dict_of_available_three_days_of_holiday(list_of_holiday)

    print("Три ближайших праздника:")
    for name, details in dict_of_holiday.items():
        print(f" - {name} | {details}")



if __name__ == '__main__':
    main()
