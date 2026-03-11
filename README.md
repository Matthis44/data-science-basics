# Data Science Basics

Portfolio of data science fundamentals covering NumPy, Pandas, and Scikit-learn through structured assignments and reference notebooks.

---

## Tech Stack

| Category | Libraries |
|---|---|
| **Numerical Computing** | `numpy` `scipy` |
| **Data Manipulation** | `pandas` `geopandas` |
| **Machine Learning** | `scikit-learn` |
| **Visualization** | `matplotlib` `descartes` |
| **Testing & Quality** | `pytest` `flake8` `pydocstyle` |
| **CI/CD** | GitHub Actions |

---

## Project Structure

```
data-science-basics/
├── numpy/                      # NumPy assignment
│   ├── numpy_questions.py
│   └── test_numpy_questions.py
├── pandas/                     # Pandas assignment (French referendum analysis)
│   ├── pandas_questions.py
│   ├── test_pandas_questions.py
│   └── data/                   # CSV + GeoJSON datasets
├── sklearn/                    # Scikit-learn assignment
│   ├── sklearn_questions.py
│   └── test_sklearn_questions.py
├── pandas_data_basics.ipynb   # Pandas reference notebook
└── sklearn_ml_basics.ipynb    # Scikit-learn reference notebook
```

---

## Modules

### NumPy

**Skills developed:**
- Multi-dimensional array indexing with `np.argmax()` and `np.unravel_index()`
- Mathematical series computation (Wallis product for π approximation)
- Input validation and custom `ValueError` handling
- Unit testing with `pytest`

---

### Pandas — French Referendum Analysis

Real-world data pipeline on French referendum results at town level (36,565 records across 13 regions).

**Skills developed:**

| Task | Techniques |
|---|---|
| Data loading | `pd.read_csv()` with custom delimiters |
| Table joining | `pd.merge()` with multi-key joins |
| Data cleaning | `dropna()`, `drop_duplicates()`, boolean filtering |
| Aggregation | `groupby()` + custom aggregation functions |
| Geospatial mapping | `geopandas`, GeoJSON, choropleth maps |

**Reference notebook** (`pandas_data_basics.ipynb`) also covers:
- `iloc` / `loc` selection and filtering (`isin`, `between`, `str.contains`)
- Type casting, `apply()`, lambda transformations
- Time-series operations: `pct_change`, `rolling`, `resample`, `interpolate`
- Merging strategies: inner / outer / right joins
- `GridSearchCV` pipelines integrating preprocessing and classifiers

---

### Scikit-learn — Custom Estimator & Cross-Validator

From-scratch implementations that are fully compliant with the scikit-learn API.

#### KNearestNeighbors Classifier

Custom k-NN inheriting from `BaseEstimator` + `ClassifierMixin`:

- `fit(X, y)` — store training data, validate with `check_X_y()`
- `predict(X)` — pairwise Euclidean distances + majority voting via `np.argsort()`
- `score(X, y)` — classification accuracy
- Passes `check_estimator()` for full API compliance
- Validated against `sklearn.neighbors.KNeighborsClassifier` for k ∈ {1, 3, 5, 7}

#### MonthlySplit Cross-Validator

Time-series aware cross-validator inheriting from `BaseCrossValidator`:

- `get_n_splits()` — counts unique months in a `DatetimeIndex`
- `split()` — yields consecutive monthly train/test index pairs, preserving temporal order
- Compatible with both index-based and column-based datetime inputs
- Supports shuffled data and multi-dimensional features

**Skills developed:**
- Scikit-learn API design patterns (BaseEstimator, ClassifierMixin, BaseCrossValidator)
- Distance-based learning (`pairwise_distances`)
- Time-series cross-validation design
- Docstring conventions (`pydocstyle`)
- PEP8 compliance (`flake8`)
- CI/CD pipelines with GitHub Actions

---

## Testing

Each module includes a full `pytest` test suite and a GitHub Actions workflow that runs on every push:

```bash
# Run tests for any module
cd numpy && pytest test_numpy_questions.py
cd pandas && pytest test_pandas_questions.py
cd sklearn && pytest test_sklearn_questions.py
```

---

## Key Competencies

- **Data Engineering** — ETL pipelines, merging, aggregation, time-series handling, missing value treatment
- **Machine Learning** — Supervised learning (classification & regression), k-NN, SVM, Random Forest, Gradient Boosting, Logistic Regression, Ridge/Lasso/ElasticNet
- **Model Evaluation** — Cross-validation, `GridSearchCV`, accuracy metrics, pipelines
- **Geospatial Analysis** — GeoDataFrame operations, GeoJSON parsing, choropleth mapping
- **Software Practices** — Unit testing, code quality enforcement, CI/CD, API-compliant custom implementations
