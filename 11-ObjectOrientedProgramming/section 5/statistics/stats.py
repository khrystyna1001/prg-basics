# Add to the set of numbers, the next number read from the keyboard 
# (store the numbers in the array)
# Display all numbers separated by a space
# Determine the greatest number
# Determine the smallest number
# Calculate the arithmetic mean of numbers
# Calculate of the median
# Print of calculated / determined statistical quantities (minimum, maximum, arithmetic 
# mean, median)

class Statistics:
    def __init__(self):
        self.numbers = []
    
    def add(self, number):
        self.numbers.append(number)
    
    def mean(self):
        if not self.numbers:
            return 0
        return sum(self.numbers) / len(self.numbers)
    
    def min(self):
        if not self.numbers:
            return 0
        return min(self.numbers)
    
    def max(self):
        if not self.numbers:
            return 0
        return max(self.numbers)

    def median(self):
        if not self.numbers:
            return 0
        return sorted(self.numbers)[len(self.numbers) // 2]
    
    def display_info(self):
        print(f"Numbers: {self.numbers}")
        print(f"Mean: {self.mean():.1f}")
        print(f"Min: {self.min()}")
        print(f"Max: {self.max()}")
        print(f"Median: {self.median()}")