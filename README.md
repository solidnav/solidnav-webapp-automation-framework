# WebApp Automation Framework

## Overview

This is a simple yet scalable automation framework for web application testing, designed to demonstrate industry-standard practices in Automation QA.

The framework is built using:
- [Selenium WebDriver](https://www.selenium.dev/)
- [Pytest/TestNG] (choose your framework)
- Page Object Model (POM) design pattern
- Modular, extensible architecture
- Integrated with GitHub Actions for CI/CD

> Purpose: To automate functional test cases for a sample web application (Demo site: [https://demo.opencart.com/](https://demo.opencart.com/)).

---

## Technology Stack

| Tool | Purpose |
|:-----|:--------|
| Python / Java | Programming Language |
| Selenium WebDriver | Browser automation |
| Pytest / TestNG | Test framework |
| Allure Reports / Extent Reports | Reporting |
| GitHub Actions | CI/CD Pipeline |
| ConfigParser / .properties | External configuration management |
| Logging module / Log4j | Logging |

---

## Project Structure

```bash
webapp-automation-framework/
├── src/
│   ├── pages/        # Page Object Model classes
│   ├── tests/        # Test cases
│   ├── utils/        # Driver factory, config readers, loggers
│   ├── resources/    # Config files, test data
├── reports/          # Test execution reports
├── .github/workflows/ # GitHub Actions CI configs
├── README.md
├── requirements.txt / pom.xml
└── .gitignore
