import re

def IrCodeValidator(input):
    '''
    Melli Code validation based on implemented formula.
    Returns False if input is not a valid Melli Code.
    '''

    x = ['0000000000', '1111111111', '2222222222', '3333333333', '4444444444', '5555555555', '6666666666', '7777777777', '8888888888', '9999999999']

    if not re.search(r'^\d{10}$', input) or input in x:
        return False

    check = int(input[9])
    s = sum([int(input[x]) * (10 - x) for x in range(9)]) % 11
    return (s < 2 and check == s) or (s >= 2 and check + s == 11)


regex_fa = '^[\s\u0020\u2000-\u200F\u2028-\u202F\u0621-\u0628\u062A-\u063A\u0641-\u0642\u0644-\u0648\u064E-\u0651\u0655\u067E\u0686\u0698\u06A9\u06AF\u06BE\u06CC]*$'
regex_ir_phone = '^(0|\+98|00)(21|26|25|86|24|23|81|28|31|44|11|74|83|51|45|17|41|54|87|71|66|34|56|13|77|76|61|38|58|35|84)(2|3)\d{7}$'
regex_ir_cell = '^(\+98|0|00)?9(12|14|19|35|36|37|38|39|32)\d{7}$'