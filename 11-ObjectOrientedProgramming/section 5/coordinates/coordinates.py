class C:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def m(self, n):
        for row in self.coordinates:
            if row[0] > 0 and row[1] > 0:
                n -= 1
        if n > 0:
            return False
        else:
            return True