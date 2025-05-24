# ітерація (цикли)
myList = [1, 2, 3]           # three generally
iterator = iter(myList)      # creating iterator (__iter__)
print(next(iterator))        # one           (__next__)
print(next(iterator))        # two
print(next(iterator))        # three

print("================================================")

# ітеровані об'єкти
class Counter:
    def __init__(self, max):
        self.i = 0
        self.maxN = max
    def __iter__(self):            # лінк на об. ітер
        self.i = 0
        return self                # занулення
    def __next__(self):
        self.i += 1
        if self.i > self.maxN:
            raise StopIteration
        return self.i
count = Counter(5)
for elem in count:
    print(elem)

print("================================================")

# генератори (ітератор+функція)
def f(n, max):
    i = 0
# _ - якщо змінна поч значення 0
    for _ in range(max):
        yield n**i             # return але НЕ закінчує def
        i += 1
res = f(123, 10)
print(res)
for _ in res:
    print(_)

print("================================================")

# декоратор (покращує звичний вигляд чогось)
def c(function):                                  # base
    def c(*args, **kwargs)
        try:
            result = function(*args, **kwargs)    # launching
        except Exception as exc:
            print(f"problem {exc}")
        else:
            print(f"no problems {result}")
    return c()
@c
def calc(exp):
    return eval(exp)
calc("2+2")