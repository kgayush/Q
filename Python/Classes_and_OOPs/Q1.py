from numpy import average


class Country:
    avg_population = 100000

    def __init__(self, country_name, country_code):
        try:
            if type(country_name) != str:
                raise ValueError
            if len(country_code) != 3:
                raise ValueError
            self.country_name = country_name
            self.country_code = country_code
            print(self.country_name, self.country_code)

        except ValueError:
            print("Invalid Input.")

        except TypeError:
            print("Input must be a string.")

    def country_short_form(self, country_name):
        try:
            return country_name[:2].upper()

        except TypeError:
            return "Invalid Input."

    @classmethod
    def is_densly_populated(cls, population):
        try:
            if population > cls.avg_population:
                return True
            else:
                return False
        except TypeError:
            return "Invalid Input."

    @staticmethod
    def world_avg_population(population_list):
        try:
            return average(population_list)

        except:
            pass

    
    @property
    def formatted_country_name(self):
        try:
            print(f'{self.country_name}')
        
        except TypeError:
            print("Something went wrong.")

    @formatted_country_name.setter
    def formatted_country_name(self, new_country_name):
        try:
            self.country_name = new_country_name
            print(f'The updated country name is {new_country_name}')

        except TypeError:
            print("Invalid Input.") 

    @formatted_country_name.deleter
    def formatted_country_name(self):
        print("Deleting...")
        del self.country_name            
            

        

country = Country("India", "IND")
print(country.country_short_form("India"))
print(country.is_densly_populated(1000000))
print(country.world_avg_population([100000, 200000, 25000]))
country.formatted_country_name = 'Srilanka'
del country.formatted_country_name