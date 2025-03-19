# Automating Google Workspace User Registration Testing with Pytest and Allure

## Overview

This project is designed to automate and validate the Google Workspace user registration process using Pytest, Playwright, and Allure. By leveraging modern testing frameworks, it ensures that user registration functions correctly across different scenarios while providing detailed reports and traceability.

With built-in parallel execution, detailed HTML reports, and Allure-based test documentation, this framework helps streamline UI testing, debugging, and reporting, making it an essential tool for QA engineers and developers.

## Key Features
✅ Automated UI Testing – Uses Playwright for browser automation

✅ Comprehensive Test Reporting – Allure reports for clear visualization

✅ Parallel Test Execution – Speed up testing with Pytest’s multi-threading

✅ Customizable Browser Options – Run tests in Chromium, Firefox, and more

✅ Playwright Tracing – Debug failed tests with detailed execution traces

## Project Setup

* Clone the project
* Navigate to the project directory

* Install requirements (dependencies) by running the following command:
```
pip install -r requirements.txt 
```

## Running Tests with report

```
python -m pytest tests/ --html-report=./reports
```

## Running Tests with report and see the output under the console
```
python -m pytest -s tests/ --html-report=./reports
```

## Running Tests in parallel with report and see the output under the console
```
python -m pytest -s -n auto tests/ --html-report=./reports
```

When no browser is selected, Chromium will be used by default.

* Run tests in pytest:

```
pytest
```

## Viewing Test Results

* View reports locally by navigating to the reports folder under the main project directory.


* View Allure results locally by navigating to the project folder and running the command:
```
allure serve
```

* View trace of Playwright by running the command:
```
npx playwright show-trace trace/trace.zip
```


## View Help And Custom CLI Options

```
pytest --help
```