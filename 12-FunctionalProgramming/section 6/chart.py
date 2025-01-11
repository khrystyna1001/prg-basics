import matplotlib.pyplot as plt

medals = [{"country":"Denmark","gold":2,"silver":4,"bronze":6},
{"country":"Finland","gold":5,"silver":0,"bronze":4},
{"country":"USA","gold":12,"silver":5,"bronze":11},
{"country":"Peru","gold":0,"silver":1,"bronze":7}]

num_of_medals = []
for medal in medals:
    num_of_medals.append(medal["gold"] + medal["silver"] + medal["bronze"])

for medal in medals:
    plt.bar(medal["country"], num_of_medals[medals.index(medal)])
plt.show()