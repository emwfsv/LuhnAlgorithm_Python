import re as regex
import luhnAlgorithm
import Loghandler
import os
import datetime
import DatabaseHandler



# Get the running directory for the app
dirname, filename = os.path.split(os.path.abspath(__file__))

# Constructor
logHandler = Loghandler.LogHandler(dirname + "\\Logs\\logFile.txt")
dbHandler = DatabaseHandler.DatabaseHandler("Driver={SQL Server Native Client 11.0};"
                                            "Server=servername;"
                                            "Database=databasename;"
                                            "uid=SA;pwd=password")

# Read database data
# Just for test of database connections
dbHandler.readAllRowData("Tokens")

# Write logrow
logHandler.writeToFile("Application Started - " + str(datetime.datetime.now()))

# Since it is a swedish "Personnummer" it might contain a '-' which we remove.
inputData = input("Please enter a swedish personal number, 10 digits, to check if the Luhn is correct or not: ").replace("-", "")

#Get the last value in the input which is the luhn value
luhnValue = inputData[-1]

# Write logrow
logHandler.writeToFile("User entered input: '" + inputData + "'" )

#Only allow valid integers in input which is 0-9
luhnAlgorithm.validate_only_integers(inputData)

#Swedish personnumer should be 10 digits long. Check it and if not valid, return error to user
if luhnAlgorithm.validate_input(inputData):
    if luhnAlgorithm.valid_luhn(inputData, luhnValue):
        log = str.format("Luhn value {} in input parameter was correct.", luhnValue)
        print(log)
        logHandler.writeToFile(log)
    else:
        log = str.format("Luhn value {} in input parameter was NOT correct!!!", luhnValue)
        print(log)
        logHandler.writeToFile(log)

        ## Add calculation here to what it should be
        suggestedLuhn = luhnAlgorithm.calculate_luhn(inputData)
        log = str.format("Suggested Luhn value is {}.", suggestedLuhn)
        print(log)
        logHandler.writeToFile(log)
else:
    log = "Could not execute the calculation."
    print(log)
    logHandler.writeToFile(log)


      

