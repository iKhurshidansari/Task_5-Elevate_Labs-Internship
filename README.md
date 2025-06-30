# 🚢 Titanic Dataset - Exploratory Data Analysis (EDA)

## 📊 Overview

This project was completed as part of the **Data Analyst Internship – Task 5**. The objective was to perform Exploratory Data Analysis (EDA) using Python to uncover meaningful insights, patterns, and relationships from the Titanic dataset.

---

## 🧰 Tools & Libraries Used

- Python
- Jupyter Notebook
- Pandas
- Matplotlib
- Seaborn
- FPDF (for report generation)

---

## 📁 Dataset

- **Source:** [Kaggle Titanic Competition](https://www.kaggle.com/c/titanic/data)
- **File Used:** `train.csv`
- **Rows:** 891  
- **Columns:** 12 (PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked)

---

## 📌 Steps Performed

1. **Data Loading & Inspection**
   - Used `.head()`, `.info()`, `.describe()` to understand structure.
   - Checked for null values and unique counts.

2. **Univariate Analysis**
   - Histograms for `Age` and `Fare`
   - Bar plots for `Sex` and `Pclass`

3. **Bivariate Analysis**
   - Boxplot: `Age` vs `Survived`
   - Countplot: `Sex` vs `Survived`

4. **Multivariate Analysis**
   - Pairplot: `Survived`, `Age`, `Fare`, `Pclass`
   - Heatmap: Correlation matrix of numeric variables

5. **Report Generation**
   - Screenshots of each visual embedded
   - Final report created in PDF format

---

## 📌 Key Observations

- Most passengers were aged between 20–40; many fares were low, but a few high outliers exist.
- More males were on board, but females had a much higher survival rate.
- 3rd class had the highest number of passengers, while 1st class had better survival odds.
- Younger passengers and females had higher chances of survival.
- Higher fares and 1st-class tickets correlated with greater survival.
- Clear negative correlation between `Pclass` and `Fare`, and positive between `Fare` and `Survived`.
- Dataset had missing values in `Age` and `Cabin`, but no severe multicollinearity detected.

---

## 📌 Summary of Findings

### 1. Demographics & Survival Patterns
- **Females** had a much higher survival rate than males.
- **Children (Age < 10)** were more likely to survive.
- Survivors had a slightly lower median age than non-survivors.

### 2. Socioeconomic Impact
- **1st class** passengers had better survival odds.
- Negative correlation between `Pclass` and `Survived`.

### 3. Fare Distribution
- Right-skewed distribution with many low fares and few very high ones.
- Higher fare often indicated better survival chances.

### 4. Data Quality
- Missing values in `Age`, `Cabin`.
- No strong multicollinearity between numeric features.

### 5. Correlation Highlights
- Positive: `Fare` & `Survived`
- Negative: `Pclass` & `Survived`

---

## 📸 Visual Insights

Visuals included in the report:
- Histogram of Age & Fare
- Bar plots of Sex & Pclass
- Boxplot of Age vs Survival
- Countplot of Sex vs Survival
- Pairplot of numerical features
- Heatmap of correlations

---

## 📄 Files Included

- `train.ipynb` – Jupyter notebook with all code & visuals
- `Titanic_EDA_Report.pdf` – Final report with embedded screenshots
- `train.csv` – Titanic dataset
- `data_visualisation.py` – python code used in jupyter notebook for visualisation
- `README.md` – This file

---

## 🙌 Acknowledgements

Thanks to Kaggle for the open dataset and the internship mentors for this learning opportunity.

