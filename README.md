# Project Setup Guide

## Setting Up a Virtual Environment and Installing Dependencies

Follow these steps to create a virtual environment and install the required dependencies for this project.

### 1️⃣ Create a Virtual Environment

Run the following command in your project directory:

#### **For Windows**

```sh
python -m venv venv
```

#### **For macOS/Linux**

```sh
python3 -m venv venv
```

This will create a `venv` folder containing the virtual environment.

---

### 2️⃣ Activate the Virtual Environment

#### **For Windows (Command Prompt)**

```sh
venv\Scripts\activate
```

#### **For Windows (PowerShell)**

```powershell
.\venv\Scripts\Activate
```

#### **For macOS/Linux**

```sh
source venv/bin/activate
```

After activation, your terminal should show `(venv)` at the beginning of the line.

---

### 3️⃣ Install Dependencies

Once the virtual environment is activated, install the required dependencies from `requirements.txt`:

```sh
pip install -r requirements.txt
```

This will install all necessary packages for the project.

---

### 4️⃣ Deactivating the Virtual Environment

Once you're done working, you can deactivate the virtual environment by running:

```sh
deactivate
```

---

### 🎯 You're all set! 🎯

You have successfully set up your virtual environment and installed the dependencies. Happy coding! 🚀
