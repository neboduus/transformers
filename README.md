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

### Connect local Jupyter Server to Colab (develop locally, execute on Colab)

- Install `jupyter_http_over_ws` Jupyter extension globally

```shell
pip install jupyter_http_over_ws
```

- Enable extension

```shell
jupyter serverextension enable --py jupyter_http_over_ws
```

- Now start the Jupyter Notebook server and authenticate

```shell
jupyter notebook \
  --NotebookApp.allow_origin='https://colab.research.google.com' \
  --port=8888 \
  --NotebookApp.port_retries=0
```

- Or start the Jupyter Lab server

```shell
jupyter-lab \
  --NotebookApp.allow_origin='https://colab.research.google.com' \
  --port=8889 \
  --NotebookApp.port_retries=0
```

- You should see something like this at this point:

```shell
To access the server, open this file in a browser:
        file:///home/marian/.local/share/jupyter/runtime/jpserver-48209-open.html
    Or copy and paste one of these URLs:
        http://localhost:8889/lab?token=4314cd24b037880969d55945795e7cc3a355b8943931249e
     or http://127.0.0.1:8889/lab?token=4314cd24b037880969d55945795e7cc3a355b8943931249e
```

- Copy the URL showed in the terminal above

- Go to [Colaboratory Dashboard](https://colab.research.google.com/), click the
  "Connect" button and select "Connect to local runtime...". Enter the URL from
  the previous step in the dialog that appears and click the "Connect" button. 

- After this, you should now be connected to your local runtime.

- You can test the integration by running the following code in a Jupyter 
  Notebook cell

```python
if 'google.colab' in str(get_ipython().__dict__):
  print('Running on CoLab')
else:
  print('Not running on CoLab')
```