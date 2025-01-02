import stadium

# C({"A":120,"D":150,"G":90,"K":110})
# m1("G",130)
# m2("GD") returns 280
# m2("KEJ") returns 110

def main():
    stad = stadium.C({"A":120,"D":150,"G":90,"K":110})
    stad.m1("G",130)
    print(stad.m2("GD"))
    print(stad.m2("KEJ"))

if __name__ == "__main__":
    main()