import pandas as pd

# Step 1: Create dictionary
data = {
    "Name": [
        "Abel", "Sara", "John", "Mahi", "Kebede",
        "Liya", "Noah", "Hana", "Samuel", "Ruth",
        "Daniel", "Meron", "Eden", "Yonatan", "Betty"
    ],
    "Age": [
        20, 22, 21, 23, 24,
        20, 22, 21, 23, 22,
        24, 21, 20, 23, 22
    ],
    "Department": [
        "CS", "Math", "Physics", "CS", "Biology",
        "Math", "Physics", "CS", "Biology", "Math",
        "Physics", "CS", "Biology", "Math", "CS"
    ],
    "GPA": [
        3.5, 3.8, 3.2, 3.9, 2.8,
        3.6, 3.1, 3.7, 2.9, 3.4,
        3.0, 3.8, 2.7, 3.5, 3.9
    ],
    "Graduated": [
        False, True, False, True, False,
        True, False, True, False, True,
        False, True, False, True, True
    ]
}

# Step 2: Custom index
index_labels = [f"STD{i}" for i in range(1, 16)]

# Step 3: Create DataFrame
df = pd.DataFrame(data, index=index_labels)

# Step 4: Display
print(df)