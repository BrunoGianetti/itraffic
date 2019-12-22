# What is Intellingent Light Traffic?

One day I drove in Sao Paulo and got stuck in the traffic jam. So I had an idea how a traffic light could work to make the flow of vehicles along the road more efficient. 

# How do I intend to build this model in the future?

What if we could put a raspberry py board with a camera and leds and program an AI to identify vehicles, people, animals, etc. and thereafter make decisions about signal opening and closing? Where there was the largest accumulation of cars, more open signal time would remain. This would make the flow of cars work more efficiently. Other possibilities such as recordings of criminal occurrences, identification of objects on the road that could cause an accident, pedestrians waiting to cross, etc. could also be considered viable in decisions.

# How my script works?

While waiting for calls on Uber, I opened QPython3 on my cell phone and started coding something very simple that could emulate my idea. Of course, it's not the final version, but I just want to demonstrate how it would work. I imagined an intersection of two avenues that would have 4 signal phases. In infinite looping, a random function draws a number of cars on a given street and compares which of the four phases has the largest accumulation of vehicles. I then programmed a second wait for each identified car and automatically new identifications are performed.

# Raspberry py scheme and peripherals

<img width="300" alt="rename screenshot" src="https://github.com/BrunoGianetti/itraffic/blob/master/rasp.jpeg"> 
<img width="300" alt="rename screenshot"src="https://github.com/BrunoGianetti/itraffic/blob/master/raspcam.jpeg">
<img width="300" alt="rename screenshot"src="https://github.com/BrunoGianetti/itraffic/blob/master/raspled.jpeg">

# A script photo

<img width="300" alt="rename screenshot" src="https://github.com/BrunoGianetti/itraffic/blob/master/Screenshot_20191222-194838.png">

# Watch video instructions on my Linked In account

Click on this link to access video: https://www.linkedin.com/posts/bruno-gianetti-32813aa3_ontem-estava-rodando-em-sp-e-observando-o-activity-6595678436478464000-QcGN (video in Portuguese-BR).
