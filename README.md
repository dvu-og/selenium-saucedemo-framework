# SauceDemo Selenium Automation

UI test automation for https://www.saucedemo.com (a practice e-commerce site)
using Python, Selenium and pytest with the Page Object Model.

## Tests
- Valid login
- Invalid login (locked user, wrong password, empty fields)
- Add item to cart

## Tech stack
Python | Selenium 4 | pytest | pytest-html

## How to run
pip install -r requirements.txt
pytest -v

## What I learned
- Locators and explicit waits
- Page Object Model
- pytest fixtures and parametrized tests
