#!/bin/bash

echo "Running Selenium Tests..."
pytest --alluredir=allure-results

echo "Generating Allure Report..."
allure generate allure-results --clean -o allure-report
