import coordinates

def main():
    cords = coordinates.C([[2,3],[1,8],[-6,4],[3,-7]])
    print(cords.m(2))
    print(cords.m(1))
    print(cords.m(3)) 

if __name__ == "__main__":
    main()