# Выведите все праздники для России на 2024 год

import requests

DICT_HOLIDAY = dict[str, str]
LIST_HOLIDAY = list[DICT_HOLIDAY]


def get_list_of_available_holiday() -> LIST_HOLIDAY:
    url = 'https://date.nager.at/api/v3/PublicHolidays/2024/RU'
    res = requests.get(url=url).json()
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
