from appointment import Appointment
from datetime import date


# Implements the Daily type of appointment
# This appointment occurs daily
# This class extends the Appointment class
class Daily(Appointment):

    # Constructor method for the OneTime class.
    # @param description: description of the appointment. Eg: Dentist appointment
    # @param year, month, day: date of the appointment
    def __init__(self, descr, year, month, day):
        super().__init__(descr, year, month, day)

    # Checks if an appointment occurs in a specific date
    # @param year, month, day: date the user wants to check
    # @return True if the appointment occurs in the date
    def occursOn(self, year, month, day):
        return date(year=year, month=month, day=day) >= self._date

    # Repr method for the Daily class
    # returns the type of date, description and date. Eg: Daily,Appointment,2023,7,11
    def __repr__(self):
        year = str(self.getDate().year)
        month = str(self.getDate().month)
        day = str(self.getDate().day)
        return "Daily,"+self.getDescription()+","+year+","+month+","+day
