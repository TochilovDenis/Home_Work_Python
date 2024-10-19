# Выведите все праздники для России на 2024 год

import requests

DICT_HOLIDAY = dict[str, str]
LIST_HOLIDAY = list[DICT_HOLIDAY]


def get_list_of_available_holiday() -> LIST_HOLIDAY:
    url = 'https://date.nager.at/api/v3/PublicHolidays/2024/RU'
    payload: dict[str, str] = {
        "date": "",             # дата праздника
        "localName": "",        # название праздника зависит от кода страны
        "name": "",             # название праздника на англ
        "countryCode": "RU",    # код страны
        "fixed": False,         # фиксированный
        "global": True,         # глобальный
        "counties": 0,          # округа null
        "launchYear": 0,        # год запуска null
        "types": ["Public"] }   # виды
    res = requests.get(url=url, params=payload).json()
    return res


def get_dict_of_available_holiday(holidays: LIST_HOLIDAY) -> DICT_HOLIDAY:
    result: DICT_HOLIDAY = dict()
    for holiday in holidays:
        result[holiday['date']] = f'| {holiday['localName']} | {holiday['name']}'

    return result


def main() -> None:
    list_of_holiday = get_list_of_available_holiday()
    dict_of_holiday = get_dict_of_available_holiday(list_of_holiday)

    for date, name in dict_of_holiday.items():
        print(date, name)


if __name__ == '__main__':
    main()
