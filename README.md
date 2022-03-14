# App_API
This microservice is the api of the project Information retrival from the noisy documents

## Setup
### Clone repository and initialise submodules
This repository contains the X5GON_content_metadata_dataset repository as a [submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules). To automatically initialise the submodule, use the following command to clone this repository:
```
$ git clone --recurse-submodules <https or ssh link of this repository>
```
### Environment
To set up your environment, open a terminal and cd to the api directory. You then need to set up a Python virtual environment using
```
// mac or linux
python3 -m venv venv
source venv/bin/activate
// windows
python -m venv venv
venv\Scripts\activate
```
You might have to upgrade pip:
```
(venv)pip install --upgrade pip
```
Then install following dependencies on the requirements file by:
```
(venv) pip install -r requirements.txt
```
You can check whether this is working:
```
(venv) flask run
```
To stop the flask server press Control-C.

### X5GON Dataset
You have to install the [X5GON_content_metadata_dataset](https://github.com/IRCAI/X5GON_content_metadata_dataset) package:
```
(venv) cd X5GON_content_metadata_dataset
(venv) pip install -e .
```

## Run the api on the docker environment
```
(venv) docker-compose up
```
* noted that the the docker compose in this api is for testing purpose only