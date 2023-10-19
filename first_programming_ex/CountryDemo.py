def demoCountry():
    import argparse
    import textwrap
    from Country import Country
    parser = argparse.ArgumentParser(prog='my test program',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=textwrap.dedent('''\
                                                 Country
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


    parser.add_argument('--run_demo', action='store_true', help='runs this demo')
    args = parser.parse_args()

    if args.run_demo:
        country1 = Country('a', 1000, 1)
        country2 = Country('b', 1, 1000)
        Country.largestCountryDict()
        print('Expected: b')
        Country.largestCountryList()
        print('Expected: b')
        Country.mostPopulatedCountryDict()
        print('Expected: a')
        Country.mostPopulatedCountryList()
        print('Expected: a')
        Country.largestDensityCountryDict()
        print('Expected: a')
        Country.largestDensityCountryList()
        print('Expected: a')


demoCountry()