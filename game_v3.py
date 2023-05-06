# region imports
import numpy as np
from benchmark import score_game
# endregion


# поиск заданного числа с применением сужающихся интервалов
def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0

    # верхняя граница загаданного числа
    max_num = 100

    predict = np.random.randint(1, max_num + 1)

    p = predict

    step = (max_num if predict < number else predict) // 2

    # загаданное число лежит в диапазоне от 0 до predict
    # или от predict до max_num;
    # возьмем predict за точку отсчета и будем двигаться от него с шагом step,
    # постепенно уменьшая шаг
    while number != p:
        count += 1
        # добавить или отнять шаг от предполагаемого числа
        # в зависимости от того, больше оно искомого или меньше
        dir = -1 if p > number else 1
        p += dir*step
        # с каждым циклом сужаем диапазон поиска вдвое
        step = step // 2 if step // 2 != 0 else 1
    return count


if __name__ == "__main__":
    score_game(game_core_v3)
