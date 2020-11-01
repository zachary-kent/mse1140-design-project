import csv


class AccParser:

    def __enter__(self):
        self.file = open(self.path, mode="r")
        self.reader: csv.reader = csv.reader(self.file, delimiter=",")
        self.__init_lists__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def __init_lists__(self):
        self.lines = tuple(row for row in self.reader)[1::]
        self.x_acc = self.__get_acc__(1)
        self.y_acc = self.__get_acc__(2)
        self.z_acc = self.__get_acc__(3)

    def __get_acc__(self, index: int) -> tuple:
        return tuple((float(line[0]), float(line[index])) for line in self.lines)

    def __init__(self, path: str):
        self.path = path


if __name__ == "__main__":
    with AccParser("sensor.csv") as parser:
        print(parser.x_acc)



