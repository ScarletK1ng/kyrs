# Задание 2
<b>Задача:</b> Разработать блок-схему алгоритма, написать код программы на языке высокого уровня, составить тестовые примеры исходных данных, которые охватывали бы прохождение всех ветвей алгоритма, составить описание объектных моделей кода. Дан одномерный массив А размерности N. Найти количество элементов, больших заданного числа В и их произведение.

<b>Блок-схема:</b> `task2.drawio`

## Описание объектных моделей кода

<b>Основные объекты</b>
<table>
    <thead>
        <tr>
            <th>Объект</th>
            <th>Тип</th>
            <th>Описание</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>n</code></td>
            <td><code>int</code></td>
            <td>Размер одномерного массива</td>
        </tr>
        <tr>
            <td><code>arr</code></td>
            <td><code>list[int]</code></td>
            <td>Одномерный массив целых чисел</td>
        </tr>
        <tr>
            <td><code>i</code></td>
            <td><code>int</code></td>
            <td>Индекс текущего элемента массива</td>
        </tr>
        <tr>
            <td><code>value</code></td>
            <td><code>int</code></td>
            <td>Очередной вводимый элемент массива</td>
        </tr>
        <tr>
            <td><code>sum_pos</code></td>
            <td><code>int</code></td>
            <td>Сумма положительных элементов массива</td>
        </tr>
        <tr>
            <td><code>count_pos</code></td>
            <td><code>int</code></td>
            <td>Количество положительных элементов массива</td>
        </tr>
        <tr>
            <td><code>find_positive_sum_and_count(arr)</code></td>
            <td>функция</td>
            <td>Выполняет обработку массива и возвращает сумму и количество положительных элиментов</td>
        </tr>
        <tr>
            <td><code>main()</code></td>
            <td>функция</td>
            <td>Организует ввод данных, проверку размера массива, вызов обработки и вывод результата</td>
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