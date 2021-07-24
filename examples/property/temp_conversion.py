# Requires Python 3.8 (for := assignment) but should work in earlier
# versions with modification.

# Demonstrates effective use of properties, validation, and using keyword
# arguments at call site of constructor (instead of doing something like
# creating a factory method for each Temperature unit type for instance).

class Temperature(object):
    def __init__(self, **kwargs):
        if (tc := kwargs.get('celsius')) is not None:
            self.celsius = tc
        elif (tf := kwargs.get('fahrenheit')) is not None:
            self.fahrenheit = tf
        elif (tk := kwargs.get('kelvin')) is not None:
            self.kelvin = tk
        else:
            self.kelvin = 0.0

    def __repr__(self):
        return ("<T %7.2f °F %7.2f °C %7.2f °K>" %
                (self.fahrenheit, self.celsius, self.kelvin))

    @property
    def celsius(self):
        return self.kelvin - 273.15

    @celsius.setter
    def celsius(self, tc):
        self.kelvin = tc + 273.15

    @property
    def fahrenheit(self):
        return (9.0 / 5.0) * (self.kelvin - 273.15) + 32.0

    @fahrenheit.setter
    def fahrenheit(self, tf):
        self.kelvin = (5.0 / 9.0) * (tf - 32.0) + 273.15

    @property
    def kelvin(self):
        return self._tk

    @kelvin.setter
    def kelvin(self, value):
        if value < 0.0:
            raise ValueError("invalid temperature (below 0 °K)")
        self._tk = value


if __name__ == '__main__':
    print("set temperature")
    t = Temperature()
    t.celsius = 100
    print(" boiling: ", t)
    t.fahrenheit = 32
    print(" freezing:", t)
    t.kelvin = 0
    print(" abs zero:", t)

    print("constructor with keyword arguments")
    t_100c = Temperature(celsius=100)
    t_0c = Temperature(fahrenheit=32)
    t_0k = Temperature(kelvin=0)
    print(" T_100C: ", t_100c)
    print(" T_0C:   ", t_0c)
    print(" T_0K:   ", t_0k)

    print("is property valid?")
    print(" okay:", Temperature(kelvin=0.0))
    print(" okay:", Temperature(celsius=-273.15))
    print(" okay:", Temperature(fahrenheit=-459.66))
    # raises ValueError
    #bad = Temperature(kelvin=-0.1)
    #bad = Temperature(celsius=-273.16)
    #bad = Temperature(fahrenheit=-459.68)
