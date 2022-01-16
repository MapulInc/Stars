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
        print(self.brightness)
        if self.time_br_change < 0:
            self.time_br_change = time.time()
        time_diff = time.time() - self.time_br_change
        change_brightness = time_diff * self.v_br
        if change_brightness > 1:
            self.brightness += int(change_brightness)
            self.time_br_change = time.time()
        


