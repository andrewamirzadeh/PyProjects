# //Author Name: Bijan Amirzadehasl
# //Date: 10/18/2021
# //Program Name: Amirzadehasl_AirportInfo.py
# //Purpose: to query a user for an airport code and then display the information for that airport code if it exists.
# if it doesn't exist, let the user know


def main():
    # multiple dictionaries seperated by airport name, airport city, and airport state
    # the airport code is the key part for the value in the dictionary
    Name = {'ATL': 'Hartsfield-Jackson International Airport', 'DFW': 'Dallas/Fort Worth International Airport',
            'DEN': 'Denver International Airport',
            'ORD': 'OHARE International Airport', 'LAX': 'Los Angeles International Airport'}

    City = {'ATL': 'Atlanta', 'DFW': 'Dallas',
            'DEN': 'Denver', 'ORD': 'Chicago',
            'LAX': 'Los Angeles'}

    State = {'ATL': 'Georgia', 'DFW': 'Texas',
             'DEN': 'Colorado', 'ORD': 'Illinois',
             'LAX': 'California'}
    # Query user for airport code or N to exit
    airportcode = input('Enter an airport code (Enter N or n to Exit): ')
    airportcode = airportcode.upper()
    # while loop that will allow the user to query the dictionaries based on the key of airportcode
    while airportcode != 'n' or airportcode != 'N':
        # Will break out of the loop if user enters n or N
        if airportcode == 'n' or airportcode == 'N':
            print('Thanks for using my program professor!')
            break
        # will report to the user that the airport code they entered does not exist in the dictionaries
        # this assumes that the key values for ALL the dictionaries are accurate
        elif airportcode not in Name:
            print('Airport code', airportcode.upper(), 'not found in dictionaries')
        # prints out the values stored in the multiple dictionaries
        else:
            print('The details for the airport', airportcode, 'are:')
            print('Name:', Name[airportcode])
            print('City:', City[airportcode])
            print('State:', State[airportcode])
        # restarts the user prompt.
        airportcode = input('Enter an airport code (Enter N or n to Exit): ')
        airportcode = airportcode.upper()

main()

# My original program
# airports = {'ATL': ['Hartsfield-Jackson International Airport', 'Atlanta', 'GA'],
#             'DFW': ['Dallas/Fort Worth International Airport', 'Dallas', 'TX'],
#             'DEN': ['Denver International Airport', 'Denver', 'CO'],
#             'ORD': ['OHARE International Airport', 'Chicago', 'IL'],
#             'LAX': ['Los Angeles International Airport', 'Los Angeles', 'CA'],
#             'CLT': ['Charlotte Douglas International Airport', 'Charlotte', 'NC'],
#             'LAS': ['McCarran International Airport', 'Las Vegas', 'NV'],
#             'PHX': ['Phoenix Sky Harbor International Airport', 'Phoenix', 'AZ'],
#             'MCO': ['Orlando International Airport', 'Orlando', 'FL'],
#             'SEA': ['Seattle-Tacoma International Airport', 'Seattle', 'WA']
#             }
#
# choice = input('Enter an airport code to look up (Enter N or n to Exit)')
#
# while choice != 'N' or choice != 'n':
#
#     if choice == 'n' or choice == 'N':
#         break
#     print(airports.get(choice.upper(), 'Airport was not found :('))
#     choice = input('Enter an airport code to look up (Enter N or n to Exit)')
