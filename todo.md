## Thoughts to solve problem

We have two sets of events in this problem: deliveries and pickups.
The goal is to hit as many deliveries as possible. It also says to find a “reasonably short route”, is this a multi-objective?
Let's focus on hitting max # deliveries.

If we assume the problem is not _too_ big, we can probaby solve it using MIP. For bigger problems this approach will grind to a halt and we are better off with local neighborhood solvers.

###  MIP approach
Often TSP problems are formulated using x_ij variables where i represents the origin and j the destination node.
We have two sets of nodes:
Deliveries:     d \in D
Pickups:        p \in P

If we want to maximize the number of deliveries: 

Objective = MAX [ \sum_{i in D \union P} \sum_{d \in D} x_id ]        where i \in {D union P}

*with constraints*:
Route: 
x_ij \in {0,1}      forall i,j in {D union P}                                               # The route can be described in binary variables
\sum_{j in D union P} x_ij == \sum_{i in D union P} x_ji    forall j in {D union {}         # Incoming == Outgoing
\sum_{j in D union P} x_i,depot == \sum_{j in D union P} x_depot,i == 1                     # Depot one leaves and one comes back
0 <= \sum_{i in D union P} x_ij <= 1     forall j in {D union P}                            # Cannot be visited more than ones
\sum_{i in D}\sum{j in P} x_ij == 1                                                         # Only one Pickup event can be visited

Capcity constraints:

Ok stop, the route here is not actually relevant. This is more of a bin-packing problem. After deciding on which cargo to pickup/dropoff I can run a simple TSP problem on those nodes. 

-----

## Approach 2
We can always do the pickup we are looking for at the end of the route (after having done all the dropoffs). So let's leave that out for now and just focus on the dropoffs. Then we solve a TSP with the chosen dropoff nodes.

### Bin packing problem:
Maximize number of items in bin with constraint that sum of weights of items is less than ...

### TSP:
Solve TSP on the chosen dropoffs.

### 
Brute force through all Pickup nodes to see the easiest way it can be added to the route (use heuristic)

Ok this seems like it could work let's try this.



