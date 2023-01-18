# Transformers

This repo contains experiments using transformers.

### Install Requirements

- Create Virtual Environment

```shell
python3 -m venv env
```

- Activate Virtual Environment

```shell
. env/bin/activate
```

- Within this directory, execute:

```shell
pip install -r requirements.txt
```

- Test installation

```shell
python -c "from transformers import pipeline; print(pipeline('sentiment-analysis')('we love you'))"
```

- Output should be

```shell
[{'label': 'POSITIVE', 'score': 0.9998704195022583}]
```

### Use with Jupyter Notebook


- We need to install `jupyterlab` globally, therefore deactivate virtual 
  environment

```shell
deactivate
```

- Install `jupyterlab`

```shell
pip install jupyterlab==3.5.2
```

- Now we need to introduce the previously created virtual environment to 
  Jupyter, therefore we need to reactivate the environment

```shell
source env/bin/activate
```

- Introduce environment to Jupyter

```shell
python -m ipykernel install --user --name=env
```

- Launch `jupyterlab`

```shell
jupyter-lab
```