class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname = surname
        self.age = age
        self.seniority = seniority
    def __str__(self):
        if self.age >= 18:
            return f"{self.surname.upper()}{self.name[0].upper()}{self.seniority}"
        else:
            return f"{self.surname.lower()}{self.name[0].lower()}{self.seniority}"