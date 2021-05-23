from symptoms import Symptoms

class NOP:

    def __init__(self, id, date, voivodeship, region, gender, symptoms):
        self.id = id
        self.date = date
        self.voivodeship = voivodeship
        self.region = region
        self.gender = gender
        self.symptoms = Symptoms(symptoms)



