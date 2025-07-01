# Selenium Automation Framework ✅

A complete **Selenium + Pytest test automation framework** designed for cross-browser testing, Allure reporting, and CI/CD integration with GitHub Actions.


![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/SaahilParmar/selenium-automation-framework/selenium-tests.yml?branch=main)
![Python Version](https://img.shields.io/badge/python-3.12-blue)
![License](https://img.shields.io/github/license/SaahilParmar/selenium-automation-framework)


## 1. 📁 Project Structure
![Project Structure](assets/1_project_structure.png)



![Selenium Structure](assets/selenium_structure.jpg)




## 2. 🧠 Features of This Framework

1. ✅ Modular Pytest + Selenium setup
2. ✅ CLI browser and headless test control
3. ✅ Cross-platform ready (Linux, Codespaces, Local)
4. ✅ Allure reporting support
5. ✅ GitHub Actions CI/CD integration
6. ✅ Professional error handling and logging
7. ✅ Easily extendable for large teams or real-world use


## 3. 🚀 Setup Instructions


### 3.1 Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/selenium-automation-framework.git
cd selenium-automation-framework
```

### 3.2 Create and Activate Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```
##### Reference Image for Activating Virtual Environment.
![Venv Setup](assets/8_venv.jpg)

### 3.3 Install Dependencies
```bash
pip install -r requirements.txt
```
##### Reference Image for installing dependencies.
![Requirements](assets/9_requirements.jpg)




## 4. 🧪 Running the Tests

### 4.1 Basic Test Run (Chrome + Headless)
```bash
pytest --browser chrome --headless --alluredir=reports/
```
##### Reference Image for test run for Chrome + Headless.
![Test Run](assets/11_test_pass.jpg)



### 4.2 Run with Visible Browser (Non-headless)
```bash
pytest --browser chrome --alluredir=reports/
```
![Test Run](assets/non_head.jpg)



## 5. 📊 View Allure Report


> Make sure you have Allure installed:
> [Installation Guide → https://docs.qameta.io/allure/]


### 5.1 To Serve the Report:
```bash
allure serve reports/
```
This opens an interactive test report in your browser.
![Report 1](assets/report_1.jpg)





## 6. 🛠 Available CLI Options


| Argument        | Description                                | Example                       |
|-----------------|--------------------------------------------|-------------------------------|
| `--browser`      | Browser to run tests (e.g., chrome)        | `--browser chrome`            |
| `--headless`     | Run without UI                             | `--headless`                 !
| `--alluredir`    | Directory to save Allure results           | `--alluredir=reports`        |

## 7. 🔄 CI/CD Integration (GitHub Actions)

This project includes a CI workflow located at:

```
.github/workflows/selenium-tests.yml
```

It runs on every push to `main`:
- ✅ Sets up environment
- ✅ Installs dependencies
- ✅ Runs headless tests
- ✅ Optionally uploads results

> To trigger: simply `git push` your code!




## 8. 🐛 Troubleshooting

All known errors and solutions have been logged in:

```
troubleshooting_log.md
```


This includes:
- Chromedriver errors
- NoSuchElement exceptions
- GitHub Actions failures
- Push errors and LFS issues


##### Reference Image for chrome installation.
![Chrome Installation 1](assets/1_chrome_install.jpg)
![Chrome Installation 2](assets/2_chrome_install.jpg)
![Chrome Installation 3](assets/3_chrome_install.jpg)
![Chrome Installation 4](assets/4_chrome_install.jpg)
![Chrome Installation 5](assets/5_chrome_install.jpg)
![Chrome Installation 6](assets/6_chrome_install.jpg)
![Chrome Installation 7](assets/7_chrome_install.jpg)




## 9. 🖼️ Screenshots

# Install Allure CLI (if not already)
# Mac: brew install allure
# Windows: choco install allure
# Linux: see https://docs.qameta.io/allure/

### 9.1 Allure Report Sample:
![Report 2](assets/report_2.jpg)
![Report 3](assets/report_3.jpg)
![Report 4](assets/report_4.jpg)
![Report 5](assets/report_5.jpg)
![Report 6](assets/report_6.jpg)
![Report 7](assets/report_7.jpg)
![Report 8](assets/report_8.jpg)




## 10. 📌 Dependencies

- `selenium`
- `pytest`
- `webdriver-manager`
- `allure-pytest`

Install all using:
```bash
pip install -r requirements.txt
```




## 11. 🔖 License

This project is licensed under the **MIT License**.
Feel free to modify and use for educational or professional use.
## 12. 👨‍💻 Author

**Saahil Parmar**
Test Automation Engineer in Progress 💻
_Reach out via GitHub for collaboration or questions!_

## 🎯 Why This Project?

This project was created to demonstrate my ability to design, build, and maintain a robust, scalable, and professional-grade test automation framework using industry-standard tools. It showcases not only my technical skills in Python, Selenium, and Pytest, but also my understanding of best practices in test architecture, reporting, and CI/CD integration.

Key goals for this project:
- **Real-World Readiness:** The framework is structured for easy extension and team collaboration, mirroring what’s needed in modern software teams.
- **Maintainability:** Modular code, clear documentation, and error handling make it easy to update and scale.
- **Professional Practices:** Includes Allure reporting, GitHub Actions CI/CD, and troubleshooting logs to reflect real engineering workflows.
- **Cross-Platform Support:** Designed to run seamlessly on local machines, Linux servers, and cloud environments like GitHub Codespaces.

By building this framework from scratch, I aimed to prove my readiness for a test automation engineering role and my commitment to delivering high-quality, maintainable solutions.
