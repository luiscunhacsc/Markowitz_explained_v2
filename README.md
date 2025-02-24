# Markowitz Portfolio Optimization Explained

## 1. What Is This?

The **Markowitz Portfolio Optimization** model—also known as the **Mean–Variance Framework**—is a cornerstone of modern portfolio theory. It helps investors construct an optimal portfolio by balancing expected return against risk (measured by variance or standard deviation).

This project features an interactive application where you can:

- **Set a Target Return:** Adjust your desired portfolio return using a slider.
- **Compute Optimal Weights:** See how the analytical solution of the Markowitz model allocates weights among assets.
- **Visualize the Efficient Frontier:** Explore the trade-off between risk and return, with your selected portfolio highlighted.

## 2. Setting Up a Local Development Environment

### 2.1 Prerequisites

1. **A Computer** (Windows, macOS, or Linux).
2. **Python 3.9 or higher** (Python 3.12 preferred).  
   - If you do not have Python installed, visit [python.org/downloads](https://www.python.org/downloads/) to install the latest version.
3. **Visual Studio Code (VS Code)**  
   - Download from [code.visualstudio.com](https://code.visualstudio.com/)
4. **Git** (optional but recommended for cloning the repository).  
   - Install from [git-scm.com/downloads](https://git-scm.com/downloads)

### 2.2 Downloading the Project

#### Option 1: Cloning via Git (Recommended)

1. Open **Terminal** (macOS/Linux) or **Command Prompt/PowerShell** (Windows).
2. Navigate to the folder where you want to download the project:
   ```bash
   cd Documents
   ```
3. Run the following command:
   ```bash
   git clone https://github.com/luiscunhacsc/Markowitz_explained_v2.git
   ```
4. Enter the project folder:
   ```bash
   cd Markowitz_explained_v2
   ```

#### Option 2: Download as ZIP

1. Visit [https://github.com/luiscunhacsc/Markowitz_explained_v2](https://github.com/luiscunhacsc/Markowitz_explained_v2)
2. Click **Code > Download ZIP**.
3. Extract the ZIP file into a local folder.

### 2.3 Creating a Virtual Environment

It is recommended to use a virtual environment (`venv`) to manage dependencies:

1. Open **VS Code** and navigate to the project folder.
2. Open the integrated terminal (`Ctrl + ~` in VS Code or via **Terminal > New Terminal**).
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

### 2.4 Installing Dependencies

After activating the virtual environment, install the required dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This installs libraries such as:
- **Streamlit** (for the interactive UI)
- **NumPy** (for numerical computations)
- **Matplotlib** (for plotting the efficient frontier)

## 3. Running the Application

To launch the application, execute:

```bash
streamlit run markowitz.py
```

A new tab should open in your web browser displaying the interactive tool. If it does not open automatically, check the terminal for a URL (e.g., `http://localhost:8501`) and open it manually.

### 3.1 Troubleshooting

- **ModuleNotFoundError:** Ensure your virtual environment is activated (`venv\Scripts\activate` on Windows or `source venv/bin/activate` on macOS/Linux).
- **Python not recognized:** Verify that Python is installed and added to your system's PATH.
- **Browser does not open:** Manually enter the provided URL (e.g., `http://localhost:8501`) into your browser.

## 4. Editing the Code

To modify the application:
1. Open `markowitz.py` in **VS Code**.
2. Make your changes and save the file.
3. Restart the Streamlit app after changes by stopping it with `Ctrl + C` and rerunning:
   ```bash
   streamlit run markowitz.py
   ```

## 5. Additional Resources

- **Streamlit Documentation:** [docs.streamlit.io](https://docs.streamlit.io)
- **Markowitz Portfolio Theory:** [Investopedia Guide](https://www.investopedia.com/terms/m/modernportfoliotheory.asp)
- **Modern Portfolio Theory (Wikipedia):** [Modern Portfolio Theory](https://en.wikipedia.org/wiki/Modern_portfolio_theory)

## 6. Support

For issues or suggestions, please open an **Issue** on GitHub:  
[https://github.com/luiscunhacsc/Markowitz_explained_v2/issues](https://github.com/luiscunhacsc/Markowitz_explained_v2/issues)

---

*Happy optimizing your portfolio!*

*Author: Luís Simões da Cunha*
```