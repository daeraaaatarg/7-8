# 1
print("Task 1")
class WLI:
    def __init__(self, words):
        self.words = words
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.words):
            length = len(self.words[self.index])
            self.index += 1
            return length
        else:
            raise StopIteration
words = ["gun", "rose", "court", "Rhysand"]
iterator = WLI(words)
print(words)
for length in iterator:
    print(length)

print("================================================================================================================================================")
print("Task 2")
# 2
class Two:
    def __init__(self, max):
        self.max = max
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.max:
            result = 2 ** self.i
            self.i += 1
            return result
        else:
            raise StopIteration
iterator = Two(200)
for value in iterator:
    print(value)

print("================================================================================================================================================")
print("Task 3")
# 3
def f(n, max):
    i = 0
    for _ in range(max):
        yield n**i
        i += 1
res = f(3, 300)
for _ in res:
    print(_)

print("================================================================================================================================================")
