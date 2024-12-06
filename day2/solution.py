""" The engineers are trying to figure out which reports are safe. 
The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. 
So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.

Analyze the unusual data from the engineers. How many reports are safe?
"""
#%%

# i want this to stop as soon as there's a diiference, but for now i just do it all first and then check if it's safe
import numpy as np

with open("input.txt", "r") as file:
    # Create a list of lists where each row becomes a list
    rows = [[int(x) for x in line.split()] for line in file]
# %%
# for report in rows:
def check_row_safety(report):
    difference = []
    for i,x in enumerate(report[:-1]):
        difference.append(report[i+1]-report[i])
    all_same_sign = all(x > 0 for x in difference) or all(x < 0 for x in difference)
    safe_difference = all(abs(x)>0 for x in difference) and all(abs(x)<4 for x in difference)
    return all_same_sign and safe_difference

# check which reports are safe, we only need how many are safe but i'm also saving the index
safe_reports = []
unsafe_reports = []
for i, report in enumerate(rows):
    safety = check_row_safety(report)
    # print(safety)
    if safety:
        safe_reports.append(i)
    else:
        unsafe_reports.append(i)

print(len(safe_reports))
# %% PART 2: The problem dampener
# now i'm only going to look at the unsafe reports
# for each report, step trhough each level and check for difference
for report in unsafe_reports:
    print(rows[report])
#%%
test = rows[1]
print(test)
safe_difference = []
sign = []
for i,x in enumerate(test[:-1]):
    difference = test[i+1]-test[i]
    
    if difference > 0:
        sign.append("positive")
    elif difference < 0:
        sign.append("negative")
number_false_dif = safe_difference.count(False)
all_same = len(set(sign)) == 1



# %%
