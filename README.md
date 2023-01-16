# transformers

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

