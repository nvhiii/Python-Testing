class Time:

    def __init__(self, hours = 0, minutes = 0, seconds = 0):    ## similar to a constructor
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):  ## overloads the print fxn
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def __radd__(self, other):
        return self.__add__(other)

    def __add__(self, other):   ## this overrides the + operator
        s1 = self.time_to_int()

        if isinstance(other, Time): ## are we allowed to call time_to_int() on other? A: only if it is of type Time
            s2 = other.time_to_int()
        else:
            s2 = int(other)
        return int_to_time(s1 + s2)

    def time_to_int(self):
        seconds = self.seconds
        seconds += self.minutes * 60
        seconds += self.hours * 3600
        return seconds

    def __gt__(self, other):  ## replaces greather than operator
        s1 = self.time_to_int()
        s2 = other.time_to_int()
        return s1 > s2

    ## above is a method, below is an allocation of functions
    ## oop above, procedural below

def increment(t, s):
    t.seconds += s

def int_to_time(s): ## this will remain a funciton because its a method that doesnt need a
    result = Time()
    result.seconds = s
    result.minutes = result.seconds // 60
    result.seconds = result.seconds % 60
    result.hours = result.minutes // 60
    result.minutes = result.minutes % 60

    return result

t1 = Time(7, 30, 21)
t2 = Time(4, 45, 44)

print(10 + t1)
print(t1.time_to_int())
print(t1)

if t1 > t2:
    print("t1")
else:
    print("t2")
