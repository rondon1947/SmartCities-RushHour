# HackNITR 2020
For the "HackNITR" Hackathon 2020

# Rush Hour - The Traffic Management Project

Our project is from the track - "Smart Cities". It is a traffic management project, incorporating the fields of Machine Learning, Web Development and App Development. At each traffic signal, for each side, it counts the number of cars, scooters, buses, etc., and then assigns a corresponding priority and time for that particular signal, instead of just assigning a fixed time to all irrespective of the number of vehicles present at that time. Thus, this will save time of the commuters. Also, our project contains a special feature for ambulances, fire-fighters and other emergency-response teams to mark in their location of their starting and destination points and according to it, algorithms of all the traffic signals along that way will be altered in a certain way, allowing the emergency vehicles to pass the signal without any stopping at the signal.
The different fields of our project include:
* 1. Machine Learning: This would count the number of cars, buses, etc. on each side, for all the four directions, then would assign the different priorities and times for the green signal, according the no. of vehicles present. If the number of vehicles are same, more priority would be assigned to that direction, where more no. of buses or other larger vehicles are present.
* 2. App: Every owner and/or driver of all emergency vehicles like ambulances, fire-engines, etc., will have this app, where they could mark in their location of their starting and destination points and according to it, algorithms of all the traffic signals along that way will be altered in a certain way, allowing the emergency vehicles to pass the signal without any stopping at the signal.
* 3. Website: This website would be for the traffic controlling head officer of each area of the cities, where he could login as admin, and look ever any anomalies for his area, like, if a certain signal requires more or less time for each side, how many emergency vehicles passed the signals and if they stopped there, etc.

## Advantages:

* 1. Very less human intervention at each signal.
* 2. Quick and free roads for all the emergency vehicles, thus, allowing better social amneties for the citizens.
* 3. Better surveillance of the breaking of traffic rules, like overspeeding, wrong sides, not following the traffic lights, etc., because the same computer vision to count the vehicles, can also be used to detect them.
* 4. Overall monitoring increases coordination between different signals and helps in the betterment of one of the core features of a Smart City - Traffic Management.   

## Getting Started

These instructions will get anyone a copy of the project up and running on his/her local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This contains a list of things a person needs before-hand to install the software and how to install them.

```bash    
pip install -r requirements.txt 
```

### Installing

This contains a step by step series of examples that tell anyone how to get a development environment running.

```
Steps:
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo.

## Running the tests

This explains how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With (Tech Stack)

* [Flutter](https://flutter.dev/) - The app development framework used.

* [Node.js](https://nodejs.org/) - Website Backend development environment , also used to integrate ML project in a website.

* [Keras](https://keras.io/) - The Machine Learning framework used for counting the the number of vehicles at each signal(object detection).

* [Matplotlib](https://matplotlib.org/) - The Library used for Visualization .

* [OpenCV](https://docs.opencv.org/master/d0/de3/tutorial_py_intro.html) - The Library used for Image-Processing . 

* [CVlib](https://www.cvlib.net/) - The Machine Learning framework used for counting the the number of vehicles at each signal(object detection).


## Authors

* **Raj Sahu** - *Machine Learning* - ( https://github.com/raj-sahu )
* **Harshit Raj** - *Website Backend & Deployment* - ( https://github.com/prodigioharshit )
* **Rishav Raj** - *Website Frontend & Working Algorithm* - ( https://github.com/rishav139 ) 
* **Rohan Nishant** - *App Development and Integration* - ( https://github.com/rondon1947 )

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
