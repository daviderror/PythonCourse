import doctest
class Furniture:
    def __init__(self, material: str, dimensions: tuple):
        """
        Инициализация объекта Furniture.

        :param material: Материал, из которого изготовлена мебель. Не может быть пустым.
        :param dimensions: Размеры мебели в формате (ширина, высота, глубина).
                           Все значения должны быть положительными.

        :raises ValueError: Если материал пустой или размеры некорректные.

        >>> chair = Furniture("Дерево", (50, 100, 50))
        >>> chair.material
        'Дерево'
        """
        if not material:
            raise ValueError("Материал не может быть пустым.")
        if any(d <= 0 for d in dimensions):
            raise ValueError("Все размеры должны быть положительными.")

        self.material = material
        self.dimensions = dimensions

    def assemble(self) -> None:
        """
        Собрать мебель.

        :return: None

        >>> chair = Furniture("Дерево", (50, 100, 50))
        >>> chair.assemble()
        """
        ...

    def disassemble(self) -> None:
        """
        Разобрать мебель.

        :return: None

        >>> chair = Furniture("Дерево", (50, 100, 50))
        >>> chair.disassemble()
        """
        ...


class Tree:
    def __init__(self, species: str, age: int):
        """
        Инициализация объекта Tree.

        :param species: Вид дерева. Не может быть пустым.
        :param age: Возраст дерева в годах. Должен быть неотрицательным.

        :raises ValueError: Если вид пустой или возраст отрицательный.

        >>> oak = Tree("Дуб", 50)
        >>> oak.species
        'Дуб'
        """
        if not species:
            raise ValueError("Вид дерева не может быть пустым.")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным.")

        self.species = species
        self.age = age

    def grow(self, years: int) -> None:
        """
        Увеличить возраст дерева.

        :param years: Количество лет, на которое нужно увеличить возраст. Должно быть положительным.

        :return: None

        >>> oak = Tree("Дуб", 50)
        >>> oak.grow(5)
        """
        ...

    def shed_leaves(self) -> None:
        """
        Сбросить листья дерева.

        :return: None

        >>> oak = Tree("Дуб", 50)
        >>> oak.shed_leaves()
        """
        ...


class SocialMedia:
    def __init__(self, name: str, user_count: int):
        """
        Инициализация объекта SocialMedia.

        :param name: Название социальной сети. Не может быть пустым.
        :param user_count: Количество пользователей. Должно быть неотрицательным.

        :raises ValueError: Если название пустое или количество пользователей отрицательное.

        >>> fb = SocialMedia("Facebook", 2000000000)
        >>> fb.name
        'Facebook'
        """
        if not name:
            raise ValueError("Название социальной сети не может быть пустым.")
        if user_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")

        self.name = name
        self.user_count = user_count

    def add_user(self) -> None:
        """
        Добавить нового пользователя.

        :return: None

        >>> fb = SocialMedia("Facebook", 2000000000)
        >>> fb.add_user()
        """
        ...

    def remove_user(self) -> None:
        """
        Удалить пользователя.

        :return: None

        >>> fb = SocialMedia("Facebook", 2000000000)
        >>> fb.remove_user()
        """
        ...
