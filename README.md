# TwilioProject

#### Create a .env file for environment variables



#### Create a virtualenv 
`virtualenv venv`


#### Activate the env

##### linux
`source venv/bin/activate`

##### window
`venv\Scripts\activate`




## Now run following commands on activated virtualenv



## Make directories if not exists
`mkdir media static templates`


#### Install required packages
`pip install -r requirements.txt`


### Run makemigrations
`python manage.py makemigrations`

### Run migrate
`python manage.py migrate`



### Create superuser
`python manage.py createsuperuser`



####  https://github.com/TwilioDevEd/account-security-quickstart-django


####  https://www.twilio.com/console/sms/settings/geo-permissions




#### In trail version to must be in the verified number list
##### https://www.twilio.com/console/phone-numbers/verified


#### and also to send in another geo location it should be nebaled via
##### https://www.twilio.com/console/sms/settings/geo-permissions


#### also from should be from 
##### https://www.twilio.com/console/phone-numbers/incoming
