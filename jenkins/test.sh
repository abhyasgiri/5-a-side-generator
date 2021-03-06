#!/bin/bash

sudo apt-get update
sudo apt-get install -y python3-venv python3-pip

#Test service 1
cd service_1
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate
cd ..

#Test service 2
cd service_2
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate
cd ..

#Test service 3
cd service_3
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate
cd ..

#Test service 4
cd service_4
python3 -m pytest --cov=application --cov-report xml --cov-report term-missing --junitxml junit.xml
deactivate
cd ..
