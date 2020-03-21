# Algorithm for Traffic Signals

## Normal Scenario

In this, we are finding out the number of vehicles present at the left side of each road. These numbers are always found out after a fixed amount of time. When this project is run for the first time, the road with the maximum number of vehicles is chosen and its signal is made green. This time fo the green signal is assigned according to the number of vehicles present in that road. There is a maximum time-limit, decided beforehand, i.e., no road can have green signal on for more than that time even if all vehicles have not passed. If a road was chosen at any point of time, then it can not be chosen again till all other roads have been chosen atleast once, i.e., its priority is made zero or negative. In this way, each road gets its green signal atleast for some time in the loop, depending on the number of vehicles.

### For example:

If the four sides of the road is labelled A, B, C, D. At the starting, if it is found out that A has 12 vehicles, B has 20, C has 7 and D has 10. Thus priority assigned would be:
* B = 1
* A = 2
* D = 3
* C = 4

So, now, B's green signal will open for 20 seconds. In the meantime, as these 20 seconds are about to come to an end, it is again found out that now A has 15 vehicles, C has 17 and D has 16. Now, the priority assigned would be:
* C = 1
* D = 2
* A = 3
* B = (-1)

So, now, C's green signal will open for 17 seconds. In the meantime, as these 17 seconds are about to come to an end, it is again found out that now A has 29 vehicles and D has 21. Now, the priority assigned would be:
* A = 1
* D = 2
* B = -1
* C = -2

and thus, this loop would go on.

## Emergency Scenario

If any road is found that there will be an emergency vehicle coming then its priority is made the highest. This road will get the green signal first. This will decrease the time of journey (source to destination) for that vehicle. This will be very useful in the case of ambulance, fire extinguisher etc. when the emergency vehicle has gone than the system runs normally.

### Continuing the above example:
