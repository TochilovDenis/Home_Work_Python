from datetime import datetime, date


def parse_date(date_string: str) -> date:
    format_date: list[str] = [
        '%Y-%m-%d',  # стандартный формат
        '%d/%m/%Y',  # стандартный формат для Великобритании и некоторых других англоязычных стран.
        '%Y.%m.%d'   # Используется в некоторых европейских странах.
    ]

    for fmt in format_date:
        try:
            return datetime.strptime(date_string, fmt)

            # dt = datetime.strptime(date_string, fmt)
            # return date.fromisoformat(dt.strftime(fmt))
        except ValueError:
            pass

    # If no valid format is found, raise an exception
    raise ValueError(f"Unable to parse date: {date_string}")


# Example usage
try:
    birth_date: date = parse_date("2024-02-11")
    print(f"Parsed date: {birth_date}")
except ValueError as e:
    print(e)