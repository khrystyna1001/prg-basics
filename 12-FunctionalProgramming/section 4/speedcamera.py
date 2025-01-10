speeds = [48,47,54,50,42,68,39,46]

speedings = lambda x: filter(lambda speed: speed > 50, x)
print(list(speedings(speeds)))