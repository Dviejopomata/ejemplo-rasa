SHELL := /bin/bash
train:
	source ./venv/bin/activate; \
    python3 -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose; \
    python3 -m rasa_core.train -c policy.yml -d domain.yml -s stories.md -o models/current/dialogue;

train-interactive:
	source ./venv/bin/activate; \
    python3 -m rasa_core.train interactive -c policy.yml -d domain.yml -s stories.md -o models/current/dialogue;
#    \
#    python3 -m rasa_nlu.train -c nlu_config.yml --data nlu.md -o models --fixed_model_name nlu --project current --verbose;


serve:
	source ./venv/bin/activate; \
#	python3 -m rasa_nlu.server --debug --response_log logs --path ./models/current --endpoints endpoints.yml
	python3 -m rasa_nlu.server --debug --response_log logs --path ./models/current --endpoints endpoints.yml --pre_load models/current/nlu
# curl "localhost:5000/parse?q=hola&project=nlu"
# curl "localhost:5000/parse?q=hola&project=nlu&model=current"

cmdline:
	source ./venv/bin/activate; \
	python3 -m rasa_core.run -d models/current/dialogue -u models/current/nlu --debug --endpoints endpoints.yml
run-actions:
	source ./venv/bin/activate; \
	python3 -m rasa_core_sdk.endpoint --actions actions
train-cmd:  train cmdline

