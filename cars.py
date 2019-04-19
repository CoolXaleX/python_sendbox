import csv
import os


class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__("car", brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__("truck", brand, photo_file_name, carrying)
        self.body_length, self.body_width, self.body_height = Truck.get_parameters(body_whl)

    @staticmethod
    def get_parameters(body_whl):
        try:
            atr = body_whl.split('x')
            return float(atr[0]), float(atr[1]), float(atr[2])
        except:
            return 0.0, 0.0, 0.0

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__("spec_machine", brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            try:
                if row[0] == "car":
                    car_list.append(Car(row[1], row[3], row[5], row[2]))
                elif row[0] == "truck":
                    car_list.append(Truck(row[1], row[3], row[5], row[4]))
                elif row[0] == "spec_machine":
                    car_list.append(SpecMachine(row[1], row[3], row[5], row[6]))
            except:
                continue
    return car_list
