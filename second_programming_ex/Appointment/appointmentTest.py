from appointment import Appointment
from monthly import Monthly
from daily import Daily
from onetime import OneTime
import argparse
import textwrap


def demoAppointment():
    parser = argparse.ArgumentParser(prog='Appointment test program',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=textwrap.dedent('''\
                                                  Appointment
                                      --------------------------------
                                      A simulated Appointments program. Saves and loads appointments and lets the user
                                      see how many dates are in a specific date. 
                                      Appointments can be of 3 classes: OneTime, Daily or Monthly.
                                      
                                      Instance methods:
                                      
                                      1) occursOn:  returns true if the appointment occurs in a specific date.
                                         @param year, month, day: date that the users wants to use.
                                         @return True if the appointment occurs in that date.

                                      2) getDescription:  returns the description of the appointment.
                                         @return description.

                                      3) getDate:  returns the date of the appointment. If it has an occurrence, returns
                                         the date of the first appointment.
                                         @return date of the appointment.
                                      
                                      Class Methods:
                                      
                                       1) allAppointments: prints all the appointments that occur in a specific date.
                                          @param year, month, day: date to check
                                       
                                       2) save: save all the appointments in a csv file.
                                          @param path of the file to save
                                       
                                       3) load: loads appointments from a csv file.
                                          @param path of the file to load

                                      '''),
                                     epilog=textwrap.dedent('''\
                                                 Usage
                                      --------------------------------
                                       Instance methods:
                                       app1 = OneTime('appointment 1',2023, 1, 1)
                                       app1.occursOn(2023, 1, 1)
                                       
                                       Class Methods:
                                       Appointment.allAppointments(2023, 1, 1)
                                       Appointment.save("appointments.csv")
                                       Appointment.load("appointments.csv")
                                      ''')
                                     )
    parser.add_argument('--save_demo', action='store_true', help='runs a demo that saves appointments')
    parser.add_argument('--load_demo', action='store_true', help='runs a demo that loads appointments')
    args = parser.parse_args()

    if args.save_demo:
        a = OneTime("Cita 1", 2024, 2, 1)
        b = Daily("Cita 2", 2023, 12, 5)
        c = Monthly("Cita 3", 2024, 1, 1)
        d = Daily("Cita 4", 2023, 1, 3)
        print("Result: ")
        Appointment.allAppointments(2024, 2, 1)
        Appointment.save()
        print("------------------------------")
        print("Expected\nCita 1\nCita 2\nCita 3\nCita 4\n")

    if args.load_demo:
        Appointment.load("second_programming_ex/Appointment/dates2.csv")
        print("Result: ")
        Appointment.allAppointments(2024, 2, 1)
        print("------------------------------")
        print("Expected\nCita 1\nCita 2\nCita 3\nCita 5\n")


demoAppointment()
