import time
class Star():
    def __init__(self, x, y, brightness, period, side):
        self.x = x
        self.y = y
        self.brightness = brightness
        self.period = period
        self.side = side
        self.time_br_change = -1
        self.v_br = 255 / (self.period / 2)

    def check_brightness(self):
        if self.time_br_change < 0:   #if нужен для запуска функции первый раз
            self.time_br_change = time.time()
        time_diff = time.time() - self.time_br_change
        change_brightness = time_diff * self.v_br
        if abs(change_brightness) > 1:    #if нужен для изменения яркости на целое значение
            self.brightness += int(change_brightness)
            self.time_br_change = time.time()
            if self.brightness > 255:
                self.v_br = self.v_br * (-1)
                self.brightness = 255
            elif self.brightness < 0:
                self.v_br = self.v_br * -1
                self.brightness = 0
        print(self.brightness, self.v_br, time_diff * self.v_br)


        


