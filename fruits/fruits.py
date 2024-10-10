from random import choice, randint


class Fruits:
    def __init__(self, name, weight, color, height, taste):
        self.name = name
        self.weight = weight
        self.color = color
        self.height = height
        self.taste = taste

    def __str__(self):
        return (f"Название: {self.name} "
                f"| Вес: {self.weight} гр. "
                f"| Цвет: {self.color} "
                f"| Высота: {self.height} см."
                f"| Вкус: {self.taste}")


class BasketFruits:
    def __init__(self):
        self.fruits = list()

    def add_fruit(self, fruit):
        self.fruits.append(fruit)

    def __str__(self):
        total_weight = 0
        for fruit in self.fruits:
            total_weight += fruit.weight
        # total_weight = sum(fruit.weight for fruit in self.fruits)
        return f"В корзине {len(self.fruits)} фруктов общей массой {total_weight:.2f} кг"


NAMES = ["Яблоко", "Банан", "Апельсин", "Груша", "Киви"]
COLOR = ["Зеленый", "Желтый", "Оранжевый", "Красный", "Синий"]
TASTE = ["Сладкий", "Горький", "Кислый", "Отвратительный"]

def generator_random_fruits():
    name = choice(NAMES)
    weight = randint(100, 500)
    color = choice(COLOR)
    height = randint(1, 10)
    taste = choice(TASTE)

    return Fruits(name, weight, color, height, taste)


if __name__ == '__main__':
    basket1 = BasketFruits()
    basket2 = BasketFruits()

    for _ in range(15):
        fruits = generator_random_fruits()
        basket1.add_fruit(fruits)
    print("Корзина 1:")
    print(basket1)

    for _ in range(15):
        fruits = generator_random_fruits()
        basket2.add_fruit(fruits)
    print("\nКорзина 2:")
    print(basket2)

