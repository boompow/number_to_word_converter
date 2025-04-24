def num_to_letter(number, language):

    """Section zero"""
    # creating a library of numbers to letters as a key-value pair
    library_list = [{
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",  7: "seven", 8: "eight",
        9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty",
        50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred", 1000: "thousand",
        1000000: "million", 1000000000: "billion", 1000000000000: "trillion", 1000000000000000: "quadrillion",
        1000000000000000000: "quintillion", 1000000000000000000000: "sextillion",
        1000000000000000000000000: "septillion",
        1000000000000000000000000000: "octillion",
        1000000000000000000000000000000: "nonillion",
        1000000000000000000000000000000000: "decillion",
        1000000000000000000000000000000000000: "undecillion",
        1000000000000000000000000000000000000000: "duodecillion",
        1000000000000000000000000000000000000000000: "tredecillion",
        1000000000000000000000000000000000000000000000: "quattuordecillion",
        1000000000000000000000000000000000000000000000000: "quindecillion",
        1000000000000000000000000000000000000000000000000000: "sexedecillion",
        1000000000000000000000000000000000000000000000000000000: "septendecillion",
        1000000000000000000000000000000000000000000000000000000000: "octodecillion",
        1000000000000000000000000000000000000000000000000000000000000: "novemdecillion",
        1000000000000000000000000000000000000000000000000000000000000000: "vigintillion"

    }, {
        0: "ዜሮ", 1: "አንድ", 2: "ሁለት", 3: "ሶስት", 4: "አራት", 5: "አምስት", 6: "ስድስት", 7: "ሰባት", 8: "ስምንት", 9: "ዘጠኝ",
        10: "አስር", 11: "አስራ አንድ", 12: "አስራ ሁለት", 13: "አስራ ሶስት", 14: "አስራ አራት", 15: "አስራ አምስት", 16: "አስራ ስድስት",
        17: "አስራ ሰባት", 18: "አስራ ስምንት", 19: "አስራ ዘጠኝ", 20: "ሃያ", 30: "ሰላሳ", 40: "አርባ", 50: "ሃምሳ",
        60: "ስድሳ", 70: "ሰባ", 80: "ሰማንያ", 90: "ዘጠና", 100: "መቶ", 1000: "ሺህ", 1000000: "ሚሊዮን", 1000000000: "ቢሊዮን",
        1000000000000: "ትሪሊዮን", 1000000000000000: "ኳድሪሊዮን", 1000000000000000000: "ኲንቲሊዮን",
        1000000000000000000000: "ሲክቲሊዮን",
        1000000000000000000000000: "ሴፕቲሊዮን",
        1000000000000000000000000000: "ኦክቲሊዮን",
        1000000000000000000000000000000: "ኖኒሊዮን",
        1000000000000000000000000000000000: "ዴሲሊዮን",
        1000000000000000000000000000000000000: "አንዴሲሊዮን",
        1000000000000000000000000000000000000000: "ዱዴሲሊዮን",
        1000000000000000000000000000000000000000000: "ትሬዴሲሊዮን",
        1000000000000000000000000000000000000000000000: "ኳትርዴሲሊዮን",
        1000000000000000000000000000000000000000000000000: "ኲንዴሲሊዮን",
        1000000000000000000000000000000000000000000000000000: "ሴክዴሲሊዮን",
        1000000000000000000000000000000000000000000000000000000: "ሴፕቴንዴሲሊዮን",
        1000000000000000000000000000000000000000000000000000000000: "ኦክቶዴሲሊዮን",
        1000000000000000000000000000000000000000000000000000000000000: "ኖቬምዴሲሊዮን",
        1000000000000000000000000000000000000000000000000000000000000000: "ቪንቲሊዮን"
    }]

    library = {}

    # Language selection options

    if language in ["Amharic", "amharic", "Amh", "amh", "አማርኛ", "አማረኛ"]:
        library = library_list[1]
    elif language in ["eng", "english", "English", "Eng"]:
        library = library_list[0]
    else:
        library = {}
        print("Either you typed incorrectly or the language is not available")
        print("ወይ በትክክል አልጻፉም ወይም ቋንቋው በመዝገባችን አይገኝም።")
        print("")

    """Section one"""
    # breaking down the number into three digit strings I call chunks
    number_string = str(number)
    amount = len(number_string)
    split = int(amount / 3)
    multipliers_split = []
    multipliers_split_modified = []
    multipliers = []

    if number_string[:amount-3*split] != "":
        remainder = number_string[:amount-3*split]
        multipliers.append(remainder)
    for i in range(1, split+1):
        range_reversed = split+1 - i
        to_be_multiplier = number_string[amount-3*range_reversed:amount-3*(range_reversed-1)]
        multipliers.append(to_be_multiplier)

    """Section two"""

    # further breaking down the chunks into multiples of ten, multiples of hundred, and numbers one to nineteen
    # that will add up to the chunk number

    for multiplier in multipliers:
        length = len(multiplier)
        for i in range(length):
            if multiplier[i] != "0":
                if i == (length - 2) and multiplier[i] == "1":
                    j = int(multiplier[i]) * 10 + int(multiplier[length - 1])
                    multipliers_split.append(str(j))
                else:
                    k = int(multiplier[i]) * 10 ** ((length - 1) - i)
                    multipliers_split.append(str(k))
            elif multiplier[i] == "0" and length == 1:
                multipliers_split.append(i)

        second_last_entry = multiplier[len(multiplier) - 2]
        last_entry = multiplier[len(multiplier) - 1]
        if second_last_entry == "1" and last_entry != "0" and len(multiplier)>1:
            multipliers_split.pop()

    # further separating the multiples of hundred to the multiplier and hundred

    for num in multipliers_split:
        if int(num) >= 100:
            first = num[0]
            rest = num.replace(first, "1")
            multipliers_split_modified.append(first)
            multipliers_split_modified.append(rest)
        else:
            multipliers_split_modified.append(num)

    """Section three"""
    # counting the list of numbers from the chunk broken down and using that number to insert exponential of
    # one thousand between the chunks

    counter = 0
    values = 0
    for multiplier in multipliers:
        counter += 1
        # Those with value of zero
        if int(multiplier) == 0:
            value = 0

        # Those with value of one
        elif int(multiplier) < 20 or (int(multiplier)%10 == 0 and int(multiplier) < 100):
            value = 1

        # Those with value of two
        elif 20 < int(multiplier) < 100:
            value = 2
        elif int(multiplier)% 100 == 0:
            value = 2

        # Those with value of three
        elif int(multiplier) > 100 and int(multiplier[1:]) < 20:
            value = 3
        elif int(multiplier)%10 == 0 and int(multiplier) > 100:
            value = 3

        # Those with value of four
        elif int(multiplier) > 100 and int(multiplier[1:]) > 20:
            value = 4

        values += value
        total = values + counter-1
        len_multi = len(multipliers)

        if int(multiplier) != 0 and len_multi - counter != 0:
            multipliers_split_modified.insert(total, (1000**(len_multi - counter)))
    """Section four"""

    another_counter = 0
    # calling out the letter form of the numbers we've stored in the multiplier_split_modified list to
    # complete our function

    numbers_in_letters = ""
    for num in multipliers_split_modified:
        another_counter += 1
        k = library.get(int(num))
        if another_counter % 6 == 0:
            numbers_in_letters += str(k) + " " + "\n"
        else:
            numbers_in_letters += str(k) + ' '

    numbers_in_letters = numbers_in_letters.capitalize()

    return numbers_in_letters
