import math


def count_proper_divisors(n):
    """Возвращает количество делителей числа n, не считая 1 и n."""
    if n <= 1:
        return 0

    divisors = set()
    # Перебираем делители до корня из n
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            # Добавляем парный делитель (n // i), если он не равен i
            if i != n // i:
                divisors.add(n // i)

    return len(divisors)


# Ввод данных
a = int(input())
b = int(input())

count = 0

# Перебираем числа в интервале (a, b] — т.е. от a+1 до b включительно
for num in range(a + 1, b + 1):
    if count_proper_divisors(num) == 6:
        count += 1

# Вывод результата
if count == 0:
    print(-1)
else:
    print(count)
