# Coding Problems

Here you can find [solutions](#Solutions) for various coding/algorithmic problems and many useful [resources](#Learning-Resources) for learning algorithms and data structures.\
Also, this repo will be updated with new solutions and resources from time to time.

*Note that this repo is meant to be used for learning and researching purposes only and it is **not** meant to be used for production.*


## Solutions

Algorithms and data structures are not language-specific (it's true that some languages are faster, and some are easier to use), but if you are good with the logic and pseudocode, any language would be good.\
So I've decided to use [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) because I think it's very close to pseudocode and it's easily readable (so it'll be easy for someone from another environment to implement the same solutions).\
As I said previously, all solutions are written in [Python](https://www.python.org/) (more precisely, [Python 3](https://docs.python.org/3)), using the [Built-in Functions](https://docs.python.org/3/library/functions.html) (print, len, range, sorted, sum, min, max, etc...) and a few modules from the [Python Standard Library](https://docs.python.org/3/library/) like:
- [math](https://docs.python.org/3/library/math.html) (used for constants like math.pi, math.inf and functions like math.ceil, math.floor, math.gcd, math.log, math.pow, math.sqrt, etc)
- [collections](https://docs.python.org/3/library/collections.html) (used for [collections.deque](https://docs.python.org/3/library/collections.html#collections.deque) when there is a need for [Stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) or [Queue](https://en.wikipedia.org/wiki/Queue_(abstract_data_type)) data structures)
- [heapq](https://docs.python.org/3/library/heapq.html) (used when there is a need for [Priority Queue](https://en.wikipedia.org/wiki/Priority_queue) data structure).
- [random](https://docs.python.org/3/library/random.html) (used for [nondeterministic algorithms](https://en.wikipedia.org/wiki/Nondeterministic_algorithm), like shuffling arrays ([Fisher–Yates shuffle](https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle)), sampling arrays ([Reservoir sampling](https://en.wikipedia.org/wiki/Reservoir_sampling)) and [Monte Carlo methods](https://en.wikipedia.org/wiki/Monte_Carlo_method)).

So, to execute these solutions there is no need from installing any external packages. \
Coding style and name conventions are described in the official [PEP8](https://www.python.org/dev/peps/pep-0008) page.

*Note that I'm **not** the author of these problems, they are from sites like [LeetCode](https://leetcode.com/) (you can find more than 40 sites like this in the [Training Sites](#Training-Sites) section). **Only** the solutions and explanations are mine. If you find any **bug** or incorrect implementation (or faster/better implementation) in this repo, please let me know by opening an issue or pull request.*


### Template

For easier navigation into the solutions, each file with a solution in this repo will have the following template:

```python
'''
Problem Name

Problem explanation.

Input: XXX
Output: XXX
Output explanation: XXX

=========================================
Solution 1 explanation.
    Time Complexity:    O(X)
    Space Complexity:   O(X)
Solution 2 explanation.
(some of the problems are solved in more than one way)
    Time Complexity:    O(X)
    Space Complexity:   O(X)
'''


##############
# Solution 1 #
##############

def name_of_solution_1(params):
    # description of code
    pass


##############
# Solution 2 #
##############

def name_of_solution_2(params):
    # description of code
    pass


###########
# Testing #
###########

# Test 1
# Correct result => 'result1'
test_val = 'example1'
print(name_of_solution_1(test_val))
print(name_of_solution_2(test_val))

# Test 2
# Correct result => 'result2'
test_val = 'example2'
print(name_of_solution_1(test_val))
print(name_of_solution_2(test_val))
```

*Note that here I'm using the **simplest** way of testing, printing the results using the [print](https://docs.python.org/3/library/functions.html#print) method. Why? Because I think that the bigger part of the users of this repo isn't familiar with [unit testing](https://en.wikipedia.org/wiki/Unit_testing) and I wanted this part to be intuitive. Btw, I strongly recommend using some unit testing framework for this kind of testing. The Python Standard Library contains a **great** framework for unit testing called [unittest](https://docs.python.org/3/library/unittest.html), or you can install some third-party unit testing framework like [pytest](https://docs.pytest.org/en/latest/).*

### Categories

Each solution/problem in this repo belongs to one of these categories:

1. [Arrays](https://github.com/MTrajK/coding-problems/tree/master/Arrays) - Array Manipulations, Sorting, Binary Search, Divide and Conquer, Sliding Window, etc.
2. [Linked Lists](https://github.com/MTrajK/coding-problems/tree/master/Linked%20Lists) - Linked List Searching, Pointer Manipulations, etc.
3. [Trees](https://github.com/MTrajK/coding-problems/tree/master/Trees) - Binary Search Trees, Tree Traversals: Breadth-First (Level Order) Traversal, Depth-First Traversal (Inorder, Preorder, Postorder), etc.
4. [Hashing DS](https://github.com/MTrajK/coding-problems/tree/master/Hashing%20DS) - Hashing Data Structures: Sets/HashSets and Dictionaries/HashMaps.
5. [Dynamic Programming](https://github.com/MTrajK/coding-problems/tree/master/Dynamic%20Programming) - 2D and 1D Dynamic Programming, LCS, LIS, Knapsack, etc.
6. [Strings](https://github.com/MTrajK/coding-problems/tree/master/Strings) - String Manipulations, Reversing, Encodings/Decodings, etc.
7. [Math](https://github.com/MTrajK/coding-problems/tree/master/Math) - GCD, LCM, Factorization, Geometry, Math Formulas, etc.
8. [Other](https://github.com/MTrajK/coding-problems/tree/master/Other) - Backtracking, BFS, DFS, Stacks, Queues, Deques, Priority Queues (Heaps), Matrices, etc.


## Learning Resources

The learning resources are divided into 4 categories: [Courses](#Courses), [Books](#Books), [Training Sites](#Training-Sites), [Other Resources](#Other-Resources).


### Courses

Collection of free courses from one of the best CS universities.

1. Stanford University
    - [Algorithms Specialization (Coursera)](https://www.coursera.org/specializations/algorithms)
        * [Divide and Conquer, Sorting and Searching, and Randomized Algorithms](https://www.coursera.org/learn/algorithms-divide-conquer)
        * [Graph Search, Shortest Paths, and Data Structures](https://www.coursera.org/learn/algorithms-graphs-data-structures)
        * [Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming](https://www.coursera.org/learn/algorithms-greedy)
        * [Shortest Paths Revisited, NP-Complete Problems and What To Do About Them](https://www.coursera.org/learn/algorithms-npcomplete)
    - [Introduction to Programming Contests - CS 97SI](http://web.stanford.edu/class/cs97si/)

2.  Princeton University
    - [Algorithms Part 1 (Coursera)](https://www.coursera.org/learn/algorithms-part1)
    - [Algorithms Part 2 (Coursera)](https://www.coursera.org/learn/algorithms-part2)
    - [Analysis of Algorithms (Coursera)](https://www.coursera.org/learn/analysis-of-algorithms)

3. UC San Diego
    - [Data Structures and Algorithms Specialization (Coursera)](https://www.coursera.org/specializations/data-structures-algorithms)
        * [Algorithmic Toolbox](https://www.coursera.org/learn/algorithmic-toolbox)
        * [Data Structures](https://www.coursera.org/learn/data-structures)
        * [Algorithms on Graphs](https://www.coursera.org/learn/algorithms-on-graphs)
        * [Algorithms on Strings](https://www.coursera.org/learn/algorithms-on-strings)
        * [Advanced Algorithms and Complexity](https://www.coursera.org/learn/advanced-algorithms-and-complexity)
    - [Data Structures and Performance (Coursera)](https://www.coursera.org/learn/data-structures-optimizing-performance)
    - [edX](https://www.edx.org/school/uc-san-diegox)
        * [Data Structures Fundamentals](https://www.edx.org/course/data-structures-fundamentals)
        * [Algorithmic Design and Techniques](https://www.edx.org/course/algorithmic-design-and-techniques)
        * [Graph Algorithms](https://www.edx.org/course/graph-algorithms)
        * [Data Structures: An Active Learning Approach](https://www.edx.org/course/data-structures-an-active-learning-approach)

4. MIT University
    - [Introduction to algorithms 2005](https://www.youtube.com/playlist?list=PL8B24C31197EC371C) - *[Official MIT page with resources](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-introduction-to-algorithms-sma-5503-fall-2005/)*. Note: this course is the old 6.046J course (the new name is ***Design and analysis of algorithms***, you can find it below).
    - [Introduction to algorithms 2011 - 6.006](https://www.youtube.com/playlist?list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb) - *[Official MIT page with resources](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/)*
    - [Design and analysis of algorithms - 6.046J](https://www.youtube.com/playlist?list=PLUl4u3cNGP6317WaSNfmCvGym2ucw3oGp) - *[Official MIT page with resources](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-046j-design-and-analysis-of-algorithms-spring-2015/index.htm)*
    - [Advanced Data Structures - 6.851](https://www.youtube.com/playlist?list=PLUl4u3cNGP61hsJNdULdudlRL493b-XZf) - *[Official MIT page with resources](http://courses.csail.mit.edu/6.851/spring14/lectures/)*
    - [Advanced Algorithms 2016 - 6.854](https://www.youtube.com/playlist?list=PL6ogFv-ieghdoGKGg2Bik3Gl1glBTEu8c) - *[Official MIT page with resources](http://people.csail.mit.edu/moitra/854.html)*
    - [Programming for the Puzzled 2018 - 6.S095](https://www.youtube.com/playlist?list=PLUl4u3cNGP62QumaaZtCCjkID-NgqrleA) - *[Official MIT page with resources](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-s095-programming-for-the-puzzled-january-iap-2018/)*

5. Harvard University
    - [Advanced algorithms - CS224](https://www.youtube.com/playlist?list=PL2SOU6wwxB0uP4rJgf5ayhHWgw7akUWSf)

6. UC Berkeley
    - [Data Structures - CS61B](https://inst.eecs.berkeley.edu/~cs61b/archives.html)
    - [Efficient Algorithms and Intractable Problems - CS170](https://cs170.org/) - *[YouTube videos](https://www.youtube.com/playlist?list=PLkFD6_40KJIx8lWWbE-Uk069aZ1R-W-VU)*


### Books

Several books that have made an impression on me:

1. [Grokking Algorithms by Aditya Bhargava](https://www.goodreads.com/book/show/22847284-grokking-algorithms-an-illustrated-guide-for-programmers-and-other-curio) - **The best** book for complete beginners in algorithms! I wish this book existed when I started learning algorithms.
2. [Introduction to Algorithms by CLRS](https://www.goodreads.com/book/show/6752187-introduction-to-algorithms) - This book is called the "bible textbook of algorithms" by many programmers.
3. [Algorithms by Robert Sedgewick & Kevin Wayne](https://www.goodreads.com/book/show/10803540-algorithms) - These authors are instructors of the previously mentioned Coursera courses: [Algorithms Part 1](https://www.coursera.org/learn/algorithms-part1) and [Algorithms Part 2](https://www.coursera.org/learn/algorithms-part2). Also, this book has an excellent and free [site](http://algs4.cs.princeton.edu) with exercises, presentations, and examples.
4. [The Algorithm Design Manual by Steven Skiena](https://www.goodreads.com/book/show/425208.The_Algorithm_Design_Manual) - The book describes many advanced topics and algorithms and it focuses on real-life practical examples. This book has [one](http://www.algorist.com) of the best sites with resources ([solutions](http://www.algorist.com/algowiki/index.php/The_Algorithms_Design_Manual_(Second_Edition)), [algorithms and data structures](http://www.algorist.com/algorist.html), [python implementations](http://www.algorist.com/languages/Python.html)).
5. [Algorithms by S. Dasgupta, C. Papadimitriou, and U. Vazirani](https://www.goodreads.com/book/show/138563.Algorithms) - This book is an official book for algorithms and data structures classes in several famous universities.
6. [Competitive Programming 3 by Steven Halim & Felix Halim](https://www.goodreads.com/book/show/22820968-competitive-programming-3) - A great book that prepares you for competitive programming (not for complete beginners). You can learn many things and tricks about competitive programming. *But if your goal is to prepare for competitive programming then choose a faster language than Python, **C/C++** (or Java, it's faster than Python but not like C/C++).*
7. [Cracking the Coding Interview by Gayle Laakmann McDowell](https://www.goodreads.com/book/show/29350585-cracking-the-coding-interview) - A bit different from the previous books. Prepares you for coding interviews using great coding problems.


### Training Sites

If the problems from [LeetCode](https://leetcode.com/) are not enough and you need more problems like those, you can find much more on these platforms:

- [HackerRank](http://hackerrank.com/)
- [CodeChef](http://codechef.com/)
- [HackerEarth](http://hackerearth.com/)
- [CodeForces](http://codeforces.com/)
- [Topcoder](http://topcoder.com/)
- [Project Euler](https://projecteuler.net/)
- [SPOJ](http://www.spoj.com/)
- [PEG](https://wcipeg.com/)
- [Online Judge](https://onlinejudge.org/)
- [E-Olymp](https://www.e-olymp.com/en/)
- [VJudge](https://vjudge.net/)
- [DMOJ](https://dmoj.ca/)
- [USA CO](http://www.usaco.org/)
- [Rosetta Code](http://rosettacode.org/)
- [AtCoder](https://atcoder.jp/)
- [LintCode](http://www.lintcode.com/en/)
- [Kattis](https://www.kattis.com/developers)
- [CodeAbbey](http://codeabbey.com/)
- [CS Academy](https://csacademy.com/)
- [Advent of Code](https://adventofcode.com/)
- [Exercism](https://exercism.io/)
- [CodeFu](https://codefu.mk/)
- [Mendo](https://mendo.mk/Welcome.do)
- [Z-Training](http://www.codah.club/)
- [Codewars](http://www.codewars.com/)
- [Wolfram Challenges](https://challenges.wolfram.com/)
- [Google's Coding Competitions](https://codingcompetitions.withgoogle.com/)
- [Cyber-dojo](https://cyber-dojo.org/)
- [CodingBat](http://codingbat.com/)
- [CodeKata](http://codekata.com/)
- [Daily Coding Problem](https://www.dailycodingproblem.com/)
- [Daily Interview Pro](http://dailyinterviewpro.com/)
- [AlgoDaily](https://algodaily.com/)
- [Codility](https://codility.com/)
- [CoderByte](https://coderbyte.com/)
- [AlgoExpert](https://www.algoexpert.io/)
- [CodeSignal](https://codesignal.com/)
- [Edabit](https://edabit.com/)
- [DevPost](https://devpost.com/)
- [Brilliant](http://brilliant.org/)
- [Codingame](https://www.codingame.com/)
- [CheckiO](http://www.checkio.org/)
- [Kaggle](http://kaggle.com/)
- [Rosalind](http://rosalind.info/problems/locations/)
- [workat.tech](https://workat.tech/problem-solving/practice/)


### Other Resources

1. [Geeks For Geeks](https://www.geeksforgeeks.org/) - The site which **all** interested in algorithms (no matter if beginners or experts) should know! [YouTube channel](https://www.youtube.com/channel/UC0RhatS1pyxInC00YKjjBqQ) with many useful videos.
2. [The Algorithms - Python](https://github.com/TheAlgorithms/Python) - Great GitHub repo with many algorithms written in Python ([Link](https://github.com/TheAlgorithms) from the same repo written in other programming languages).
3. [CP Algorithms](http://cp-algorithms.com/) - Great page with excellent explanations for various algorithms.
4. Visualizers:
    - [USFCA Visualization Tool](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html) - Great tool for visualizing data structures and algorithms, created by the University of San Francisco.
    - [VisuAlgo](https://visualgo.net/en) - Another great tool for visualizing data structures and algorithms through animation.
    - [Algorithm Visualizer](https://algorithm-visualizer.org/) - Interactive online platform that visualizes algorithms from code. This platform is an open-source project, [here](https://github.com/algorithm-visualizer/algorithm-visualizer) you can find the source code.
5. Courses and tutorials (but not from universities like the [Courses](#Courses) section):
    - [Google - Intro to Data Structures and Algorithms](https://www.udacity.com/course/data-structures-and-algorithms-in-python--ud513) - Free course on Udacity offered by Google.
    - [HackerEarth - Tutorials and Practice](https://www.hackerearth.com/practice/) - Practice problems and learn about many algorithms and data structures needed for competitive programming.
    - [KhanAcademy - Algorithms](https://www.khanacademy.org/computing/computer-science/algorithms) - Good explanations for some basic algorithms.
    - [Tutorialspoint - Data Structures and Algorithms](https://www.tutorialspoint.com/data_structures_algorithms/index.htm) - Another platform with good explanations, also Tutorialspoint has free tutorials for almost everything related to CS!
    - [Programiz - Data Structures and Algorithms](https://www.programiz.com/dsa) - One more platform which explains the data structures and algorithms in a simple and interesting way.
    - [Hackr.io - Data Structures and Algorithms Tutorials and Courses](https://hackr.io/tutorials/learn-data-structures-algorithms) - Big collection of tutorials and courses.
    - [Scaler - Data Structures Tutorial](https://www.scaler.com/topics/data-structures/) - Interesting and interactive explanations of some basic data structures.
6. YouTube playlists with tutorials:
    - [Data Structures by mycodeschool](https://www.youtube.com/playlist?list=PL2_aWCzGMAwI3W_JlcBbtYTwiQSsOTa6P)
    - [Data Structures by HackerRank](https://www.youtube.com/playlist?list=PLI1t_8YX-Apv-UiRlnZwqqrRT8D1RhriX)
    - [Algorithms by HackerRank](https://www.youtube.com/playlist?list=PLI1t_8YX-ApvMthLj56t1Rf-Buio5Y8KL)
