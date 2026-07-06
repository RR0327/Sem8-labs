# ML Stroke Prediction Explanation

## 1. Import Libraries

- Imports all required Python libraries.
- These libraries are used for data processing, visualization, machine learning, and model evaluation.

---

## 2. Load Dataset

- Loads the Healthcare Stroke Dataset using **Pandas**.
- Displays the dataset size, column names, class distribution, and missing values.

---

## 3. Data Preprocessing

- Removes unnecessary columns such as **id**.
- Removes the rare **gender = "Other"** record.
- Fills missing BMI values using the **median**.
- Converts categorical data into numerical values using **Label Encoding**.

---

## 4. Handle Class Imbalance

- The dataset contains far fewer stroke cases than non-stroke cases.
- Uses **Oversampling** to increase the number of stroke samples.
- Creates a balanced dataset for better model training.

---

## 5. Feature and Target Split

- Splits the dataset into:
  - **Features (X)** – Input variables.
  - **Target (y)** – Stroke prediction.

---

## 6. Train-Test Split

- Divides the dataset into:
  - **80% Training Data**
  - **20% Testing Data**
- Uses stratified sampling to preserve class distribution.

---

## 7. Feature Scaling

- Uses **StandardScaler** to normalize feature values.
- Improves the performance of models such as Logistic Regression and SVM.

---

## 8. Train Machine Learning Models

- Trains four supervised learning models:
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - Support Vector Machine (SVM)

---

## 9. Make Predictions

- Each trained model predicts whether a patient is likely to have a stroke.
- Predictions are made using the testing dataset.

---

## 10. Model Evaluation

- Evaluates each model using:
  - Accuracy
  - Precision
  - Recall
  - F1-Score
- Prints the Classification Report for detailed performance analysis.

---

## 11. Model Comparison

- Displays the performance of all models in a comparison table.
- Makes it easier to identify the best-performing model.

---

## 12. Visualization

- Creates three visualizations:
  - Grouped Bar Chart for model comparison.
  - Confusion Matrix for each model.
  - Horizontal Bar Chart of F1-Scores.

---

## Why Use Data Preprocessing?

- Cleans the dataset before training.
- Handles missing values and converts categorical data into numerical form.

---

## Why Handle Class Imbalance?

- Prevents the model from favoring the majority class.
- Improves the prediction of stroke cases.

---

## Why Use Feature Scaling?

- Makes all features have the same scale.
- Improves the performance of scale-sensitive algorithms like Logistic Regression and SVM.

---

## Why Use Multiple Models?

- Different algorithms perform differently on the same dataset.
- Comparing multiple models helps identify the most accurate one.

---

## Why Use Accuracy?

- Measures the overall percentage of correct predictions.

### Formula

```
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```

---

## Why Use Precision?

- Measures how many predicted stroke cases are actually stroke cases.

### Formula

```
Precision = TP / (TP + FP)
```

---

## Why Use Recall?

- Measures how many actual stroke cases are correctly identified.

### Formula

```
Recall = TP / (TP + FN)
```

---

## Why Use F1-Score?

- Combines Precision and Recall into a single performance metric.
- Useful for imbalanced datasets.

### Formula

```
F1-Score = 2 × (Precision × Recall) / (Precision + Recall)
```

---

## Why Use Confusion Matrix?

- Shows the number of correct and incorrect predictions.
- Helps analyze model performance in detail.

---

## Program Flow

1. Import required libraries.
2. Load the Healthcare Stroke Dataset.
3. Preprocess the data.
4. Handle class imbalance using Oversampling.
5. Split features and target.
6. Divide data into training and testing sets.
7. Scale the feature values.
8. Train four supervised learning models.
9. Predict stroke outcomes.
10. Evaluate each model using performance metrics.
11. Compare all models.
12. Visualize the results using graphs.

---

## Supervised Models Used

### Logistic Regression

- A linear classification algorithm.
- Suitable for binary classification problems.

### Decision Tree

- Makes predictions using a tree-like structure.
- Easy to understand and interpret.

### Random Forest

- An ensemble of multiple Decision Trees.
- Produces more accurate and stable predictions.

### Support Vector Machine (SVM)

- Finds the optimal boundary between classes.
- Performs well on high-dimensional datasets.

---

## Very Simple Viva Explanation

> This project predicts whether a patient is likely to have a **stroke** using **Supervised Machine Learning**. First, the Healthcare Stroke Dataset is loaded and preprocessed by removing unnecessary data, handling missing values, and encoding categorical features. Since the dataset is imbalanced, **Oversampling** is applied to balance the classes. The data is then divided into training and testing sets, and feature scaling is performed. Four supervised learning models—**Logistic Regression, Decision Tree, Random Forest, and Support Vector Machine (SVM)**—are trained and evaluated using **Accuracy, Precision, Recall, and F1-Score**. Finally, the models are compared using tables, confusion matrices, and graphs to identify the best-performing model.
