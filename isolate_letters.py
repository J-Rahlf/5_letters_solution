import pandas as pd

# Read the CSV file
df = pd.read_csv("five_letter_words.csv")

# Create a new DataFrame for preprocessing
preprocessed_df = pd.DataFrame(columns=["Word", "L1", "L2", "L3", "L4", "L5"])

# Iterate over each row in the original DataFrame
for index, row in df.iterrows():
    word = row["Word"]
    # Add the word to the new DataFrame
    preprocessed_df.loc[index, "Word"] = word
    # Split the word into letters and add them to the new DataFrame
    for i in range(len(word)):
        preprocessed_df.loc[index, f"L{i+1}"] = word[i]

# Save the new DataFrame as a CSV file
preprocessed_df.to_csv("preprocessed_words.csv", index=False)
