from acc_parser import AccParser
from generator import Generator

if __name__ == "__main__":
    with AccParser("sensor.csv") as parser:
        generator = Generator(parser.y_acc)
        generator.set_properties(
            k=0.1,
            m=0.05,
            length=0.01,
            area=0.01,
            B_max=0.001,
            R=1,
            n=30
        )
        print(generator.get_energy())
