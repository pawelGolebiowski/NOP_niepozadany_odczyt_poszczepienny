import re

class Symptoms:
    symptom = ''
    
    def __init__(self, symptom):
        self.symptom = symptom
    
    def __repr__(self):
        if 'drgawki' in self.symptom:
            return str("Drgawki")
        if 'gorączka' in self.symptom or r"temp" in self.symptom:
            return str("Gorączka")
        if 'zaczerwienienie' in self.symptom:
            return str('Zaczerwienienie i bolesność')
        if 'wymioty' in self.symptom:
            return str("Wymioty")
        if ('omdlenie' or 'utrata przytomności') in self.symptom:
            return str("Omdlenie")
        else:
            return str("Pozostałe")