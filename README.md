# Plotwise assignment

## Problem description:
For this problem an event is a location on the plane encoded by their coordinates (x,y). You are given two sets of events D and P, let’s call them the set of deliveries and the set of pickups respectively. You’re task is to create a tool that:
- Given as input D and P (encoded and inputted however you want) outputs a “reasonably short route”.
- Each event has a capacity. The vehicle performing the delivery also has a physical capacity limit and the capacity of events in the vehicle at any given time may not exceed this physical limit.
- A route is an ordering of events starting and ending with the “depot” event located at the origin (0,0).
- The length of a route is calculated as the sum of distances between each subsequent event.
- A delivery is loaded onto the vehicle at the first depot and dropped off at its specified location. A pickup, conversely, is loaded at its specified location and unloaded upon returning to the depot.
- The twist: you should visit as many delivery events as possible but only one (1) pickup event of your choice!