# Python

This repository is a personal workspace for testing and experimenting with Python, statistics, data science, and machine learning. It includes:

- **Python Basics**: Fundamental concepts and practice exercises in Python programming.
- **Statistics**: Explorations of statistical methods and analyses, essential for data-driven insights.
- **Data Science**: Projects and tutorials focused on data manipulation, visualization, and analytics.
- **Machine Learning**: Implementations of various machine learning models and techniques, from basics to advanced methods.

Whether you are following along or diving into specific topics, this repository serves as a hands-on lab for learning and applying Python skills in data analysis and machine learning.

---

# How to Activate a Python Virtual Environment in Windows

Follow these steps to create and activate a Python virtual environment on Windows using PowerShell. This will also include setting the execution policy to allow the activation script to run.

---

## Step 1: Set the PowerShell Execution Policy

1. **Open PowerShell as Administrator**:
   - Right-click on the Start menu and select **Windows PowerShell (Admin)**.

2. **Set the Execution Policy**:
   - Enter the following command to allow PowerShell to run scripts:

     ```powershell
     Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
     ```

   - When prompted, type **"A"** for "Yes to All" to confirm.

---

## Step 2: Create the Virtual Environment

1. **Navigate to the Project Directory**:
   - Use the `cd` command to move to the folder where you want to create the environment:

     ```powershell
     cd path\to\your\project
     ```

2. **Create the Environment**:
   - Run the following command to create a virtual environment. Replace `env_name` with your preferred name for the environment:

     ```powershell
     python -m venv env_name
     ```

---

## Step 3: Activate the Virtual Environment

1. **Activate the Environment**:
   - To activate the environment in PowerShell, use the following command:

     ```powershell
     .\env_name\Scripts\Activate
     ```

   - After activation, `(env_name)` should appear at the beginning of the PowerShell prompt.

2. **Deactivate the Environment**:
   - When finished, deactivate the environment with:

     ```powershell
     deactivate
     ```

---

## Summary of Commands

Here’s a quick list of the commands:

- **Set execution policy**:

  ```powershell
  Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
  ```

- **Navigate to project directory**:
  
  ```powershell
  cd path\to\your\project
  ```

- **Create virtual environment**:
  
  ```powershell
  python -m venv env_name
  ```

- **Activate environment**:

  ```powershell
  .\env_name\Scripts\Activate
  ```

- **Deactivate environment**:

  ```powershell
  deactivate
  ```

---

This guide will help you easily create, activate, and deactivate a Python virtual environment in Windows PowerShell!
