"""Auto-generated file, do not edit by hand. SE metadata"""
from ..phonemetadata import NumberFormat, PhoneNumberDesc, PhoneMetadata

PHONE_METADATA_SE = PhoneMetadata(id='SE', country_code=46, international_prefix='00',
    general_desc=PhoneNumberDesc(national_number_pattern='[1-9]\\d{5,9}', possible_number_pattern='\\d{5,10}'),
    fixed_line=PhoneNumberDesc(national_number_pattern='1(?:0[1-8]\\d{6}|[136]\\d{5,7}|(?:2[0-35]|4[0-4]|5[0-25-9]|7[13-6]|[89]\\d)\\d{5,6})|2(?:[136]\\d{5,7}|(?:2[0-7]|4[0136-8]|5[0138]|7[018]|8[01]|9[0-57])\\d{5,6})|3(?:[356]\\d{5,7}|(?:0[0-4]|1\\d|2[0-25]|4[056]|7[0-2]|8[0-3]|9[023])\\d{5,6})|4(?:0[1-9]\\d{4,6}|[246]\\d{5,7}|(?:1[013-8]|3[0135]|5[14-79]|7[0-246-9]|8[0156]|9[0-689])\\d{5,6})|5(?:0[0-6]|[15][0-5]|2[0-68]|3[0-4]|4\\d|6[03-5]|7[013]|8[0-79]|9[01])\\d{5,6}|6(?:0[1-9]\\d{4,6}|3\\d{5,7}|(?:1[1-3]|2[0-4]|4[02-57]|5[0-37]|6[0-3]|7[0-2]|8[0247]|9[0-356])\\d{5,6})|8[1-9]\\d{5,7}|9(?:0[1-9]\\d{4,6}|(?:1[0-68]|2\\d|3[02-5]|4[0-3]|5[0-4]|[68][01]|7[0135-8])\\d{5,6})', possible_number_pattern='\\d{5,9}', example_number='8123456'),
    mobile=PhoneNumberDesc(national_number_pattern='7[02369]\\d{7}', possible_number_pattern='\\d{9}', example_number='701234567'),
    toll_free=PhoneNumberDesc(national_number_pattern='20(?:0(?:0\\d{2}|[1-9](?:0\\d{1,4}|[1-9]\\d{4}))|1(?:0\\d{4}|[1-9]\\d{4,5})|[2-9]\\d{5})', possible_number_pattern='\\d{6,9}', example_number='20123456'),
    premium_rate=PhoneNumberDesc(national_number_pattern='9(?:00|39|44)(?:1(?:[0-26]\\d{5}|[3-57-9]\\d{2})|2(?:[0-2]\\d{5}|[3-9]\\d{2})|3(?:[0139]\\d{5}|[24-8]\\d{2})|4(?:[045]\\d{5}|[1-36-9]\\d{2})|5(?:5\\d{5}|[0-46-9]\\d{2})|6(?:[679]\\d{5}|[0-58]\\d{2})|7(?:[078]\\d{5}|[1-69]\\d{2})|8(?:[578]\\d{5}|[0-469]\\d{2}))', possible_number_pattern='\\d{7}(?:\\d{3})?', example_number='9001234567'),
    shared_cost=PhoneNumberDesc(national_number_pattern='77(?:0(?:0\\d{2}|[1-9](?:0\\d|[1-9]\\d{4}))|[1-6][1-9]\\d{5})', possible_number_pattern='\\d{6}(?:\\d{3})?', example_number='771234567'),
    personal_number=PhoneNumberDesc(national_number_pattern='75[1-8]\\d{6}', possible_number_pattern='\\d{9}', example_number='751234567'),
    voip=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    pager=PhoneNumberDesc(national_number_pattern='74[02-9]\\d{6}', possible_number_pattern='\\d{9}', example_number='740123456'),
    uan=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    voicemail=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    no_international_dialling=PhoneNumberDesc(national_number_pattern='NA', possible_number_pattern='NA'),
    national_prefix='0',
    national_prefix_for_parsing='0',
    number_format=[NumberFormat(pattern='(8)(\\d{2,3})(\\d{2,3})(\\d{2})', format='\\1-\\2 \\3 \\4', leading_digits_pattern=['8'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([1-69]\\d)(\\d{2,3})(\\d{2})(\\d{2})', format='\\1-\\2 \\3 \\4', leading_digits_pattern=['1[013689]|2[0136]|3[1356]|4[0246]|54|6[03]|90'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='([1-69]\\d)(\\d{3})(\\d{2})', format='\\1-\\2 \\3', leading_digits_pattern=['1[13689]|2[136]|3[1356]|4[0246]|54|6[03]|90'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{2})(\\d{2})(\\d{2})', format='\\1-\\2 \\3 \\4', leading_digits_pattern=['1[2457]|2[2457-9]|3[0247-9]|4[1357-9]|5[0-35-9]|6[124-9]|9(?:[125-8]|3[0-5]|4[0-3])'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(\\d{3})(\\d{2,3})(\\d{2})', format='\\1-\\2 \\3', leading_digits_pattern=['1[2457]|2[2457-9]|3[0247-9]|4[1357-9]|5[0-35-9]|6[124-9]|9(?:[125-8]|3[0-5]|4[0-3])'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(7\\d)(\\d{3})(\\d{2})(\\d{2})', format='\\1-\\2 \\3 \\4', leading_digits_pattern=['7'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(77)(\\d{2})(\\d{2})', format='\\1-\\2\\3', leading_digits_pattern=['7'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(20)(\\d{2,3})(\\d{2})', format='\\1-\\2 \\3', leading_digits_pattern=['20'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(9[034]\\d)(\\d{2})(\\d{2})(\\d{3})', format='\\1-\\2 \\3 \\4', leading_digits_pattern=['9[034]'], national_prefix_formatting_rule='0\\1'),
        NumberFormat(pattern='(9[034]\\d)(\\d{4})', format='\\1-\\2', leading_digits_pattern=['9[034]'], national_prefix_formatting_rule='0\\1')],
    intl_number_format=[NumberFormat(pattern='(8)(\\d{2,3})(\\d{2,3})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['8']),
        NumberFormat(pattern='([1-69]\\d)(\\d{2,3})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['1[013689]|2[0136]|3[1356]|4[0246]|54|6[03]|90']),
        NumberFormat(pattern='([1-69]\\d)(\\d{3})(\\d{2})', format='\\1 \\2 \\3', leading_digits_pattern=['1[13689]|2[136]|3[1356]|4[0246]|54|6[03]|90']),
        NumberFormat(pattern='(\\d{3})(\\d{2})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['1[2457]|2[2457-9]|3[0247-9]|4[1357-9]|5[0-35-9]|6[124-9]|9(?:[125-8]|3[0-5]|4[0-3])']),
        NumberFormat(pattern='(\\d{3})(\\d{2,3})(\\d{2})', format='\\1 \\2 \\3', leading_digits_pattern=['1[2457]|2[2457-9]|3[0247-9]|4[1357-9]|5[0-35-9]|6[124-9]|9(?:[125-8]|3[0-5]|4[0-3])']),
        NumberFormat(pattern='(7\\d)(\\d{3})(\\d{2})(\\d{2})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['7']),
        NumberFormat(pattern='(77)(\\d{2})(\\d{2})', format='\\1 \\2 \\3', leading_digits_pattern=['7']),
        NumberFormat(pattern='(20)(\\d{2,3})(\\d{2})', format='\\1 \\2 \\3', leading_digits_pattern=['20']),
        NumberFormat(pattern='(9[034]\\d)(\\d{2})(\\d{2})(\\d{3})', format='\\1 \\2 \\3 \\4', leading_digits_pattern=['9[034]']),
        NumberFormat(pattern='(9[034]\\d)(\\d{4})', format='\\1 \\2', leading_digits_pattern=['9[034]'])],
    mobile_number_portable_region=True)
