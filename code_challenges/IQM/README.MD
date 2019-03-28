# Dexcom Code Chalenge

## Refactoring (Part 1)

I've refactored the code so that it is much easier to read and follows some of Python's PEP8 best practices.
The first step was renaming some of the variables in order to make the code clearer and more easily understood.
For example, since we're using Interquartile Mean, instead of using the variable `q` to represent quartile I've renamed it to `quartile`, which provides a more direct correlation. I've also put the code blocks into their own functions which allows them to be reusable. I've put some code comments into some of my methods explaining in detail why it's better to use them this way.

I've seperated the code into 3 seperate files:

- `create_data.py`:
  This script runs the file creation of `data.txt`

- `incremental_interquartile_mean.py`:
  This runs the Interquartile Mean and performs the heavy lifting.

- `main.py`:
  I import `create_data` and `incremental_interquartile_mean` as Python modules into this script which follows a more Object Oriented Design. It also cleans it up and makes it a little more readable.

## Optimization (Part 2)

Refactoring the script was the easy part. The more challenging bit was trying to find a much faster way of calculating IQM. I first noticed that the main issue of time was due to the sorting algorithm used. Python's built-in sort method uses a pretty good sorting algorithm that's based on Insertion Sort and Merge Sort. The algorithm is called Timsort and it's the main algorithm used for Python's `sorted()` and `sort()` methods along with Java's `Arrays.sort()`.

It starts off by sorting small pieces using Insertion Sort, then merges the pieces using merge of merge sort. We divide the Array into blocks known as Run. We sort those runs using insertion sort one by one and then merge those runs using combine function used in merge sort. If the size of Array is less than run, then Array get sorted just by using Insertion Sort. The size of run may vary from 32 to 64 depending upon the size of the array. Note that merge function performs well when sizes subarrays are powers of 2. The idea is based on the fact that insertion sort performs well for small arrays.

This is usually a good enough algorithm to use in general but when it comes to a sorted list of items, like the example we're dealing with, the better approach is to use Binary Search. It is a search algorithm that finds the position of a target value within a sorted array. Binary search compares the target value to the middle element of the array. If they are not equal, the half in which the target cannot lie is eliminated and the search continues on the remaining half, again taking the middle element to compare to the target value, and repeating this until the target value is found.

I ended up using a Python module called `bisect`, which uses Binary Search under the hood. The module provides support for maintaining a list in sorted order without having to sort the list after each insertion. This is essential as this reduces overhead time required to sort the list again and again after insertion of each element.

After running both instances 3 times each I compared the time it took on average. This is on an early 2015 Macbook Pro:

    2.9 GHz Intel Core i5
    16 GB 1867 MHz DDR3

- Using the built-in `sort()` method (Timsort):
  `real    12m56.799s`

Now let's see how Binary Search works:

- `real    8m24.075s`

As you can see the final result is much faster. This approach works well with the given challenge of 100,000 integers. If the challenge were to increase to a million or a billion input values I believe the method of Binary Search would still work but there is a concern of "integer overflow". Per Wikipedia, "An integer overflow occurs when an arithmetic operation attempts to create a numeric value that is outside of the range that can be represented with a given number of digits – either larger than the maximum or lower than the minimum representable value." From my research into the bisect method it looks like most of the issues with integer overflow have been fixed but there is yet another issue of resources. With an increase in input values you have the issue of an increase of memory usage, processing power and storage. This is highly dependant on the computer running this algorithm.

If we needed to store the intermediate state between each IQM calculation in a data store I don't think this method would change much. We would probably have to change the storage from an array into a datastore endpoint which would still act as an array or a linked list. Here is a quote direct from redis: "Lists: collections of string elements sorted according to the order of insertion. They are basically linked lists." Redis is not a plain key-value store, it is actually a data structures server, supporting different kinds of values.