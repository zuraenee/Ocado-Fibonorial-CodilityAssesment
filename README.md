# Ocado-Fibonorial-CodilityAssesment
""This is my own solution, that has TIME ERROR""
You are a programmer in a scientific team doing research into particles.
As an experiment, you have measured the position of a single particle in N
equally distributed moments of time. The measurement made in moment
Kis recorded in array A as AlKl.
Now, your job is to count all the periods of time when the movement of
the particle was stable. Those are the periods during which the particle
doesn't change its velocity: i.e. the difference between any two
consecutive position measurements remains the same. Note that you
need at least three measurements to be sure that the particle didn't
change its velocity.
For example:
1,
7,
7
9
is stable (velocity is 2)
is stable (particle stays in
place)
3,
-1, -5,
-9
1
is stable (velocity is
-4)
is not stable (you need at least
three measurements!
11
is not stable (velocity changes
between measurements)
More formally, your task is to find all the periods of time AlP], A[P+1l,
A[Q] (of length at least 3) during which the movement of the particle is
stable. Note that some periods of time might be contained in others (see
example test).

Write a function:
def solution (A)
)
that, given array A consisting of N integers representing the results of the
measurements, returns the number of periods of time when the movement of the particle was stable. The function should return -1 if the
result exceeds 1,000,000,000.
Examples:
Given array A = [-1, 1, 3, 3, 3, 2, 3, 2, 1, 0] the function should return 5,
because there are five periods during which the movement of the particle
is stable, namely: (0, 2), (2, 4), (6, 9), (6, 8) and (7, 9). Note that the last two
periods are contained by (6, 9).
Given A = 12, 2, ...
. 21 of length 10,000, the function should return
49985001.
Write an efficient algorithm for the following assumptions:
??
N is an integer within the range [0..60,000];
each element of array A is an integer within the range
[-2,000,000,000..2,000,000,000].
