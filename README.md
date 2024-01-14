# Django site to control my Rpi

## Idea

I want to be able to control my RPi embedded programming programs with Django.

See my bare-metal-pi repository https://www.github.com/Johnny-Codes/bare-metal-pi

## NOHUP to keep server running

### Start:

`nohup python manage.py runserver 0.0.0.0:8000 &`

### Kill:

`pgrep -f "python manage.py runserver 0.0.0.0:8000"`

- returns the PID

`kill -15 PID`

Kind of my proof of concept for IOT/Home Automation without using Home Automation (the program)
