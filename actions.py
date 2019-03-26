import logging

from rasa_core_sdk import Action
from rasa_core_sdk.forms import FormAction

logger = logging.getLogger(__name__)


class ActionHappy(Action):
    def name(self):
        # type: () -> Text
        logger.info("Got name")
        return "action_happy"

    def run(self, dispatcher, tracker, domain):
        # type: (CollectingDispatcher, Tracker, Dict[Text, Any]) -> List[Dict[Text, Any]]
        logger.info("Esto esta corriendo")
        # cuisine = tracker.get_slot('cuisine')
        # q = "select * from restaurants where cuisine='{0}' limit 1".format(cuisine)
        # result = db.query(q)
        dispatcher.utter_message("lmao me alegro")  # send the message back to the user

        return []
        # return [SlotSet("matches", result if result is not None else [])]


class SuggestionForm(FormAction):
    """Accept free text input from the user for suggestions"""

    def name(self):
        return "suggestion_form"

    @staticmethod
    def required_slots(tracker):
        return ["suggestion"]

    def slot_mappings(self):
        return {"suggestion": self.from_text()}

    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_template('utter_thank_suggestion', tracker)
        return []
