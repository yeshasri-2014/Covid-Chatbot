## say greet
* greet
  - utter_greet

## say goodbye
* goodbye
  - utter_goodbye

## corona symptions
* greet
  - utter_greet
* corona-common-symptoms
  - utter_corona_symptoms
* goodbye
  - utter_goodbye

## corona mild symptions
* greet
  - utter_greet
* corona-symptoms
  - slot{"severity":"mild"}
  - utter_corona_mild_symptoms
* goodbye
  - utter_goodbye

## corona common symptions
* greet
  - utter_greet
* corona-symptoms
  - slot{"severity":"common"}
  - utter_corona_common_symptoms
* goodbye
  - utter_goodbye

## corona serious symptions
* greet
  - utter_greet
* corona-symptoms
  - slot{"severity":"serious"}
  - utter_corona_serious_symptoms
* goodbye
  - utter_goodbye

## corona nation stats
* greet
  - utter_greet
* corona-stats-india
  - utter_corona_stats_country
  - action_corona_stats_country{"country":"india"}
* goodbye
  - utter_goodbye

## corona state stats
* greet
  - utter_greet
* corona-stats-state
  - utter_corona_stats_state
  - action_corona_stats_state{"state":"telangana"}
* goodbye
  - utter_goodbye

## corona state hospitals
* greet
  - utter_greet
* corona-hospitals
  - utter_corona_hospitals
  - action_corona_hospitals{"facility":"hospitals","state":"telangana"}
* goodbye
  - utter_goodbye

## corona prevention_1
* greet
  - utter_greet
* corona-prevention-cure
  - slot{"cure":"prevention"}
  - utter_corona_prevention
* goodbye
  - utter_goodbye

## corona prevention_2
* greet
  - utter_greet
* corona-prevention-cure
  - slot{"cure":"prevent"}
  - utter_corona_prevention
* goodbye
  - utter_goodbye

## corona cure
* greet
  - utter_greet
* corona-prevention-cure
  - slot{"cure":"cure"}
  - utter_corona_cure
* goodbye
  - utter_goodbye

## corona food
* greet
  - utter_greet
* corona-prevention-cure
  - slot{"cure":"food"}
  - utter_corona_food
* goodbye
  - utter_goodbye

## corona immunity
* greet
  - utter_greet
* corona-prevention-cure
  - slot{"cure":"immunity"}
  - utter_corona_food
* goodbye
  - utter_goodbye

## corona medicines
* greet
  - utter_greet
* corona-prevention-cure
  - slot{"cure":"medicines"}
  - utter_corona_cure
* goodbye
  - utter_goodbye

