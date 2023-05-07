# vue-fastapi


## Demo

There seem to be two options to run the dev servers:
- A docker(docker-compose)
- Running dev servers in a local environment separately

To execute the API:
```bash
uvicorn api.main:app --reload
```

To run the dev server:
```bash
cd vue-fastapi
npm dev run
```


## Prerequisites
- python 3.11
- poetry

## Project memo

- Virtual environment set up
```bash
pyenv local 3.11.3
python -m venv .venv
poetry init
poetry shell
```

- FastAPI set up
```bash
poetry add fastapi[all]
```

- Vue3+Vite set up
```bash
npm init vue@latest
cd vue-fastapi/
npm install axios vue-axios
npm install
```
