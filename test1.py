import numpy as np
import pandas as pd

# Generating random scores for each person
p1 = np.random.randint(25, 100, 5)
p2 = np.random.randint(25, 100, 5)
p3 = np.random.randint(25, 100, 5)
p4 = np.random.randint(25, 100, 5)
p5 = np.random.randint(25, 100, 5)
p6 = np.random.randint(25, 100, 5)
p7 = np.random.randint(25, 100, 5)
p8 = np.random.randint(25, 100, 5)
p9 = np.random.randint(25, 100, 5)
p10 = np.random.randint(25, 100, 5)

# Creating a DataFrame
ds4 = pd.DataFrame({
    "person_1": p1,
    "person_2": p2,
    "person_3": p3,
    "person_4": p4,
    "person_5": p5,
    "person_6": p6,
    "person_7": p7,
    "person_8": p8,
    "person_9": p9,
    "person_10": p10
}, index=["Tamil", "English", "Maths", "Science", "Social"])

# Creating a DataFrame for the totals row
tot = pd.DataFrame({
    "person_1": [ds4["person_1"].sum()],
    "person_2": [ds4["person_2"].sum()],
    "person_3": [ds4["person_3"].sum()],
    "person_4": [ds4["person_4"].sum()],
    "person_5": [ds4["person_5"].sum()],
    "person_6": [ds4["person_6"].sum()],
    "person_7": [ds4["person_7"].sum()],
    "person_8": [ds4["person_8"].sum()],
    "person_9": [ds4["person_9"].sum()],
    "person_10": [ds4["person_10"].sum()]
}, index=["Total"])

# Concatenating the totals row to the original DataFrame
ds5 = pd.concat([ds4, tot])

print(ds5)
