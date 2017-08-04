class Patient(object):
    def __init__(self, id, name, allergies, bed_number = None):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_number = bed_number
    

patientone = Patient(100, "Bob", "nuts", 1)
patienttwo = Patient(101, "Mike", "fruits", 2)
patientthree = Patient(102, "Paul", "chocolate", 3)

class Hospital(object):
    def __init__(self, hospital_name, capacity):
        self.patient = []
        self.hospital_name = hospital_name
        self.capacity = capacity
    
    def admit(self, pat):
        # self.bed_number = bed_number
        # print self.patient

        
        if len(self.patient) < self.capacity:
            bed_number = len(self.patient)
            pat.bed_number = bed_number
            self.patient.append(pat)
            print "Admitted"
            print self.patient
        else:
            print "Hospital full" 
        
        return self
    
    def discarge(self, patid):
        if len(self.patient) > 0:
            self.patient.remove()
        return self

hospitalone = Hospital("Mac", 2)
hospitalone.admit(patientone)
hospitalone.admit(patienttwo)
hospitalone.admit(patientthree)