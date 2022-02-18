class Hello:
    def say(self):
        print('hello, world')

    def add(self, x, y):
        # print("x+y=", (x+y))
        a = x
        b = y
        return (a+b)


if __name__ == "__main__":
    h = Hello()
    h.say()
    print(h.add(2, 3))
