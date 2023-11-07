from appointment import Appointment


# Implements the OneTime type of appointment
# This appointment occurs only time
# This class extends the Appointment class
class OneTime(Appointment):

    # Constructor method for the OneTime class
    # @param description: description of the appointment. Eg: Dentist appointment
    # @param year, month, day: date of the appointment
    def __init__(self, descr, year, month, day):
        super().__init__(descr, year, month, day)

    # Repr method for the OneTime class
    # returns the type of date, description and date. Eg: Onetime,Appointment,2023,7,11
    def __repr__(self):
        year = str(self.getDate().year)
        month = str(self.getDate().month)
        day = str(self.getDate().day)
        return "OneTime,"+self.getDescription()+","+year+","+month+","+day

