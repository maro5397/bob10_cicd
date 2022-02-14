class Hello:
    def say(self):
        print("Hello world")
    def add(self, x, y):
        #print("x+y=", x + y)
        a = x
        b = y
        a = a + 1
        return a+b
        

if __name__ == "__main__":
    h = Hello()
    h.say()
    print(h.add(2, 3))