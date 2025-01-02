from stats import Statistics

# Then, use the program for numbers below to calculate and print the basic staticstics:

# 12, 37, 6, 9, 17 

def main():
    stats = Statistics()

    stats.add(12)
    stats.add(37)
    stats.add(6)
    stats.add(9)
    stats.add(17)
    stats.display_info()

if __name__ == "__main__":
    main()