# Team Schedule AI - API 
## Deployment to Azure
1. Go to the root directory of the project
2. Activate the venv
3. Install requirements if not already installed
4. `az login`
5. `az webapp up -n time-schedule-poc --sku F1`
6. (optional) if you want to observe the logs, execute `az webapp log tail -n time-schedule-poc` in a separate console. Note: you must navigate to the root of the project before command execution