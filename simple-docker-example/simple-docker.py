import time
import pandas as pd

print("Creating dataframe...")
df = pd.DataFrame({
    'Customer Name': ['tom', 'tim', 'john', 'jane', 'diddy'],
    'Gender': ['male', 'male', 'male', 'female', 'female'],
    'Customer Age': [20, 40, 30, 22, 64],
    'Membership Status': ['Bronze', 'Platinum', 'Bronze', 'Silver', 'Gold'],
    'Balance': [100, 5400, 230, 999, 840]
})
print("Dataframe created")

for index, row in df.iterrows():
    print(f"{df.columns[0]}: {row['Customer Name']}, {df.columns[1]}: {row['Gender']}, {df.columns[2]}: {row['Customer Age']}, {df.columns[3]}: {row['Membership Status']}, {df.columns[4]}: {row['Balance']}")

print("All customers processed! Exiting...")
time.sleep(5)