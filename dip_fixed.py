from abc import abstractmethod,ABC


class Reader(ABC):
    @abstractmethod
    def read(self):
        pass


class Writer(ABC):
    @abstractmethod
    def write(self):
        pass


class ReadKeyboard(Reader):
    def read(self):
        pass


class WritePrinter(Writer):
    def write(self, text):
        pass


class WriteDisk(Writer):
    def write(self, text):
        pass


class Copy:
    def copy(self, Reader_obj, Writer_obj):
        while c := Reader_obj.read() != "\n":
            Writer_obj.write(c)
            
