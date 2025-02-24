import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

#######################################
# 1) Setup: Define the Portfolio Parameters
#######################################
st.set_page_config(layout="wide")
st.title("📊 Understanding Markowitz Portfolio Optimization")
st.markdown("Explore how to balance expected return and risk through optimal diversification.")

# Sidebar: Explain assets and allow target return selection
with st.sidebar:
    st.header("⚙️ Portfolio Parameters")
    st.markdown("""
    **Assumed Assets:**
    - **Asset A:** Expected Return = 8%, Volatility = 10%
    - **Asset B:** Expected Return = 12%, Volatility = 15%
    - **Asset C:** Expected Return = 15%, Volatility = 20%
    """)
    # Target return slider (in decimals)
    target_return = st.slider("Target Portfolio Return", 0.07, 0.16, 0.12, step=0.005)

# Define the expected returns and covariance matrix
mu = np.array([0.08, 0.12, 0.15])
cov_matrix = np.array([
    [0.01,   0.003,  0.002],
    [0.003,  0.0225, 0.009],
    [0.002,  0.009,  0.04]
])

#######################################
# 2) Markowitz Optimization Function
#######################################
def markowitz_opt(target, mu, cov):
    """
    Computes the optimal portfolio weights for a given target return
    using the analytical solution of the Markowitz optimization problem.
    
    Parameters:
    - target: Desired portfolio return.
    - mu: Expected returns vector.
    - cov: Covariance matrix of asset returns.
    
    Returns:
    - weights: Optimal asset weights.
    - port_return: Portfolio expected return.
    - port_std: Portfolio risk (standard deviation).
    """
    inv_cov = np.linalg.inv(cov)
    ones = np.ones(len(mu))
    A = ones.T @ inv_cov @ ones
    B = ones.T @ inv_cov @ mu
    C = mu.T @ inv_cov @ mu
    D = A * C - B**2
    
    # Lagrange multipliers from the constrained minimization:
    lambda_ = (C - B * target) / D
    gamma = (A * target - B) / D
    weights = inv_cov @ (lambda_ * ones + gamma * mu)
    
    # Calculate the achieved portfolio return and risk
    port_return = weights @ mu
    port_variance = weights.T @ cov @ weights
    port_std = np.sqrt(port_variance)
    return weights, port_return, port_std

# Compute the optimal portfolio for the selected target return
weights_opt, port_return, port_risk = markowitz_opt(target_return, mu, cov_matrix)

#######################################
# 3) Display the Interactive Results
#######################################
col1, col2 = st.columns(2)

with col1:
    st.subheader("Optimal Portfolio Composition")
    asset_names = ["Asset A", "Asset B", "Asset C"]
    for name, w in zip(asset_names, weights_opt):
        st.write(f"**{name}:** {w*100:.2f}%")
    st.write(f"**Expected Return:** {port_return*100:.2f}%")
    st.write(f"**Portfolio Risk (Std Dev):** {port_risk*100:.2f}%")

with col2:
    # Compute the efficient frontier by varying the target return
    frontier_returns = np.linspace(0.07, 0.16, 100)
    frontier_risks = []
    for r_target in frontier_returns:
        _, _, risk = markowitz_opt(r_target, mu, cov_matrix)
        frontier_risks.append(risk)
    frontier_risks = np.array(frontier_risks)
    
    # Plot the efficient frontier and highlight the chosen portfolio
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(frontier_risks*100, frontier_returns*100, 'b-', label="Efficient Frontier")
    ax.scatter(port_risk*100, port_return*100, color='red', marker='o', s=100, label="Selected Portfolio")
    ax.set_xlabel("Portfolio Risk (Standard Deviation %)")
    ax.set_ylabel("Portfolio Expected Return (%)")
    ax.set_title("Efficient Frontier")
    ax.grid(True, alpha=0.3)
    ax.legend()
    st.pyplot(fig)

st.markdown("""
---
**Pedagogical Insights:**

- **Diversification:** By combining assets with different risk–return profiles, the overall portfolio risk can be reduced.
- **Efficient Frontier:** The blue curve shows the set of portfolios that offer the best possible return for each level of risk.
- **Trade-Off:** Moving to the right along the curve increases expected return at the cost of higher risk.
""")

#######################################
# 4) Additional Tabs: Theory, Tutorial, and Labs
#######################################
tab1, tab2, tab3 = st.tabs(["📚 Theory Behind the Model", "📖 Comprehensive Tutorial", "🛠️ Practical Labs"])

with tab1:
    st.markdown("""
    ## Theoretical Foundations
    
    **Mean–Variance Framework:**  
    The Markowitz model selects portfolios by minimizing variance for a given target return, under the constraint that all weights sum to 1.
    
    **Key Equations:**
    
    - **Portfolio Return:**  
      $$ R_p = \\sum_{i=1}^{N} w_i \\mu_i $$
    
    - **Portfolio Variance:**  
      $$ \\sigma_p^2 = \\sum_{i=1}^{N}\\sum_{j=1}^{N} w_i w_j \\sigma_{ij} $$
    
    **Optimization Problem:**  
    Minimize $$\\sigma_p^2$$ subject to  
      $$\\sum_{i=1}^{N} w_i = 1 \\quad \\text{and} \\quad \\sum_{i=1}^{N} w_i \\mu_i = R_p.$$
    
    The solution of this problem gives rise to the **efficient frontier**, illustrating the risk–return trade-off.
    """)

with tab2:
    st.markdown("""
    ## Step-by-Step Tutorial
    
    1. **Set a Target Return:**  
       Use the sidebar slider to choose a desired portfolio return.
       
    2. **Compute Optimal Weights:**  
       The app calculates weights using:
       $$ w = \\Sigma^{-1}\\left(\\frac{C - B R}{D} \\cdot \\mathbf{1} + \\frac{A R - B}{D} \\cdot \\mu\\right) $$
       where:
       - $$ A = \\mathbf{1}^T \\Sigma^{-1} \\mathbf{1} $$
       - $$ B = \\mathbf{1}^T \\Sigma^{-1} \\mu $$
       - $$ C = \\mu^T \\Sigma^{-1} \\mu $$
       - $$ D = AC - B^2 $$
       
    3. **Visualize the Efficient Frontier:**  
       The plot shows how risk and return trade off across different portfolios, with your chosen portfolio marked in red.
       
    4. **Interpretation:**  
       - **Lower Risk:** Portfolios on the left of the frontier offer lower returns.
       - **Higher Return:** Moving right increases return at the cost of increased risk.
    """)

with tab3:
    st.markdown("""
    ## Practical Labs
    
    **Lab 1: Exploring Diversification**
    
    - **Objective:** Observe how the optimal weights change as you adjust the target return.
    - **Experiment:** Slide the target return and note the rebalancing among assets.
    
    **Lab 2: Risk–Return Trade-Off**
    
    - **Objective:** Identify the “knee” of the efficient frontier where increases in risk yield diminishing returns.
    - **Experiment:** Compare portfolio risk levels across different target returns.
    
    **Reflection Questions:**
    
    - How does diversification help in reducing overall portfolio risk?
    - What happens to asset weights as the desired return moves closer to the highest individual asset return?
    """)

st.markdown("""
---
**Disclaimer:**  
This tool is for educational purposes only. The presented Markowitz optimization is a simplified example and does not account for real-world constraints like transaction costs or short-selling limits.
""")
    
