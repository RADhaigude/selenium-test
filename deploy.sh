#!/bin/bash

echo "🔁 Running Tests..."
./run_tests.sh

if [ $? -eq 0 ]; then
  echo "✅ Tests Passed - Deploying Application..."
  
  # Make sure target directory exists
  sudo mkdir -p /var/www/html/
  
  # Deploy the Allure report or app files
  sudo cp -r allure-report/* /var/www/html/
  
  echo "🚀 Deployment Complete"
else
  echo "❌ Deployment Aborted - Tests Failed!"
  exit 1
fi
