# This module defines the Country class. A country has a name, a population and an area
class Country:
    _dictCountries = dict()
    _listCountries = []
    ## Constructor method for the class Country. it receives the contries name
    ## @param name: name of the country
    ## @param population: population of the country
    ## @param area: area of the country
    def __init__(self, name, population, area):
        self._name = name
        self._population = population
        self._area = area
        Country._dictCountries[name] = {'area': area, 'population': population}
        Country._listCountries.append([name, area, population])

    ## Returns the country with largest area
    ## @return country with the largest area
    @classmethod
    def largestCountryDict(cls):
        maxArea = -1000
        largestCountry = ''
        for country in Country._dictCountries:
            if Country._dictCountries[country]['area'] > maxArea:
                maxArea = Country._dictCountries[country]['area']
                largestCountry = country
        return print(largestCountry)

    ## Returns the country with largest population
    ## @return country with the largest population
    @classmethod
    def mostPopulatedCountryDict(cls):
        maxPopulation = -1000
        largestCountry = ''
        for country in Country._dictCountries:
            if Country._dictCountries[country]['population'] > maxPopulation:
                maxPopulation = Country._dictCountries[country]['population']
                largestCountry = country
        return print(largestCountry)

    ## Returns the country with largest population density
    ## @return country with the largest population density
    @classmethod
    def largestDensityCountryDict(cls):
        maxDensity = -1000
        largestCountry = ''
        for country in Country._dictCountries:
            if Country._dictCountries[country]['population'] / Country._dictCountries[country]['area'] > maxDensity:
                largestCountry = country
                maxDensity = Country._dictCountries[country]['population'] / Country._dictCountries[country]['area']
        return print(largestCountry)

    ## Returns the country with largest area
    ## @return country with the largest area
    @classmethod
    def largestCountryList(cls):
        largestCountry = ''
        maxArea = -1000
        for country in Country._listCountries:
            if country[1] > maxArea:
                largestCountry = country[0]
                maxArea = country[1]
        return print(largestCountry)

    ## Returns the country with the largest population
    ## @return conutry with the ñargest population
    @classmethod
    def mostPopulatedCountryList(cls):
        largestCountry = ''
        maxPopulation = -1000
        for country in Country._listCountries:
            if country[2] > maxPopulation:
                largestCountry = country[0]
                maxPopulation = country[2]
        return print(largestCountry)

    ## Returns the country with the largest density population
    ## @return country with the largest population density
    @classmethod
    def largestDensityCountryList(cls):
        largestCounty = ''
        maxDensity = -1000
        for country in Country._listCountries:
            if country[2] / country[1] > maxDensity:
                largestCounty = country[0]
                maxDensity = country[2] / country[1]
        return print(largestCounty)