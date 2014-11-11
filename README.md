#Phone Validator 

##About
This program is written by Katharine Chen for a programming exercise for Bright.md. 

##Description
This program uses [Protractor](https://github.com/angular/protractor) to navigate through the Ear Pain (short) survey of Bright.md's SmartExam.

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