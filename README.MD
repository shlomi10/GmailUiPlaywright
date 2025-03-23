# 🤖 Google Workspace Registration Automation

![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Allure](https://img.shields.io/badge/Allure-C70D2C?style=for-the-badge&logo=allure&logoColor=white)

## Overview

This project provides an automated testing framework for Google Workspace registration flows using Playwright, Pytest, and Allure reporting. It validates the user registration process across various scenarios and edge cases to ensure the functionality works as expected.

## 🌟 Key Features

- **Page Object Model Design** - Clean separation of test logic and UI interactions
- **Comprehensive Test Coverage** - Tests account creation, password validation, and error handling
- **Detailed Reporting** - Allure integration for beautiful, detailed test reports
- **Screenshot Capture** - Automatic screenshots on test failures for easier debugging
- **Playwright Tracing** - Full interaction recording for detailed debugging
- **Randomized Testing Data** - Uses Faker to generate unique test data for each run
- **Browser Emulation** - Randomized user agents to prevent automation detection
- **Parallel Test Execution** - Run tests simultaneously for faster feedback

## 📋 Test Scenarios

The framework validates various aspects of the Google Workspace registration process:

1. **Basic User Registration** - Create a new account with valid information
2. **Password Functionality** - Test password visibility toggle button
3. **Email Availability Check** - Verify detection of already used email addresses
4. **Email Suggestions** - Validate email suggestion functionality

## 🛠️ Project Structure

```
├── pages/                  # Page Object Models
│   ├── basePage.py         # Base page with common methods
│   ├── add_mobile_phone_page.py
│   ├── basic_information_page.py
│   ├── choose_email_address.py
│   ├── create_account_page.py
│   ├── create_password_page.py
│   └── google_workspace_page.py
├── tests/
│   ├── base_class.py       # Test base class with fixture setup
│   ├── conftest.py         # Pytest configuration
│   └── test_google_workspace.py  # Test cases
├── utils/
│   └── .env                # Environment variables
├── screenshots/            # Failure screenshots (generated during test runs)
├── trace/                  # Playwright trace files (for debugging)
├── reports/                # Generated test reports
└── README.md               # Project documentation
```

## 🚀 Setup Instructions

### Prerequisites

- Python 3.12+
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shlomi10/GmailUiPlaywright.git
   cd google-workspace-automation
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Playwright browsers:
   ```bash
   playwright install
   ```

## 🧪 Running Tests

### Basic Test Execution

```bash
pytest
```

### With HTML Reports

```bash
python -m pytest tests/ --html-report=./reports
```

### With Console Output

```bash
python -m pytest -s tests/ --html-report=./reports
```

### Parallel Execution

```bash
python -m pytest -s -n auto tests/ --html-report=./reports
```

## 📊 Viewing Test Results

### HTML Reports

Navigate to the `reports` folder after test execution to view HTML reports.

### Allure Reports

Generate and view Allure reports:

```bash
allure serve
```

### Playwright Traces

View detailed interaction recordings for debugging:

```bash
npx playwright show-trace trace/trace.zip
```

## 🔍 Configuration

The `.env` file contains configuration parameters:

```
BASE_URL=https://workspace.google.com/intl/en/gmail/
NAME=example_name
USED_EMAIL=example_email
SHLOMI=example_value
TEST=example_value
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.