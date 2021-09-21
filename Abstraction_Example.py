from abc import ABC, abstractmethod
print("hello")

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("its running lap")


class WhiteBoard(Computer):
    def process(self):
        print("it ready whiteboard")
        self.write()

    def write(self):
        print("its writing")


class Programmer:
    def work(self, com):
        print("solve bugs")
        com.process()





#lap1 = Laptop()
# lap1.process()
wh1=WhiteBoard()
prog1 = Programmer()
prog1.work(wh1)
