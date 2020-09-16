
import codecs

def check_float(st):
    try:
        float(st)
    except ValueError:
        return False
    else:
        return float(st)


def get_car_list(filename):
    car_list = []
    with codecs.open(filename, 'r', 'utf-8') as file:
        count = len(file.readlines())
    with codecs.open(filename, 'r', 'utf-8') as file:
        for _ in range(count):
            line = file.readline()
            line = line.replace('\n', '')
            line = line.replace('\r', '')
            info = line.split(';')
            if len(info)>=6 and info[1]!='':
                if check_float(info[5]) and info[3]!='':
                    if info[0] == 'car':
                        if info[2].isdigit():
                            car = Car(info[0], info[1], info[3], float(info[5]), int(info[2]))
                            car_list.append(car)
                    elif info[0] == 'truck':
                        car = Truck(info[0], info[1], info[3], float(info[5]), info[4])
                        car_list.append(car)
                    elif info[0] == 'spec_machine':
                        if len(info) >= 7:
                            car = Specmachine(info[0], info[1], info[3], float(info[5]), info[6])
                            car_list.append(car)

    return car_list


class Carbase:
    def __init__(self, car_type, brand, photo_le_name, carrying):
        self.brand = brand
        self.car_type = car_type
        self.photo_le_name = photo_le_name
        self.carrying = carrying

    def __str__(self):
        return self.car_type+ ' ' + self.brand  + ' ' + self.photo_le_name + ' ' + str(self.carrying)

    def __repr__(self):
        return self.__str__()

    def get_photo_le_ext(self):
        return self.photo_le_name[self.photo_le_name.find('.'):]


class Car(Carbase):
    def __init__(self, car_type, brand, photo_le_name, carrying, passenger_seats_count):
        super().__init__(car_type, brand, photo_le_name, carrying)
        self.passenger_seats_count = passenger_seats_count

    def __str__(self):
        return super().__str__() + ' ' + str(self.passenger_seats_count)

    def __repr__(self):
        return self.__str__()


class Truck(Carbase):
    def __init__(self, car_type, brand, photo_le_name, carrying, body_wlh):
        super().__init__(car_type, brand, photo_le_name, carrying)
        params = Truck.get_params(body_wlh)
        self.body_length = params[0]
        self.body_width = params[1]
        self.body_height = params[2]

    def __str__(self):
        return super().__str__() + ' ' + str(self.body_length) + ' ' + str(self.body_width) + ' ' + str(
            self.body_height)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def get_params(body_wlh):
        if body_wlh != '':
            lst = list(map(float, body_wlh.split('x')))
        else:
            lst = [0.0, 0.0, 0.0]
        return lst

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class Specmachine(Carbase):
    def __init__(self, car_type, brand, photo_le_name, carrying, extra):
        super().__init__(car_type, brand, photo_le_name, carrying)
        self.extra = extra

    def __str__(self):
        return super().__str__() + ' ' + str(self.extra)

    def __repr__(self):
        return self.__str__()


def main():
    get_car_list('solution.txt')


if __name__ == '__main__':
    main()
