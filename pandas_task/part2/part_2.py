import pandas as pd

# Load dataset
df = pd.read_csv("./data/train.csv")

# Helper function for clean sections
def section(title):
    print("\n" + "="*70)
    print(f"{title.center(70)}")
    print("="*70)


# ============================================== STEP 1: EXPLORATION ==============================================
section("STEP 1: EXPLORATION")

print("\nFirst 5 Rows:")
print(df.head().to_string())

print("\nDataset Info:")
df.info()

print("\nStatistical Summary:")
print(df.describe().round(2).to_string())


# ============================================== STEP 2: DATA CLEANING ============================================
section("STEP 2: DATA CLEANING")

# Fill missing Age with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Embarked with mode
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

df.drop(columns=["Cabin"], inplace=True)

df.drop_duplicates(inplace=True)

print("Missing values handled and dataset cleaned.")


# ============================================== STEP 3: DATA ANALYSIS ============================================
section("STEP 3: DATA ANALYSIS")

print("\nSurvival Rate by Gender:")
print(df.groupby("Sex")["Survived"].mean().round(3))

print("\nSurvival Rate by Class:")
print(df.groupby("Pclass")["Survived"].mean().round(3))

print("\nAverage Age per Class:")
print(df.groupby("Pclass")["Age"].mean().round(1))

# Age groups
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[0, 12, 18, 60, 100],
    labels=["Child", "Teen", "Adult", "Senior"]
)

print("\nSurvival Rate by Age Group:")
print(df.groupby("AgeGroup")["Survived"].mean().round(3))


# ============================================== STEP 4: FILTERING ================================================
section("STEP 4: FILTERING")

female_survived = df[(df["Sex"] == "female") & (df["Survived"] == 1)]
print(f"\nFemale Survivors: {len(female_survived)}")
print(female_survived.head().to_string())

children_survived = df[(df["Age"] < 12) & (df["Survived"] == 1)]
print(f"\nChild Survivors: {len(children_survived)}")
print(children_survived.head().to_string())

first_class_survived = df[(df["Pclass"] == 1) & (df["Survived"] == 1)]
print(f"\nFirst Class Survivors: {len(first_class_survived)}")
print(first_class_survived.head().to_string())

# =============================================== STEP 5: Insights =======================================================
def print_insights(df):
    print("\n" + "="*70)
    print("STEP 5: INSIGHTS".center(70))
    print("="*70 + "\n")
    
    # 1. Gender
    survival_by_gender = df.groupby("Sex")["Survived"].mean()
    print("1. Survival by Gender")
    print(f"   Female survival rate: {survival_by_gender['female']:.2%}")
    print(f"   Male survival rate:   {survival_by_gender['male']:.2%}")
    print("   Conclusion: Women were prioritized over men.\n")
    
    # 2. Class
    survival_by_class = df.groupby("Pclass")["Survived"].mean()
    print("2. Survival by Class")
    for cls in sorted(survival_by_class.index):
        print(f"   Class {cls} survival rate: {survival_by_class[cls]:.2%}")
    print("   Conclusion: Higher class passengers had better survival chances.\n")
    
    # 3. Age
    df["AgeGroup"] = pd.cut(
        df["Age"], bins=[0,12,18,60,100], labels=["Child","Teen","Adult","Senior"]
    )
    survival_by_age = df.groupby("AgeGroup")["Survived"].mean()
    print("3. Survival by Age Group")
    for group in survival_by_age.index:
        print(f"   {group} survival rate: {survival_by_age[group]:.2%}")
    print("   Conclusion: Children had higher survival probability than adults.\n")
    
    # 4. Highest survival group
    high_survival = df[(df["Sex"]=="female") & (df["Pclass"]==1) & (df["Age"]<12)]
    print("4. Highest Survival Group")
    print(f"   Female, 1st Class, Children survived count: {len(high_survival)}")
    print("   Weakest group: Male, 3rd Class, Adults.\n")
    
    print("="*70)
    print("END OF INSIGHTS".center(70))
    print("="*70 + "\n")
    

print_insights(df)