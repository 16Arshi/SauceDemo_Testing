# 🧪 SauceDemo QA Project

This repository contains both **automation** and **manual testing** for the [SauceDemo](https://www.saucedemo.com/) web application, covering core functionalities such as **login**, **add to cart**, and **checkout**.

---

## 📁 Project Structure

SauceDemo_QA/
├── .venv/ # Virtual environment
├── Base_page/ # Page Object Model files
│ ├── init.py
│ ├── Add_to_cart.py
│ ├── checkout_items.py
│ └── Login_page.py
├── Logs/ # Log files
│ ├── logins.log
│ └── orangehrm.log
├── Manual_tetsing_pdf and Automation testing paased test cases video/
│ ├── Manual Testing Documentation for SauceDemo.pdf
│ └── saucedemo_video.mp4
| └──   Use_of_AI_and_Challenges_faced.txt
├── Reports/ # HTML test reports
│ ├── all_reports.html
│ ├── cart_test_report.html
│ └── assets/
├── Test_cases/ # Pytest test cases
│ ├── init.py
│ ├── conftest.py
│ ├── pytest.ini
│ ├── test_add_to_cart.py
│ ├── test_checkout_items.py
│ └── test_login_page.py
├── Test_data/ # Test data
│ └── login_test_data.py
├── Utilities/ # Utility functions/logging
│ └── coustom_log.py
├── run.bat # Batch file to run tests
└── README.md # Project documentation


---

## 🔧 Automation Testing

### ✅ Tools & Tech Used
- **Language:** Python
- **Framework:** PyTest
- **Automation Library:** Selenium WebDriver
- **Design Pattern:** Page Object Model (POM)
- **Reporting:** HTML reports via pytest-html

### ✅ Covered Test Scenarios
| Module      | Test Description                                 |
|-------------|--------------------------------------------------|
| Login       | Valid login, invalid login, locked user          |
| Add to Cart | Add all items to cart, remove specific items     |
| Checkout    | Complete checkout process with valid data        |

### 🚀 To Run Tests

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
Run all tests and generate HTML report:
           pytest --html=Reports/all_reports.html


Run specific test module:
           pytest Test_cases/test_login_page.py


Or use the batch file:
           run.bat

           
🧑‍🔬 Manual Testing
✅ Contents
Test Cases:
Documented in the PDF file
→ Manual Testing Documentation for SauceDemo.pdf

Bug Reports:
Structured and included within the same PDF file in table format

Video:
→ saucedemo_video.mp4 (optional walkthrough of test run)

📝 Custom Markers in PyTest
To run specific groups of tests using markers:
          pytest -m regression


Defined in pytest.ini:
[pytest]
markers =
    regression: marks tests as regression
    sanity: marks tests as sanity

    
📸 Screenshots & Logs
Log files are available in the Logs/ folder

HTML reports are stored in Reports/

Screenshots (optional) can be added for failed test scenarios

📌 Conclusion
This project provides a complete end-to-end QA solution with:

Automated functional tests (Login, Cart, Checkout)

Manual test case coverage

Bug documentation

Reports and logging for traceability

🤝 Author
Arshi Khan
Tools: Selenium, Python, PyTest, Logging, HTML Reporting
