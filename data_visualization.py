# 📌 Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 📌 Load Dataset
df = pd.read_csv("train.csv")

# 📌 Initial Data Exploration
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.nunique())

# 📌 Univariate Analysis

# Histogram of Age and Fare
df['Age'].hist(color='skyblue', edgecolor='black')
plt.title("Distribution of Age")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

df['Fare'].hist(color='orange', edgecolor='black')
plt.title("Distribution of Fare")
plt.xlabel("Fare")
plt.ylabel("Frequency")
plt.show()

# Bar Plots of Categorical Features
df['Sex'].value_counts().plot(kind='bar', color='steelblue')
plt.title("Count of Passengers by Sex")
plt.xlabel("Sex")
plt.ylabel("Count")
plt.show()

df['Pclass'].value_counts().plot(kind='bar', color='lightgreen')
plt.title("Count of Passengers by Pclass")
plt.xlabel("Pclass")
plt.ylabel("Count")
plt.show()

# 📌 Bivariate Analysis

# Boxplot of Age vs Survival
sns.boxplot(x='Survived', y='Age', data=df)
plt.title("Age Distribution by Survival")
plt.xlabel("Survived")
plt.ylabel("Age")
plt.show()

# Countplot of Sex vs Survival
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival Count by Sex")
plt.xlabel("Sex")
plt.ylabel("Count")
plt.legend(title="Survived", labels=["No", "Yes"])
plt.show()

# 📌 Multivariate Analysis

# Pairplot
sns.pairplot(df[['Survived', 'Age', 'Fare', 'Pclass']])
plt.suptitle("Pairplot of Survival, Age, Fare, Pclass", y=1.02)
plt.show()

# Heatmap of Correlation
plt.figure(figsize=(10, 6))
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap of Numeric Features")
plt.show()
