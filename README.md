# py-alarm

Simple script to play a song / sound until a key combination is pressed. The idea is to create an 
alarm clock that is away from your bed that you have to walk over to and input a combination to disable. 

Basically a DIY version of [this](http://www.tomsguide.com/us/Alarm-Clock-LED-Ramos-keypad,news-14834.html).


## usage

You'll need [pygame](www.pygame.org)

```bash
sudo apt-get install python-pygame
```

then test it out with

```bash
python alarm.py
```

to actually use as an alarm, you'll probably want a [cron job](http://askubuntu.com/questions/2368/how-do-i-set-up-a-cron-job)

example for every day at 4:30am

```bash
30 4 * * * cron
```
