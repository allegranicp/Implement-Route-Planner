**Route Planner Project**

Overview
---
The goals / steps of this project are the following:

* Use A* search to implement a "Google-maps" style route planning algorithm to calculate the shortest path between two points on a map.

![alt_text][image1]

[//]: # (Image References)
[image1]: ./images/result.png "Result"


## [Rubric](https://review.udacity.com/#!/rubrics/1210/view) Points
---

The code for this project is contained in the IPython notebook: "Advanced_Lane_Finding.ipynb" 

### Discussion
* How would you explain A-Star to a family member?
    - A-Star is a searching method that uses a straight line calculation to estimate the cost of how far a specific node is from the goal. It then uses this estimation in summation with the cost at the current location and gives a total. It then uses that total to determine what the lowest cost is and takes that path to search.
* How does A-Star search algorithm differ from Uniform cost search? What about Best First search?
    - Uniform Cost Search will always find the shortest path by the cheapest cost, but to do it must expand equally in all directions not specifically in the direction of the goal which may cost additional effort to do. 
    - Breadth First Search will always find the shortest path by the number of steps (length), but it doesn't take into account the cost nor does always go in the direction of the goal.
    - A* Search uses a straight line admissible heuristic that will always go in the direct of the goal and it will also take into account cost as well. The heurstic can only be admissible if it doesn't overestimate, which means it's not always guaranteed to find the shortest.
* What is a heuristic?
    - A shortcut estimation method for solving complex problems in a practical way. It allows for fast problem sovling, but does doesn't guarntee a correct solution but a reasonable one when information is incomplete or uncertain
* What is a consistent heuristic?
    - A heuristic that is always admissisble. Once an action is taken, a successor is generated for each node. The estimated cost is less than or equal to the cost to get to the successor from node plus the estimation of the successor.
* What is a admissible heuristic?
    - A heuristic that does not overestimate the real cost to the goal. Every node must have a estimated cost lower than the true cost to reach the goal from that node.

* Some admissible heuristic are consistent.
* All Consistent heuristic are admissible.
