from abc import ABC, abstractmethod


class ObserverInterface(ABC):
    @abstractmethod
    def update(self):
        pass


class ObservableInterface(ABC):
    @abstractmethod
    def addObserver(self, observer: ObserverInterface):
        pass

    @abstractmethod
    def RemoveObserver(self, observer: ObserverInterface):
        pass

    @abstractmethod
    def notify(self):
        pass

    @abstractmethod
    def setStock(self, stockCount: int):
        pass

    @abstractmethod
    def getStock(self):
        pass


class EmailNotifier(ObserverInterface):
    def __init__(self, observable: ObserverInterface, email):
        self.observable = observable
        self.email = email
    def update(self):
        # print('p')
        self.sendEmail()
    def sendEmail(self):
        print("send email to {} Hurry stock left is {}".format(self.email, self.observable.getStock()))

class IphoneObservable(ObservableInterface):
    def __init__(self):
        self.observers = set()
        self.stockCount = 0
    def addObserver(self, observer):
        self.observers.add(observer)
    def RemoveObserver(self, observer):
        self.observers.add(observer)
    def notify(self):
        for observer in self.observers:
            # print(observer)
            observer.update()
    def setStock(self, stockCount):
        if self.stockCount == 0:
            self.stockCount = stockCount
            self.notify()
        else:
            self.stockCount += stockCount
    def getStock(self):
        return self.stockCount

ip = IphoneObservable()
ip.addObserver(EmailNotifier(ip, 'sagar@gmail.com'))
ip.addObserver(EmailNotifier(ip, 'sagar2@gmail.com'))
ip.setStock(10)
