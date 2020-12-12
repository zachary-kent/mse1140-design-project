from acc_parser import AccParser
from generator import Generator

if __name__ == "__main__":
    STEPS = 200
    STEPS_PER_DAY = 10000
    with AccParser("sensor.csv") as parser:
        generator = Generator(parser.y_acc)
        generator.constants(
            k=50,
            m=0.0067,
            length=0.01,
            area=0.0001,
            B_max=1.5,
            R=2,
            n=30
        )
        energy_per_day = generator.energy() * STEPS_PER_DAY / STEPS
        print(f"Energy generated per day: {round(energy_per_day, 50)} J")
