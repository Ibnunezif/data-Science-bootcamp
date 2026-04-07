# Statistical Engineering & Simulation

## 📌 Project Overview

This project implements a statistical engine from scratch using pure Python.
It performs data analysis and simulates probabilistic events using Monte Carlo simulation.

---

## 🧠 Mathematical Logic

### Mean

Sum of all values divided by total count.

### Median

* Odd: middle value
* Even: average of two middle values

### Variance

* Population: divide by **n**
* Sample: divide by **(n - 1)** (Bessel’s correction)

### Standard Deviation

Square root of variance.

---

## ⚠️ Why Mean Alone is Dangerous

In startup salary datasets, extreme values (like CEO salaries) distort the mean.
Standard deviation helps show the true variability.

---

## 🎲 Law of Large Numbers

As sample size increases, simulated probability approaches theoretical probability (0.045).

* 30 days → inaccurate
* 365 days → closer
* 10000 days → very accurate

---

## ⚙️ Setup Instructions

```bash
git clone <your-repo-link>
cd statistical_engine
python main.py
```

---

## 🧪 Run Tests

```bash
python -m unittest discover tests
```

---

## ✅ Acceptance Criteria

* ✔ Handles empty data
* ✔ Handles invalid data types
* ✔ Supports multimodal distributions
* ✔ Correct sample vs population variance
* ✔ Detects outliers correctly
