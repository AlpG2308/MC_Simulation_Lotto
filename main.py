import numpy as np
import plotly.express as px
from tqdm import tqdm
wins = []
tip_cost = 1.20
tip_wins_sz = {2:6,3:21.20,4:191.1,5:12135.4,6:12585434.4}
tip_wins = {3:11.1,4:50.3,5:4019.2, 6:1003509.3}
winnings = 0
for i in tqdm(range(1000000)):
    super_zahl = np.random.choice(10,1)
    sz_rand_choice = np.random.choice(10,1)
    picked_numbers = np.random.choice(np.arange(1,50),6,replace=False)
    winning = []
    for j in range(6):
        winning.append(np.random.choice(np.arange(1,50),1, replace = False))
    wins.append(len(np.intersect1d(np.array(winning),picked_numbers)))
    try:
        if (super_zahl == sz_rand_choice):
            winnings += tip_wins_sz[len(np.intersect1d(np.array(winning),picked_numbers))]-tip_cost
        elif (sz_rand_choice != super_zahl):
            winnings += tip_wins[len(np.intersect1d(np.array(winning),picked_numbers))]-tip_cost
    except KeyError:
        winnings -= tip_cost
fig = px.histogram(wins)
fig.show()
print(f"{(winnings/1000000):.2f}")