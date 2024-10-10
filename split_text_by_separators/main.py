# Функция для разделения текста по заданным разделителям
def split_text_by_separators(text: str, seps: list[str]) -> list[str]:
    # Инициализируем список результатов с пустым элементом
    result: list[str] = ['']
    # Флаг для отслеживания ожидания разделителя
    waiting_for_separator: bool = True
    # Проходим по каждому символу в тексте
    for symbol in text:
        # Если ожидаем разделитель
        if waiting_for_separator:
            # Если символ является разделителем, устанавливаем флаг в False
            if symbol in seps:
                waiting_for_separator = False
        else:
            # Если текущий символ не является разделителем и не пробелом
            if not symbol in seps and symbol != ' ':
                # Добавляем новый пустой элемент в список результатов и устанавливаем флаг в True
                result.append('')
                waiting_for_separator = True
        # Добавляем символ к последнему элементу списка результатов
        result[-1] += symbol
    # Возвращаем список результатов после обработки всей строки
    return result


if __name__ == "__main__":
    # Определяем списка разделителей
    separators: list[str] = [';', '.', '!', '?']
    # Тестовая строка для разбиения
    test_string = "Что?.. Да! Вышел корень из тумана; Вынул ножик из кармана. Раз, два, всё?.."
    # Вызываем функцию с параметрами и выводим результат
    print(split_text_by_separators(test_string, separators))
