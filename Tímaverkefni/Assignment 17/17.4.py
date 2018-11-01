class Clock:
    def __init__(self, hours = 0, minutes = 0, seconds = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def str_update(self, time_string):
        time_list = time_string.split(":")
        self.hours, self.minutes, self.seconds = [int(i) for i in time_list]

    def __str__(self):
        return "{} hours, {} minutes and {} seconds".format(self.hours, self.minutes, self.seconds)

    def add_clocks(self, clock):
        new_clock = Clock()
        mins, new_clock.seconds = divmod(self.seconds + clock.seconds,60)
        hour, new_clock.minutes = divmod(self.minutes + clock.minutes + mins, 60)
        new_clock.hours = self.hours + clock.hours + hour
        if new_clock.hours >= 24:
            new_clock.hours = new_clock.hours % 24
        return new_clock

clock1 = Clock()
clock2 = Clock()
print(clock1)
print(clock2)
clock1.str_update("03:21:34")
clock2.str_update("05:45:52")
print(clock1)
print(clock2)
clock3 = clock1.add_clocks(clock2)
print(clock3)


