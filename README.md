# HittingObjectsProblem

## Overview
The Point Covering Algorithm, implemented in Python, addresses the set covering problem, aiming to find the minimum number of straight lines required to cover a given set of 2D points in the plane.The algorithm leverages Python libraries such as: 

- `argparse`
- `itertools`
- `sys`

## Approaches

The Point Covering Algorithm offers two distinct approaches to solving the set covering problem:

### Optimal Solution

The first approach employs an optimization strategy to determine the optimal solution, seeking the minimum number of straight lines necessary to cover the given set of 2D points in the plane. This method guarantees finding the most efficient configuration for point coverage.

### Greedy Algorithm

The second approach adopts a greedy algorithm, making decisions based on the immediate maximum gain (the maximum number of elements that can be covered). However, it does not guarantee finding the best possible solution. In this greedy approach, the algorithm may converge to a suboptimal solution instead of the optimal one. 

## Usage

The program is called as follows (where `python` is the appropriate command for your system):

python points_cover.py [-f] [-g] points_file

## Parameters:

The program provides flexibility through the following optional parameters:

- **-f (optional):** If provided, the program will execute the algorithm that explores all possible subsets. Be cautious as, for numerous lines, the program may not finish in a reasonable time. If -f is not given, the program will default to the greedy algorithm.

- **-g (optional):** When specified, the program will only search for lines parallel to the axes. Otherwise, it may use any lines that pass through the points. In the event that the lines connecting the given points are insufficient for complete coverage, the program may additionally employ horizontal lines passing through points that are not collinear with any other horizontal or vertical point.

- points_file: The file containing the points to be covered. The file should consist of lines in the format: (x y)

## Test Files
To help users test the algorithm, three sample files are included in the repository:

- points_file: example_1.txt
- points_file: example_2.txt
- points_file: example_3.txt
