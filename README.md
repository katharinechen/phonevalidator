#Phone Validator 

##About
This program is written by Katharine Chen for a programming exercise for Bright.md. 

##Description
This python program validates US phone number.  Given an input phone number in the terminal, it will return 'pass' or 'fail'. Valid phone numbers are 10 or 11 digits, may not begin with a 0, and may contain any number of spaces, dots or dashes.

##Installation 
Clone this repository: 

````
git clone https://github.com/katharinechen/ear_pain_test.git
````

Run the function as follows: 

````
phone_validator(123-123-1234) ##pass
phone_validator(1.234.123.1234) ##pass
phone_validator(012.123.123) ##fail 
````
The program will accept phone numbers on the command line and return output in the terminal. 

````
python phonevalidator.py 123-123-1234
pass 

python phonevalidator.py 123
fail 
````
##Run Tests 
Run tests with the following command in the terminal:
````
python test_phone_validator.py 
````