from datetime import date


# This module defines the appointment class. An appointment has a date and a description
class Appointment:

    # List with all the appointments
    _appointments = []

    # Constructor method for the Appointment class
    # @param description: description of the appointment. Eg: Dentist appointment
    # @param year, month, day: date of the appointment
    def __init__(self, description, year, month, day):
        self._description = description
        self._date = date(year=year, month=month, day=day)
        Appointment._appointments.append(self)

    # Checks if an appointment occurs in a specific date
    # @param year, month, day: date the user wants to check
    # @return True if the appointment occurs in the date
    def occursOn(self, year, month, day):
        return date(year=year, month=month, day=day) == self._date

    # Returns the description of the appointment
    # @ return description
    def getDescription(self):
        return self._description

    # Returns the date of the appointment
    # @ return date of appointment
    def getDate(self):
        return self._date

    # prints all appointments that occur in a given date
    # @param year, month, day: date that the user wants to check
    @classmethod
    def allAppointments(cls, year, month, day):
        auxiliar = False
        for appointment in Appointment._appointments:
            if appointment.occursOn(year, month, day):
                auxiliar = True
                print(appointment.getDescription())
        if not auxiliar:
            print("There are no appointments in that date")

    # Saves all appointments
    @classmethod
    def save(cls, file="second_programming_ex/Appointment/dates.csv"):
        with open(file, "w") as outfile:
            for app in Appointment._appointments:
                outfile.write(repr(app)+'\n')

    # loads all appointments
    @classmethod
    def load(cls, file="second_programming_ex/Appointment/dates.csv"):
        from onetime import OneTime
        from daily import Daily
        from monthly import Monthly
        with open(file) as infile:
            cont = 0
            for lines in infile:
                cont += 1
                line = lines.split(",")
                if line[0] == "OneTime":
                    globals()['app'+str(cont)] = OneTime(line[1], int(line[2]), int(line[3]), int(line[4]))
                elif line[0] == "Daily":
                    globals()['app' + str(cont)] = Daily(line[1], int(line[2]), int(line[3]), int(line[4]))
                elif line[0] == "Monthly":
                    globals()['app' + str(cont)] = Monthly(line[1], int(line[2]), int(line[3]), int(line[4]))
