"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Takes in int (default = 0) to start sequential serial number"""
        self.start = start
        self.serial = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.serial}>"

    def generate(self):
        """Generates and returns next increment of serial number"""
        self.serial += 1
        return self.serial - 1

    def reset(self):
        "Resets serial number to start intial start point"
        self.serial = self.start