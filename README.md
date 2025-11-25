# Selenium Pytest Demo Project

This is a demo for Selenium, PyTest, Github actions, parallel testing, publish allure report with gh-page

## Key points
- Selenium tests with PyTest(POM, fixtures designed)
- Use pytest-xdist for running test in parallel
- Take screenshot while test failed and attach it to Allure report
- Integrate with GitHub Actions for CI/CD
- Publish Allure report to gh-pages after testing finished

## Notes
- Only "saucedemo" Env for demo purpose
- Support browser: chrome and firefox, but firefox not be integrated to pipeline

## Run at local
- Needs to create a .env file with content:
```
BASE_URL=https://www.saucedemo.com/
USERNAME=standard_user
PASSWORD=secret_sauce
```
- Run with command
```angular2html
pytest tests
```