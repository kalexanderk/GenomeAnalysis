def NumberToPattern(input_number, length_of_output_pattern):
    array_of_intermediate_code = []

    def NumberToPatternHelp(number):
        if number < 4:
            array_of_intermediate_code.append(number)
            return 0
        remainder = number - 4*(number/4)
        number = number/4
        array_of_intermediate_code.append(remainder)
        NumberToPatternHelp(number)

    NumberToPatternHelp(input_number)
    if len(array_of_intermediate_code) < length_of_output_pattern:
        for i in range(length_of_output_pattern-len(array_of_intermediate_code)):
            array_of_intermediate_code.append(0)

    #reverse array_of_intermediate_code
    array_of_intermediate_code=array_of_intermediate_code[::-1]

    result_array = []
    for i in array_of_intermediate_code:
        if i == 0:
            result_array.append("A")
        if i == 1:
            result_array.append("C")
        if i == 2:
            result_array.append("G")
        if i == 3:
            result_array.append("T")
    return result_array



print("".join(str(x) for x in NumberToPattern(2320, 2)))