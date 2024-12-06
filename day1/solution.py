"""Pair up the smallest number in the left list with the smallest number in the right list, 
then the second-smallest left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances.
    To find the total distance between the left list and the right list, add up the distances between all of the pairs you found. 
    In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!

Your actual left and right lists contain many location IDs. What is the total distance between your lists?
    """

#%%
import numpy as np
import pandas as pd
# PART 1:
data = pd.read_csv("input.txt", sep=r'\s+', header=None, names=["Left", "Right"])
sorted_data = pd.DataFrame({col: sorted(data[col]) for col in data.columns})
sorted_data['Distance'] = [abs(left - right) for left, right in zip(sorted_data['Left'], sorted_data['Right'])]
total_dist = sum(sorted_data['Distance'])
print(total_dist)
# %%
# Part 2: calculate a similarity score by counting how many times a value in left list
# is also in right list, and multiply by that value

from collections import Counter
counts = Counter(sorted_data['Right'])
sim_score = []
for x in sorted_data['Left']:
    count = counts[x]
    # print(f"{x} occurs {counts[x]} times in right list")
    sim_score.append(x*count)

total_sim_score = sum(sim_score)
print("total sim score: ", total_sim_score)
# %%
