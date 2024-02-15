import re as regex

def validate_only_integers(inputData):
    # Only allow valid integers in input which is 0-9 which this function test
    if regex.search("^[0-9]*$", inputData):
        pass
    else:
        print("Found not valid data in input!! Input only allows integers")
        exit()

def validate_input(inputData):
    # Swedish personnumer should be 10 digits long. Check it and if not valid, return error to user
    # Function returns bool to select further execution
    if len(inputData) == 10:
        return True
    elif len(inputData) > 10:
        value = "Inputvalue is to long! Found {} digits"
        print(value.format(len(inputData)))
        return False
    else :
        value = "Inputvalue is to short! Only found {} digits"
        print(value.format(len(inputData)))
        return False


def valid_luhn(inputData, luhn):
    #Calculate the luhn value with modulus 10
    calc_luhn = calculate_luhn(inputData) #  10 - (totalSum % 10)

    # Return bool depending on result.
    return True if int(luhn) == int(calc_luhn) else False


def calculate_luhn(inputData):
    # We reverse the string because we start from the back when we do the calculation
    # We also remove the presumed luhn value before calulation.
    multiple = 2
    totalSum = 0

    for x in inputData[8::-1]:
                
        #Multiply int with a multiple
        sum = int(x) * multiple

        #If the sum of the 2 values is >9 then sum both number. for instance 10 = 1 + 0
        if len(str(sum)) > 1:
            sum = int(str(sum)[0]) + int(str(sum)[1])

        #Add sum to total sum
        totalSum += sum

        # For next iteration, switch multiple
        multiple = 2 if multiple == 1 else 1

    #Calculate the luhn value with modulus 10
    return 10 - (totalSum % 10)
