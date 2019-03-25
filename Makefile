SHELL := /bin/bash
train:
	source ./venv/bin/activate; \
    python -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose; \
    python -m rasa_core.train -d domain.yml -s stories.md -o models/dialogue;