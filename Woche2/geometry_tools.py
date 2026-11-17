import math


def circle_area(radius):
    return math.pi * radius ** 2

if __name__ == '__main__':
    # läuft nur bei direkter Ausführung, nicht beim Import
    print(f"circle_area(1) = {circle_area(1):.2f}")
