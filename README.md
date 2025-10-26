# 📱 Appium + Python Mobile Automation Framework

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![Appium](https://img.shields.io/badge/Appium-3.0-00ADD8?logo=appium)](https://appium.io/)
[![Pytest](https://img.shields.io/badge/Pytest-Framework-green)](https://docs.pytest.org/)
[![Allure](https://img.shields.io/badge/Allure-Reports-orange)](https://docs.qameta.io/allure/)
[![Jenkins](https://img.shields.io/badge/Jenkins-CI%2FCD-red)](https://www.jenkins.io/)

---

A complete **mobile automation framework** built with **Appium 3.0**, **Python**, and **Pytest**.  
Supports both **iOS** and **Android** platforms, with integrated reporting and CI/CD support.

---

## 🚀 Features

- Appium 3.0 integration with XCUITest & UiAutomator2  
- Page Object / Page Factory architecture  
- Config-driven execution (`config.json`)  
- Supports **parallel execution**  
- Generates detailed **Allure** & **HTML reports**  
- Jenkins integration for CI/CD pipelines  
- Real-device and simulator execution  
- Read data dynamically from Excel or config files  

---

## 🧰 Project Structure

AllureReports/ # Allure reports output directory
config.json # Test configuration (devices, app paths, etc.)
PageObjects/ # Page Object classes
TestCases/ # Test case scripts
Utilities/ # Helper utilities (logging, data readers, etc.)
pytest.ini # Pytest configuration

yaml
Copy code

---

## 🧩 Installation

```bash
git clone https://github.com/your-username/AppiumFW.git
cd AppiumFW
pip install -r requirements.txt
⚙️ How to Run Tests
Run all tests:

bash
Copy code
pytest -v --alluredir=AllureReports
Generate and view Allure reports:

bash
Copy code
allure serve AllureReports
Run a specific test case:

bash
Copy code
pytest TestCases/test_login.py -v
Run tests in parallel:

bash
Copy code
pytest -n 2 --alluredir=AllureReports
🧠 Author
Daryna Chuzhova
Mobile QA Automation Engineer
GitHub Profile

🏁 License
This project is licensed under the MIT License
