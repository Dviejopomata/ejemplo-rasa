SHELL := /bin/bash
train:
	source ./venv/bin/activate; \
    python3 -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose; \
    python3 -m rasa_core.train -d domain.yml -s stories.md -o models/current/dialogue;

serve:
	source ./venv/bin/activate; \
	python3 -m rasa_core.run -d models/current/dialogue -u models/current/nlu

#  curl -XPOST localhost:5000/parse -d '{"q":"hello there", "project":"current"}'
cmdline:
	source ./venv/bin/activate; \
	python3 -m rasa_core.run -d models/current/dialogue -u models/current/nlu --debug --endpoints endpoints.yml
run-actions:
	source ./venv/bin/activate; \
	python3 -m rasa_core_sdk.endpoint --actions actions
