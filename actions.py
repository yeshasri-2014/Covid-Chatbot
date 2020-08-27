# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import custom

#
#
class ActionSearchCoronaSymptoms(Action):

    def name(self) -> Text:
        return "action_corona_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        severity = tracker.get_slot("severity")
        #dispatcher.utter_message(text="Gandhi Hospital {}".format(location))
        if (severity.lower() == "mild"):
            return [SlotSet("severity","mild")]
        if (severity.lower() == "common"):
            return [SlotSet("severity","common")]
        if (severity.lower() == "serious") and (severity.lower() == "severe"):
            return [SlotSet("severity","serious")]
        else:
            return []

class ActionSearchCoronaStatsCountry(Action):

    def name(self) -> Text:
        return "action_corona_stats_country"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        loc = tracker.get_slot("country")
        #dispatcher.utter_message(text="Gandhi Hospital {}".format(location))
        #if (loc.lower() == "nation") or ("india" in loc.lower()):
        s_Msg = custom.GetCoronaNationStats()
        dispatcher.utter_message(text="{}".format(s_Msg))

class ActionSearchCoronaStatsState(Action):

    def name(self) -> Text:
        return "action_corona_stats_state"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        loc = tracker.get_slot("state")
        s_Msg = custom.GetCoronaStateStats(loc.replace(" ", "").lower())
        dispatcher.utter_message(text="{}".format(s_Msg))

class ActionSearchCoronaStateHospitals(Action):

    def name(self) -> Text:
        return "action_corona_hospitals"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        loc = tracker.get_slot("state")
        s_Msg = custom.GetCoronaStateHospital(loc.replace(" ", "").lower())
        dispatcher.utter_message(text="{}".format(s_Msg))

