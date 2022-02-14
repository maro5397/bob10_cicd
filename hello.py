class Hello:
    def say(self):
        print("Hello world")
    def add(self, x, y):
        #print("x+y=", x + y)
        return x+y
        

if __name__ == "__main__":
    h = Hello()
    h.say()
    print(h.add(2, 3))