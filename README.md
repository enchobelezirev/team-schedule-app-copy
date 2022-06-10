# Introduction
Team Schedule is a cloud-based app supporting managers and employees to effectively plan complex time shift scenarios. Available at the SAP store [here](https://store.sap.com/dcp/en/product/display-0000059791_live_v1/Team%20Schedule).

As part of the application we are including "*smart features*" that automate the process of creating shift such:
- generating shifts for all employees of a manager *(currently in developement)*
- predicting how many people and shifts are needed based on the demand for a given team/store *(future developement)*

The scope of this project is concerned only with "*smart features*".

# Domain knowledge

- A new shift cannot start less than 12 hours before the end of another shift.

## Initial analysis of data

Data analysis could be found in this [notebook](https://gitlab.com/timeoffapp/timeschedule/microsoft-demo-poc/-/blob/main/data/DatasetCreation.ipynb).

### Employees per manager

| Manager ID | Employee count | Total shifts |
| -------- | -------- | -------- |
| 0 | 36 | 5564 |
| 1 | 24 | 3142 |
| 2 | 11 | 1481 |
| 3 | 12 | 1568 |
| 4 | 25 | 3672 |
| 5 | 10 | 1607 |


### Weekly hours lengts 

| Hours per week| Shifts |
| -------- | -------- |
|40  |  15240 |
|20 |  1008 |
|30 |  1008 |


### Shifts for weekday

0 - Monday ... 6 - Sunday

| Weekday| Shifts count |
| -------- | -------- |
|3  |  3413 |
|2  |  3409 |
|1  |  3366 |
|4  |  3304 |
|0  |  2953 |
|5  |   456 |
|6  |   133 |

### Shift lenghts

| Shift | Shifts count |
| -------- | -------- |
| 480 |  5385|
| 240 |   156|
| 960 |    15|
| 360 |     5|
| 421 |     3|

### Start times


| Start time | Occurrences | 
| -------- | -------- | 
|09:00  | 9300|
|08:00  | 1247|
|11:00  |  847|
|17:00  |  574|
|14:00  |  524|
|06:00  |  522|
|12:00  |  502|
|07:00  |  471|
|21:00  |  362|
|03:00  |  344|
|18:00  |  324|
|16:00  |  224|
|19:00  |  219|
|00:00  |  196|
|23:00  |  175|
|13:00  |  156|
|19:59  |  156|
|14:59  |  138|
|04:00  |  122|
|10:00  |  117|
|02:00  |  114|
|10:30  |   92|
|05:00  |   82|
|15:30  |   57|
|22:00  |   50|
|16:59  |   45|
|14:30  |   45|
|15:00  |   16|
|20:00  |    5|
|20:59  |    5|
|09:30  |    3|

### End times


| End time | Occurrences | 
| -------- | -------- | 
| 18:00   | 8439 |
| 20:00   | 1023 |
| 17:00   |  976 |
| 15:00   |  805 |
| 02:00   |  721 |
| 21:00   |  662 |
| 19:00   |  487 |
| 12:00   |  461 |
| 13:00   |  459 |
| 09:00   |  410 |
| 23:00   |  329 |
| 03:00   |  327 |
| 07:00   |  269 |
| 14:00   |  245 |
| 16:00   |  209 |
| 01:00   |  175 |
| 08:00   |  175 |
| 22:00   |  157 |
| 11:00   |  152 |
| 06:00   |  147 |
| 23:59   |  146 |
| 19:30   |   92 |
| 00:30   |   54 |
| 23:30   |   45 |
| 22:59   |   45 |
| 10:00   |   13 |
| 05:00   |    5 |
| 21:30   |    3 |
| 18:30   |    2 |
| 15:30   |    1 |


## Client interviews summary
- Managers do the shifts for the next month, trying to give them at least a few days before the start, so that employees can plan. 
- Managers have different sub-groups. 
     - E.g. Total of 20ish people, with 6 teams for.  
- The manager (Borislav Rayov) has a pattern he has established with his employees and he mainly copies it month to month. 
    - There are two people with late shifts, and they rotate week by week. Better for employees to have predictability, so they can plan.  
- There are ad-hoc changes because of 
    - Sick leave 
    - Paid leaves  
- During summer or xmass, people are encouraged to submit their paid leaves 2-3 weeks beforehand. During xmass, there are less people working.  
- There is more demand, for example on Monday/Tuesday when there are more calls.  
- There are part-timers whose preferences change every 3-4 months, according to new semester. But they are case-by-case.  
- Some managers ask their employees when it's good time for them.. Some don't care.  
- To make the shifts people managers usually spend 1-2 hours a month, including ad-hoc changes.  
- There are always employee who don't like their shifts, but it's better to have a sense that it's fair, and not one person has the best shifts.  


# Project Architecture

## Overall arhitecture
![Architecture overview](images/architecture_overview.jpg)

## Modules

### 1 Data
Sample data for:
- [a single employee](https://gitlab.com/timeoffapp/timeschedule/timeschedule-ai-api/-/blob/main/sample_data/single_employee.json)
- [large payload with multiple employees](https://gitlab.com/timeoffapp/timeschedule/timeschedule-ai-api/-/blob/main/sample_data/large_payload_zero_month.json)

### 2 Requests
We have two types of request - **GET** and **UPDATE**.

**GET** - Get the team schedule by genereting shifts for all employees for a week or a month.

**UPDATE** *[Not implemented]* - This request is a feature, but it's purpose will be the following: To be able to offer а new schedule if an employee wants to move his shift

### 3 API Mapper
The responsibility of this module is to map the incoming request that are in JSON format to our data models.

### 4 Schedule Manager
As the main purpose of the app is to generate a schedule for the manager's employees, we want to implement different types of schedule generators. The schedule manager will determine which implementation of the schedule generator to use. At the moment only the shift frequency predictor from the image is implemented.


### 5 Schedule Generator
The schedule generates shifts for all employees for a period of time. 
The shift frequency predictor ##TODO: Chris can you add a little bit more detail of the work of the shift frequency generator

### 6 Shift Preference Predictor

### 7 Restriction Manager



# Setting up project

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
  
## Static code analysis

### Black

    python -m black --line-length=120 .

### Isort

    python -m isort --line-length=150 --profile black .

### Flake8
    
    flake8 --tee --format=gl-codeclimate --max-line-length=120 --ignore=E203,E501,W503 --exclude venv,dist .
    

## Running tests

### Pytest

    py -m pytest ./test

    

# Deployment 

## Deployment to Azure
1. Go to the root directory of the project
2. Activate the venv
3. Install requirements if not already installed
4. `az login`
5. `az webapp up -n time-schedule-poc --sku F1`
6. (optional) if you want to observe the logs, execute `az webapp log tail -n time-schedule-poc` in a separate console. Note: you must navigate to the root of the project before command execution
