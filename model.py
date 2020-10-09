class Model:
    def __init__(self):
        self.count = 0
        self.observers = set()

        
    def count_up(self):
        self.count = self.count + 1
        self.notify()

        
    def add_observer(self, observer):
        self.observers.add(observer)

        
    def notify(self):
        for observer in self.observers:
            observer.update()
