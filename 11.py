print("Введите 2 не нулевых числа.")
a = int(input())
if a == 0:
    print("Введите не нулевое число.")
    exit()
b = int(input())
if b == 0:
    print("Введите не нулевое число.")
    exit()
c = abs(a) + abs(b)
v = abs(a) - abs(b)
n = abs(a) * abs(b)
m = abs(a) / abs(b)
print(f"Сумма, разность, произведение и частное их модулей:", c, v, n, m)