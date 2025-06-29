# RESIDENCE_TIME_DISTRIBUTION
Simulated Residence Time Distribution (RTD) for PFR, CSTR, and tanks-in-series reactors using analytical models.


This project simulates and analyzes the Residence Time Distribution (RTD) for different reactor types using Python. RTD is a critical diagnostic tool for understanding the flow behavior and non-idealities within chemical reactors.

# Objective

To numerically model and compare RTD curves for:
- Ideal CSTR
- Ideal Plug Flow Reactor (PFR) (approximated)
- Tanks-in-Series model (non-ideal)

Key outputs include:
- Exit age distribution function E(t)
- Cumulative RTD function F(t)
- Mean residence time (τ)
- Variance (σ²) of the RTD

# Theory

- E(t): Describes the probability that a fluid element spends time 't' inside the reactor before exiting.
- F(t):The cumulative distribution function
  
 # Features

- RTD plots for **CSTR, PFR (Gaussian spike), and Tanks-in-Series**
- Cumulative curves **F(t)**
- Calculation of mean residence time and variance
- Supports extension for experimental RTD data fitting
- Visual outputs suitable for reports, portfolios, and analysis

# Tools & Libraries

- Python 3.x
- NumPy
- Matplotlib
- SciPy
- 
# How to Run

1. Clone the repository or download the `.py` script.
2. Install dependencies (if not already):

   ```bash
   pip install numpy matplotlib scipy
