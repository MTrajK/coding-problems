# Coding Problems

My solutions for many various coding/algorithmic problems (this repo will be updated with new solutions from time to time). \
All solutions are written in [Python](https://www.python.org/) (more precisely, [Python 3](https://docs.python.org/3)), using the [Built-in Functions](https://docs.python.org/3/library/functions.html) and few modules from the [Python Standard Library](https://docs.python.org/3/library/) like:
- [math](https://docs.python.org/3/library/math.html) (used for constants like math.pi, math.inf and functions like math.ceil, math.floor, math.gcd, math.log, math.pow, math.sqrt, etc)
- [collections](https://docs.python.org/3/library/collections.html) (used for [collections.deque](https://docs.python.org/3/library/collections.html#collections.deque) when there is a need for [Stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) or [Queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) data structures)
- [heapq](https://docs.python.org/3/library/heapq.html) (used when there is a need for [Priority Queue](https://en.wikipedia.org/wiki/Priority_queue) data structure).

So, to execute these solutions there is no need from installing any external packages. \
Coding style and name conventions are described in this file [PEP8](https://www.python.org/dev/peps/pep-0008). \
These problems are from sites like [LeetCode](https://leetcode.com/) (you can find more than 30 sites like this in the [Training Sites](#Training) section).\
Also in this README you can find many resources for learning algorithms: [Courses](#Courses), [Books](#Books), [Training Sites](#Training), [Other Resources](#Other).


## Categories

Each solution/problem in this repo belongs to one of these categories:

1. [Strings](/)
2. [Lists](/)
3. [Linked Lists](/)
4. [Trees](/)
5. [Dynamic Programming](/)
6. [Backtracking](/)
7. [Graphs](/)
8. [Math](/)
9. [Other](/)


## Template

Each file with solution in this repo will have the following template:

```python
'''
Problem name

Problem explanation

Input: XXX
Output: XXX
Output explanation: XXX

=========================================
Solution explanation
    Time Complexity:    O(X)
    Space Complexity:   O(X)
Solution 2 explanation
(some of the problems are solved in more than one way)
    Time Complexity:    O(X)
    Space Complexity:   O(X)
'''

############
# Solution #
############

def name_of_problem(params):
    # description of code
    pass

##############
# Solution 2 #
##############

def name_of_problem_2(params):
    # description of code
    pass


###########
# Testing #
###########

# Test 1
# Correct result => 'result'
print(name_of_problem('example'))

# Test 2
# Correct result => 'result2'
print(name_of_problem_2('example2'))
```

## Courses

Collection of free courses from one of the best CS universities.

1. Princeton University (Coursera)
    - [Algorithms Part 1](https://www.coursera.org/learn/algorithms-part1)
    - [Algorithms Part 2](https://www.coursera.org/learn/algorithms-part2)

2. [Standford University (Coursera)](https://www.coursera.org/specializations/algorithms)
    - [Divide and Conquer, Sorting and Searching, and Randomized Algorithms](https://www.coursera.org/learn/algorithms-divide-conquer)
    - [Graph Search, Shortest Paths, and Data Structures](https://www.coursera.org/learn/algorithms-graphs-data-structures)
    - [Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming](https://www.coursera.org/learn/algorithms-greedy)
    - [Shortest Paths Revisited, NP-Complete Problems and What To Do About Them](https://www.coursera.org/learn/algorithms-npcomplete)

3. MIT University (YouTube)
    - [Introduction to algorithms 2005](https://www.youtube.com/playlist?list=PL8B24C31197EC371C)
    - [Introduction to algorithms 2011 - 6.006](https://www.youtube.com/playlist?list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
    - [Design and analysis of algorithms - 6.046J](https://www.youtube.com/playlist?list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp)
    - [Advanced Data Structures - 6.851](https://www.youtube.com/playlist?list=PLUl4u3cNGP61hsJNdULdudlRL493b-XZf)

4. Harvard University (YouTube)
    - [Advanced algorithms - CS224](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uP4rJgf5ayhHWgw7akUWSf)

5. UC Berkeley
    - [Data Structures - CS61B](https://inst.eecs.berkeley.edu/~cs61b/archives.html)
    - [Efficient Algorithms and Intractable Problems - CS170](https://cs170.org/)

## Books

Several books that have made an impression on me:

1. [Grokking Algorithms by Aditya Bhargava](https://www.goodreads.com/book/show/22847284-grokking-algorithms-an-illustrated-guide-for-programmers-and-other-curio) - The best book for complete beginners in algorithms! I wish this book existed when I started learning algorithms.
2. [Introduction to Algorithms by Thomas H. Cormen](https://www.goodreads.com/book/show/6752187-introduction-to-algorithms)
3. [Algorithms by Robert Sedgewick & Kevin Wayne](https://www.goodreads.com/book/show/10803540-algorithms)
4. [The Algorithm Design Manual by Steven Skiena](https://www.goodreads.com/book/show/425208.The_Algorithm_Design_Manual)

## Other

1. [Geeks For Geeks](https://www.geeksforgeeks.org/) - The site which all interested in algorithms (no matter if beginners or experts) should know!
2. [The Algorithms - Python](https://github.com/TheAlgorithms/Python) - Great GitHub repo with many algorithms written in Python.
3. [KhanAcademy - Algorithms](https://www.khanacademy.org/computing/computer-science/algorithms) - Good explanations for some basic algorithms.
4. HackerRank - YouTube tutorials
    - [Algorithms](https://www.youtube.com/playlist?list=PLI1t_8YX-ApvMthLj56t1Rf-Buio5Y8KL)
    - [Data Structures](https://www.youtube.com/playlist?list=PLI1t_8YX-Apv-UiRlnZwqqrRT8D1RhriX)

## Training

If the problems from [LeetCode](https://leetcode.com/) are not enough and you need more problems like those, you can find much more on these platforms:

- [HackerRank](http://hackerrank.com/)
- [CodeChef](http://codechef.com/)
- [HackerEarth](http://hackerearth.com/)
- [CodeForces](http://codeforces.com/)
- [Topcoder](http://topcoder.com/)
- [Project Euler](https://projecteuler.net/)
- [Codility](https://codility.com/)
- [CoderByte](https://coderbyte.com/)
- [CodingBat](http://codingbat.com/)
- [CodeAbbey](http://codeabbey.com/)
- [Wolfram Challenges](https://challenges.wolfram.com/)
- [CS Academy](https://csacademy.com/)
- [Daily Coding Problem](https://www.dailycodingproblem.com/)
- [Daily Interview Pro](http://dailyinterviewpro.com/)
- [Codewars](http://www.codewars.com/)
- [SPOJ](http://www.spoj.com/)
- [Online Judge](https://onlinejudge.org/)
- [LintCode](http://www.lintcode.com/en/)
- [DevPost](https://devpost.com/)
- [USA CO](http://www.usaco.org/)
- [CodeFu](https://codefu.mk/)
- [Mendo](https://mendo.mk/Welcome.do)
- [Kattis](http://www.kattis.com/)
- [AlgoExpert](https://www.algoexpert.io/)
- [Brilliant](http://brilliant.org/)
- [Kaggle](http://kaggle.com/)
- [Codingame](https://www.codingame.com/)
- [CheckiO](http://www.checkio.org/)
- [Rosalind](http://rosalind.info/problems/locations/)
- [CodeKata](http://codekata.com/)
- [FightCode](http://fightcodegame.com/)