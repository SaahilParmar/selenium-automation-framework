**File: troubleshooting\_log.md**

# Selenium Automation Framework – Troubleshooting Log

This document contains a chronological list of errors encountered during the setup and execution of the `selenium_automation_framework` project in GitHub Codespaces on an Android tablet. It includes actionable solutions that resolved each issue, aimed at helping other developers replicate this setup smoothly.

---

## ✅ Environment

* **Platform**: GitHub Codespaces
* **Device**: Xiaomi Android Tablet
* **Browser**: Google Chrome (Version 138.0.7204.49)
* **OS**: Linux (Codespaces container)

---

## 1. Error: `pytest: error: unrecognized arguments: --browser chrome --headless`

**Cause:** `pytest` CLI didn’t recognize custom arguments because `conftest.py` was empty.

**Solution:** Populated `conftest.py` with custom `pytest_addoption()` and a working `driver` fixture to handle CLI arguments.

---

## 2. Error: `collected 0 items`

**Cause:** `test_login.py` was empty — no test was defined.

**Solution:** Created and saved the `test_login_success(driver)` function with Selenium login logic.

---

## 3. Error: `WebDriver.__init__() got multiple values for argument 'options'`

**Cause:** Incorrect WebDriver instantiation.

**Solution:** Fixed driver initialization by passing `options=options` once and correctly using `webdriver.Chrome()`.

---

## 4. Error: `Service ... unexpectedly exited. Status code was: 127`

**Cause:** Chrome binary was not installed in the Codespaces container.

**Solution:** Installed Google Chrome manually:

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get update
sudo apt-get install -y ./google-chrome-stable_current_amd64.deb
```

---

## 5. Error: `TypeError: ChromeDriverManager.__init__() got an unexpected keyword argument 'version'`

**Cause:** Deprecated `version` argument was passed to `ChromeDriverManager()`.

**Solution:** Removed the `version` argument. Let `webdriver-manager` auto-detect the version.

---

## 6. Error: `ImportError: cannot import name 'ChromeType'`

**Cause:** The `ChromeType` symbol no longer exists in newer versions of `webdriver_manager`.

**Solution:** Removed all references to `ChromeType` import in `conftest.py`.

---

## 7. Error: `ValueError: There is no such driver by URL ...chromedriver_linux64.zip`

**Cause:** The specified Chrome version was not supported by available Chromedriver.

**Solution:** Installed Google Chrome directly instead of relying on the auto-downloader.

---

## 8. Error: `cannot find Chrome binary`

**Cause:** Headless Chrome was being called but no Chrome binary existed.

**Solution:** Installed Chrome as detailed in step 4 and verified installation with `google-chrome --version`.

---

## 9. Error: `NoSuchElementException: Unable to locate element: {name="username"}`

**Cause:** Test tried to interact with the login form before it was loaded.

**Solution:** Added `WebDriverWait` with `expected_conditions` for robust element detection:

```python
wait.until(EC.presence_of_element_located((By.NAME, "username")))
```

---

## 10. Error: `bash: allure: command not found`

**Cause:** Allure CLI was not installed or not in PATH.

**Solution:** Installed Allure manually:

```bash
wget https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.tgz
tar -zxvf allure-2.27.0.tgz
sudo mv allure-2.27.0 /opt/allure
sudo ln -s /opt/allure/bin/allure /usr/bin/allure
```

---

## 11. Success: `Report successfully created` ✅

**Final Confirmation:** Test results were generated, Allure report created and served locally using:

```bash
python3 -m http.server 8888 --directory allure-report
```

Opened in browser via GitHub Codespaces forwarded ports.

---

This troubleshooting log documents a real-world debugging and setup journey for a fully functional test automation framework using Selenium, pytest, and Allure inside GitHub Codespaces.
