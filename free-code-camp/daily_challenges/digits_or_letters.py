def digits_or_letters(str):
    letter_count = 0
    digit_count = 0

    for letter in str:
        if letter.isalpha():
            letter_count += 1
        elif letter.isdigit():
            digit_count += 1
    
    is_than = 'tie'
    if letter_count > digit_count:
        is_than = 'letters'
    elif digit_count > letter_count:
        is_than = 'digits'

    return is_than
