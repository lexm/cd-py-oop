class Patient(object):
    def __init__(self, id, name, allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_number = None

class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
    def admit(self, id, name, allergies):
        if len(self.patients) >= self.capacity:
            return "Hospital is full."
        else:
            new_pat = Patient(id, name, allergies)
            new_pat.bed_number = len(self.patients)
            self.patients.append(new_pat)
            return "Admission is complete"
    def discharge(self, id):
        for idx in range(len(self.patients)):
            if self.patients[idx].id == id:
                self.patients[idx].bed_number = None
                return self.patients.pop(idx)

hosp = Hospital("St. Elsewhere", 2)
print hosp.admit(123,"Joan",["Penicillin"])
print hosp.admit(125,"Jill",[])
print hosp.admit(126,"Jack",["latex"])
print hosp.discharge(125).name
