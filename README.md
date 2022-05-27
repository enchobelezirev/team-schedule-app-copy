# Team Schedule AI - API 
## Virtual environment
### Create virtual environment

    python -m venv venv

### Enter virtual environment

#### Windows (powershell): 

    . venv\Scripts\activate

#### Unix or MacOS : 

    source venv/bin/activate

## Installing packages

     pip install -r .\requirements.txt 

  Make sure you are inside venv first.

# How to run static code analysis

## Go to the main directory and activate the virtual environment

## Black

    python -m black --line-length=150 .

## Isort

    python -m isort --line-length=150 --profile black .

## Flake8
    
    flake8 --tee --format=gl-codeclimate --max-line-length=120 --ignore=E203,E501,W503 --exclude venv,dist .
  
## Deployment to Azure
1. Go to the root directory of the project
2. Activate the venv
3. Install requirements if not already installed
4. `az login`
5. `az webapp up -n time-schedule-poc --sku F1`
6. (optional) if you want to observe the logs, execute `az webapp log tail -n time-schedule-poc` in a separate console. Note: you must navigate to the root of the project before command execution