# Playwright Python Example

## Articles written about this project

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

When no browser was selected then chromium will be used.

* Run tests in pytest:

```
pytest
```

## Viewing Test Results

* View reports locally by navigate to the reports folder under the main folder of the project


* View Allure results locally by navigate to the project folder under the main folder of the project run the command:
```
allure serve
```

* View trace of playwright run the command:
```
npx playwright show-trace trace/trace.zip
```


## View Help And Custom CLI Options

```
pytest --help
```