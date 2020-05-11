import sys
ONES = [None, 'one', 'two', 'three', 'four',
        'five', 'six', 'seven', 'eight', 'nine']

# Empty string for zero will be replaced in main function

TEENS = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
         'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

TENS_PREFIXES = ['_', '_', 'twen', 'thir', 'for',
                 'fif', 'six', 'seven', 'eigh', 'nine']

# Tens places words without "-ty". ex. twenty > twen, thirty > thir

POWERS_OF_1000 = ['', 'thousand', 'million', 'billion', 'trillion',
                  'quadrillion', 'quintillion', 'sextillion',
                  'septillion', 'octillion']


def to_base_1000(number):
    # To split a number into chunks of three digits
    # ie. (fifty three thousand   two hundred one)

    digits = []
    while number:
        number, digit = divmod(number, 1000)
        digits.append(digit)

    return digits


def to_hundreds_tens_ones(number):

    assert(0 <= number < 1000)

    return number // 100, number // 10 % 10, number % 10


def two_digit_to_words(tens, ones):

    if tens == 0:
        return ONES[ones]

    elif tens == 1:
        return TEENS[ones]

    elif ones == 0:
        return '{}ty'.format(TENS_PREFIXES[tens])
        # This won't index to the underscores (positions 0 and 1)
        # because of the first two ifs

    else:
        return '{}ty {}'.format(TENS_PREFIXES[tens], ONES[ones])


def three_digit_to_words(hundreds, tens, ones):

    last_two_digits = two_digit_to_words(tens, ones)
    if hundreds == 0:
        return last_two_digits

    else:
        if last_two_digits is None:
            return '{} hundred'.format(ONES[hundreds])

        else:
            return '{} hundred {}'.format(ONES[hundreds], last_two_digits)


def chunk_to_words(chunk, position):

    multiplier = POWERS_OF_1000[position]
    # Thousand, million, etc.

    if multiplier:
        multiplier = ' ' + multiplier

    # Add space if it exists so that it's not "onemillion" "twothousand" etc.

    hundreds, tens, ones = to_hundreds_tens_ones(chunk)

    return three_digit_to_words(hundreds, tens, ones) + multiplier

def number_to_words(number):

    if number == 0:
        return 'zero'

    chunks = to_base_1000(number)

    chunk_words = []

    for position, chunk in enumerate(chunks):
        chunk_words.append(chunk_to_words(chunk, position))

    return ' '.join(chunk_words[::-1])

    # Reverse because to_base_1000 returns chunks from smallest to largest
while True:
	a = int(input('the no.'))
	print(number_to_words(a))
		
