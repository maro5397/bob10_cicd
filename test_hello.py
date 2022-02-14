from unittest import TestProgram
import hello

class TestHello():
    def test_add(self):
        h = hello.Hello()
        if h.add(2,3) != 5:
            print('FAILED')
            exit(1)
        print('PASS')
        if h.add(2,5) != 7:
            print('FAILED')
            exit(1)
        print('PASS')
        
if __name__ == "__main__":
    test = TestHello()
    test.test_add()