# 💻 Laptop Price Predictor

A Machine Learning web application that predicts the estimated price of a laptop based on its hardware specifications.

The project uses **Python, Pandas, NumPy, Scikit-learn, and Streamlit** to build and deploy the prediction model.

---

## 📌 Project Overview

The **Laptop Price Predictor** takes laptop specifications as input and predicts its estimated price using a trained **Linear Regression** model.

The application provides a simple and interactive interface where users can select laptop specifications such as brand, RAM, processor, storage, GPU, operating system, screen size, and display features.

---

## ✨ Features

* 💻 Laptop price prediction
* 🏷️ Brand selection
* 🖥️ Laptop type selection
* 🧠 RAM selection
* ⚖️ Laptop weight input
* 👆 Touchscreen selection
* 🖼️ IPS display selection
* 📐 Screen resolution selection
* 📏 Automatic PPI calculation
* ⚙️ CPU selection
* 💾 HDD and SSD selection
* 🎮 GPU selection
* 🪟 Operating system selection
* 🌐 Interactive Streamlit interface

---

## 🛠️ Technologies Used

| Technology   | Purpose                             |
| ------------ | ----------------------------------- |
| Python       | Programming language                |
| Pandas       | Data manipulation and preprocessing |
| NumPy        | Numerical calculations              |
| Scikit-learn | Machine Learning                    |
| Streamlit    | Web application                     |
| Pickle       | Model serialization                 |

---

## 📂 Project Structure

```text
Laptop-Price-Predictor/
│
├── app.py
├── pipe.pkl
├── df.pkl
├── requirements.txt
└── README.md
```

### File Description

* **`app.py`** — Streamlit application
* **`pipe.pkl`** — Trained Machine Learning pipeline
* **`df.pkl`** — Processed dataset
* **`requirements.txt`** — Required Python packages
* **`README.md`** — Project documentation

---

## 🧠 Machine Learning Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Feature Engineering
   ↓
Feature Selection
   ↓
One-Hot Encoding
   ↓
Linear Regression
   ↓
Model Training
   ↓
Save Pipeline
   ↓
Streamlit Application
   ↓
Price Prediction
```

---

## 📊 Features Used

### Categorical Features

The following categorical features are encoded using `OneHotEncoder`:

* `Company`
* `TypeName`
* `Processor`
* `GpuBrand`
* `os`

### Numerical Features

The following numerical features are used by the model:

* `Ram`
* `Weight`
* `TouchScreen`
* `IPS`
* `ppi`
* `HDD`
* `SSD`

---

## 🔧 Feature Engineering

### Memory

The original `Memory` column contains values such as:

* `500 HDD`
* `512 SSD`
* `128 SSD + 1000 HDD`

The Memory feature is processed into separate numerical features:

| Memory             | HDD  | SSD |
| ------------------ | ---- | --- |
| 500 HDD            | 500  | 0   |
| 512 SSD            | 0    | 512 |
| 128 SSD + 1000 HDD | 1000 | 128 |

This allows the Machine Learning model to work with numerical storage values.

### PPI Calculation

The application calculates **Pixels Per Inch (PPI)** using screen resolution and screen size.

```python
ppi = ((x_res ** 2) + (y_res ** 2)) ** 0.5 / screen_size
```

For example:

```text
Resolution: 1920x1080
Screen Size: 15.6 inches
```

The application automatically calculates the corresponding PPI.

---

## 🤖 Machine Learning Model

The project uses **Linear Regression** to predict laptop prices.

### Categorical Feature Encoding

```python
categorical_columns = [
    'Company',
    'TypeName',
    'Processor',
    'GpuBrand',
    'os'
]
```

The categorical features are encoded using `OneHotEncoder`:

```python
one_hot_column_transformer = ColumnTransformer(
    transformers=[
        (
            'col_tnf',
            OneHotEncoder(
                sparse_output=False,
                drop='first',
                handle_unknown='ignore'
            ),
            categorical_columns
        )
    ],
    remainder='passthrough'
)
```

### Pipeline

The preprocessing and model are combined using a Scikit-learn Pipeline:

```python
model = LinearRegression()

pipe = Pipeline([
    ('one_hot_column_transformer', one_hot_column_transformer),
    ('model', model)
])
```

---

## 💾 Model Training and Saving

The model is trained using:

```python
pipe.fit(x_train, y_train)
```

The trained pipeline is saved using Pickle:

```python
pickle.dump(pipe, open('pipe.pkl', 'wb'))
```

The processed DataFrame is saved as:

```python
pickle.dump(df, open('df.pkl', 'wb'))
```

---

## 🌐 Streamlit Application

The application collects laptop specifications from the user.

### Example Input

| Feature     | Example       |
| ----------- | ------------- |
| Brand       | HP            |
| Type        | Notebook      |
| RAM         | 16 GB         |
| Weight      | 2.0 kg        |
| TouchScreen | Yes           |
| IPS         | Yes           |
| Screen Size | 15.6 inches   |
| Resolution  | 1920x1080     |
| CPU         | Intel Core i7 |
| HDD         | 1000 GB       |
| SSD         | 512 GB        |
| GPU         | Nvidia        |
| OS          | Windows       |

The user inputs are converted into a Pandas DataFrame:

```python
query = pd.DataFrame({
    'Company': [company],
    'TypeName': [type],
    'Ram': [ram],
    'Weight': [weight],
    'TouchScreen': [touchscreen],
    'IPS': [ips],
    'ppi': [ppi],
    'Processor': [cpu],
    'HDD': [hdd],
    'SSD': [ssd],
    'GpuBrand': [gpu],
    'os': [os]
})
```

The trained pipeline then predicts the price:

```python
prediction = pipe.predict(query)[0]
```

The predicted value is converted back from logarithmic scale:

```python
price = np.exp(prediction)
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

Navigate to the project directory:

```bash
cd Laptop-Price-Predictor
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not available:

```bash
pip install streamlit pandas numpy scikit-learn
```

---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

If the `streamlit` command is not recognized in PowerShell, use:

```bash
python -m streamlit run app.py
```

The application will open automatically in your default web browser.

---

## 📦 Requirements

Create a `requirements.txt` file containing:

```text
streamlit
pandas
numpy
scikit-learn
```

Install the dependencies using:

```bash
pip install -r requirements.txt
```

---

## ⚠️ Important Notes

* `pipe.pkl` must contain the trained Machine Learning pipeline.
* `df.pkl` must contain the processed dataset.
* The input features in `app.py` must match the features used during model training.
* The same preprocessing pipeline must be used during training and prediction.
* Numerical features must contain numerical values.
* If the training features or preprocessing configuration are changed, the model must be retrained and `pipe.pkl` must be recreated.

---

## 🔮 Future Improvements

* Implement Random Forest Regression
* Implement Gradient Boosting
* Implement XGBoost
* Compare multiple Machine Learning models
* Add MAE, MSE, RMSE, and R² evaluation metrics
* Improve Streamlit UI and styling
* Add laptop comparison functionality
* Add laptop recommendation functionality
* Add data visualization
* Deploy the application online

---

## 👨‍💻 Author

**Kaushal Raut**

MCA — Artificial Intelligence & Data Science

---

## 📄 License

This project is developed for **educational and portfolio purposes**.
