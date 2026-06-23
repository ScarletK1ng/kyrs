<b>Блок-схема:</b> `scheme.drawio`

## Описание объектных моделей кода
### Класс `PositiveElementsAnalyzer`

Класс предназначен для анализа одномерного массива и поиска суммы и количества положительных элементов

<b>Поля класса</b>
<table>
    <thead>
        <tr>
            <th>Поле</th>
            <th>Тип</th>
            <th>Описание</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>array</code></td>
            <td><code>list[int]</code></td>
            <td>Одномерный массив чисел</td>
        </tr>
        <tr>
            <td><code>sum_positive</code></td>
            <td><code>int</code></td>
            <td>Сумма положительных элементов массива</td>
        </tr>
        <tr>
            <td><code>count_positive</code></td>
            <td><code>int</code></td>
            <td>Количество положительных элементов массива</td>
        </tr>
    </tbody>
</table>

<b>Метод класса</b>
<table>
    <thead>
        <tr>
            <th>Метод</th>
            <th>Описание</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>__init__(self, array)</code></td>
            <td>Конструктор класса. Получает массив и инициализирует сумму и счётчик нулями</td>
        </tr>
        <tr>
            <td><code>analyze(self)</code></td>
            <td>Проходит по массиву и считает сумму и количество положительных элементов</td>
        </tr>
        <tr>
            <td><code>get_result(self)</code></td>
            <td>Возвращает результат анализа: сумму и количество положительных элементов</td>
        </tr>
    </tbody>
</table>

## Тестовые примеры исходных данных

<table>
    <thead>
        <tr>
            <th>№</th>
            <th>Исходные данные</th>
            <th>Ожидаемая сумма</th>
            <th>Ожидаемое количество</th>
            <th>Что проверяется</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td><code>N = 5, A = [1, -2, 3, 0, 4]</code></td>
            <td><code>8</code></td>
            <td><code>3</code></td>
            <td>Смешанный массив</td>
        </tr>
        <tr>
            <td>2</td>
            <td><code>N = 4, A = [-1, -5, 0, -3]</code></td>
            <td><code>0</code></td>
            <td><code>0</code></td>
            <td>Нету положительных элементов</td>
        </tr>
        <tr>
            <td>3</td>
            <td><code>N = 3, A = [2, 7, 10]</code></td>
            <td><code>19</code></td>
            <td><code>3</code></td>
            <td>Только положительные элементы</td>
        </tr>
        <tr>
            <td>4</td>
            <td><code>N = 5, A = [0, 0, 0, 0, 0]</code></td>
            <td><code>0</code></td>
            <td><code>0</code></td>
            <td>Только нулевые элементы</td>
        </tr>
        <tr>
            <td>5</td>
            <td><code>N = 1, A = [9]</code></td>
            <td><code>9</code></td>
            <td><code>1</code></td>
            <td>Один положительный элемент</td>
        </tr>
        <tr>
            <td>6</td>
            <td><code>N = 1, A = [-9]</code></td>
            <td><code>0</code></td>
            <td><code>0</code></td>
            <td>Один отрицательный элемент</td>
        </tr>
    </tbody>
</table>
<b>Блок-схема:</b> `scheme.drawio`

## Описание объектных моделей кода
### Класс `PositiveElementsAnalyzer`

Класс предназначен для анализа одномерного массива и поиска суммы и количества положительных элементов

<b>Поля класса</b>
<table>
    <thead>
        <tr>
            <th>Поле</th>
            <th>Тип</th>
            <th>Описание</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>array</code></td>
            <td><code>list[int]</code></td>
            <td>Одномерный массив чисел</td>
        </tr>
        <tr>
            <td><code>sum_positive</code></td>
            <td><code>int</code></td>
            <td>Сумма положительных элементов массива</td>
        </tr>
        <tr>
            <td><code>count_positive</code></td>
            <td><code>int</code></td>
            <td>Количество положительных элементов массива</td>
        </tr>
    </tbody>
</table>

<b>Метод класса</b>
<table>
    <thead>
        <tr>
            <th>Метод</th>
            <th>Описание</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>__init__(self, array)</code></td>
            <td>Конструктор класса. Получает массив и инициализирует сумму и счётчик нулями</td>
        </tr>
        <tr>
            <td><code>analyze(self)</code></td>
            <td>Проходит по массиву и считает сумму и количество положительных элементов</td>
        </tr>
        <tr>
            <td><code>get_result(self)</code></td>
            <td>Возвращает результат анализа: сумму и количество положительных элементов</td>
        </tr>
    </tbody>
</table>

## Тестовые примеры исходных данных

<table>
    <thead>
        <tr>
            <th>№</th>
            <th>Исходные данные</th>
            <th>Ожидаемая сумма</th>
            <th>Ожидаемое количество</th>
            <th>Что проверяется</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td><code>N = 5, A = [1, -2, 3, 0, 4]</code></td>
            <td><code>8</code></td>
            <td><code>3</code></td>
            <td>Смешанный массив</td>
        </tr>
        <tr>
            <td>2</td>
            <td><code>N = 4, A = [-1, -5, 0, -3]</code></td>
            <td><code>0</code></td>
            <td><code>0</code></td>
            <td>Нету положительных элементов</td>
        </tr>
        <tr>
            <td>3</td>
            <td><code>N = 3, A = [2, 7, 10]</code></td>
            <td><code>19</code></td>
            <td><code>3</code></td>
            <td>Только положительные элементы</td>
        </tr>
        <tr>
            <td>4</td>
            <td><code>N = 5, A = [0, 0, 0, 0, 0]</code></td>
            <td><code>0</code></td>
            <td><code>0</code></td>
            <td>Только нулевые элементы</td>
        </tr>
        <tr>
            <td>5</td>
            <td><code>N = 1, A = [9]</code></td>
            <td><code>9</code></td>
            <td><code>1</code></td>
            <td>Один положительный элемент</td>
        </tr>
        <tr>
            <td>6</td>
            <td><code>N = 1, A = [-9]</code></td>
            <td><code>0</code></td>
            <td><code>0</code></td>
            <td>Один отрицательный элемент</td>
        </tr>
    </tbody>
</table>
<b>Блок-схема:</b> `scheme.drawio`

## Описание объектных моделей кода
### Класс `PositiveElementsAnalyzer`

Класс предназначен для анализа одномерного массива и поиска суммы и количества положительных элементов

<b>Поля класса</b>
<table>
    <thead>
        <tr>
            <th>Поле</th>
            <th>Тип</th>
            <th>Описание</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>array</code></td>
            <td><code>list[int]</code></td>
            <td>Одномерный массив чисел</td>
        </tr>
        <tr>
            <td><code>sum_positive</code></td>
            <td><code>int</code></td>
            <td>Сумма положительных элементов массива</td>
        </tr>
        <tr>
            <td><code>count_positive</code></td>
            <td><code>int</code></td>
            <td>Количество положительных элементов массива</td>
        </tr>
    </tbody>
</table>

<b>Метод класса</b>
<table>
    <thead>
        <tr>
            <th>Метод</th>
            <th>Описание</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>__init__(self, array)</code></td>
            <td>Конструктор класса. Получает массив и инициализирует сумму и счётчик нулями</td>
        </tr>
        <tr>
            <td><code>analyze(self)</code></td>
            <td>Проходит по массиву и считает сумму и количество положительных элементов</td>
        </tr>
        <tr>
            <td><code>get_result(self)</code></td>
            <td>Возвращает результат анализа: сумму и количество положительных элементов</td>
        </tr>
    </tbody>
</table>

## Тестовые примеры исходных данных

<table>
    <thead>
        <tr>
            <th>№</th>
            <th>Исходные данные</th>
            <th>Ожидаемая сумма</th>
            <th>Ожидаемое количество</th>
            <th>Что проверяется</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1</td>
            <td><code>N = 5, A = [1, -2, 3, 0, 4]</code></td>
            <td><code>8</code></td>
            <td><code>3</code></td>
            <td>Смешанный массив</td>
        </tr>
        <tr>
            <td>2</td>
            <td><code>N = 4, A = [-1, -5, 0, -3]</code></td>
            <td><code>0</code></td>
            <td><code>0</code></td>
            <td>Нету положительных элементов</td>
        </tr>
        <tr>
            <td>3</td>
            <td><code>N = 3, A = [2, 7, 10]</code></td>
            <td><code>19</code></td>
            <td><code>3</code></td>
            <td>Только положительные элементы</td>
        </tr>
        <tr>
            <td>4</td>
            <td><code>N = 5, A = [0, 0, 0, 0, 0]</code></td>
            <td><code>0</code></td>
            <td><code>0</code></td>
            <td>Только нулевые элементы</td>
        </tr>
        <tr>
            <td>5</td>
            <td><code>N = 1, A = [9]</code></td>
            <td><code>9</code></td>
            <td><code>1</code></td>
            <td>Один положительный элемент</td>
        </tr>
        <tr>
            <td>6</td>
            <td><code>N = 1, A = [-9]</code></td>
            <td><code>0</code></td>
            <td><code>0</code></td>
            <td>Один отрицательный элемент</td>
        </tr>
    </tbody>
</table>