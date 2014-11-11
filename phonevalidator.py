import re 
import sys 

def phone_validator(phone_number):
    re_pattern = r'\A([1-9]{0,1})(\s|-|\.{0,1})([1-9]{3})(\s|-|\.{0,1})(\d{3})(\s|-|\.{0,1})(\d{4})$'
    result = re.match(re_pattern, phone_number)
    if result:
        return "pass"
    else:
        return "fail"

if __name__ == "__main__": 
    phone_input = sys.argv[1]
    print phone_validator(phone_input)