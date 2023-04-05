class ReadKeyboard:
    def read(self):
        pass


class WritePrinter:
    def write(self,char):
        pass


class WriteDisk:
    def write(self,char):
        pass


class Copy:
    def copy(self, type):
        r = ReadKeyboard()
        while c := r.read() != "\n":
            if type == "printer":
                WritePrinter().write(c)
            else:
                WriteDisk().write(c)
