### **Exercise 4: Feature Engineering for Classification**
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler

# Step 1: Load the Titanic dataset
df = sns.load_dataset("titanic")

# Step 2: Create a new feature: family_size = sibsp + parch + 1 (Total family members onboard).
df["family_size"] = df["sibsp"] + df["parch"] + 1

# Step 3: Encode categorical variables (sex, embarked) using one-hot encoding.
df = pd.get_dummies(df, columns=["sex","embarked"], drop_first=True)

# Step 4: Select numerical features to scale
num_features = ["age","fare","family_size"]

# Step 5: Handle mising values
df[num_features] = df[num_features].fillna(df[num_features].median())

# Step 6: Scale numerical features using MinMaxScaler
scaler = MinMaxScaler()
df[num_features] = scaler.fit_transform(df[num_features])

print(df.head())