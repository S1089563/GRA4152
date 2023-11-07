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
                                      A simulated Country program. Stores countries and returns the largest country,
                                      the most populated country and the most dense country:
                                      1) largestCountryDict:  returns the largest country (using dictionaries)
                                         @return largest country

                                      2) largestCountryList:  returns the largest country (using lists)
                                         @return largest country

                                      3) mostPopulatedCountryDict:  returns the most populated country (using dicts)
                                         @return most populated country

                                      4) mostPopulatedCountrylist:  returns the most populated country (using lists)
                                         @return most populated country

                                      5) largestDensityCountryDict(): returns the largest density country (using dicts)
                                         @return largest density country

                                      6) largestDensityCountryList(): returns the largest density country (using lists)
                                         @return largest density country

                                      '''),
                                     epilog=textwrap.dedent('''\
                                                 Usage
                                      --------------------------------
                                       country1 = Country('a',10,10) # initialize a Message
                                       country1.largestCountryDict()
                                       country1.largestCountryList()
                                       country1.mostPopulatedCountryDict()
                                       country1.mostPopulatedCountryList()
                                       country1.largestDensityCountryDict()
                                       country1.largestDensityCountryList()
                                      ''')
                                     )
    parser.add_argument('--save_demo', action='store_true', help='runs this demo')
    parser.add_argument('--load_demo', action='store_true', help='runs this demo')
    args = parser.parse_args()

    if args.save_demo:
        a = OneTime("Cita 1", 2024, 2, 1)
        b = Daily("Cita 2", 2023, 12, 5)
        c = Monthly("Cita 3", 2024, 1, 1)
        d = Daily("Cita 4", 2023, 1, 3)
        Appointment.allAppointments(2024, 2, 1)
        Appointment.save()

    if args.load_demo:
        Appointment.load("second_programming_ex/Appointment/dates2.csv")
        print("-----")
        Appointment.allAppointments(2024, 2, 1)

demoAppointment()