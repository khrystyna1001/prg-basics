class C:
    def __init__(self, data):
        self.data = data

    def m1(self, s, n):
        if s in self.data.keys():
            self.data[s] = n
    
    def m2(self, s):
        res = 0
        for x in s:
            if x in self.data.keys():
                res += self.data[x]
        return res