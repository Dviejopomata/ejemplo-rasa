## happy path
* greet
  - utter_greet
* mood_great
  - suggestion_form
  - action_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - suggestion_form
  - utter_cheer_up
  - utter_did_that_help
* mood_affirm
  - action_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* mood_deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye