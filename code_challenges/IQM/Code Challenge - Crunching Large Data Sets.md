# Dexcom Code Challenge -- Crunching Large Data Sets

-------------------------------------------------------


## BACKGROUND:

When working with large data sets at Dexcom, we often do not have the luxury of being able to make large calculations from scratch.  Instead, we need to be able to perform calculations incrementally as data is added to the system.


The included Python code sample calculates the Incremental Interquartile Mean of a large data set.  The data.txt file contains 100,000 integer values between 0 and 600.  The given code calculates the Interquartile Mean of the first 4 values in the data set, then the first 5 values, then the first 6 values, etc, until it has calculated the IQM of all 100,000 values (99997 IQM calculations total).


This problem is meant to give you the chance to show us the way you go about solving problems and the techniques you use when developing software.  The more you tell us about your thinking and reasons behind the work you’ve done, the better understanding we’ll have of how you work!


## INSTRUCTIONS:

The challenge has two parts. You may attempt *one* or the *other*, or *both*. If you attempt both parts, submit a single code file that includes all changes.


## PART 1: REFACTORING

The code provided is written in a very rudimentary style. It is difficult to understand, and does not communicate intent or functionality.


Can you improve the code such that:


1. It communicates function and intention clearly, AND

2. It is the kind of code YOU want to read and write.


Please provide your code, any tests you create, and answers to the following questions:


1. Explain your improvement process, and why you chose each step.

2. What improvements did you make to ensure that future developers could quickly and easily understand this code?


## PART 2: OPTIMIZATION

The code provided is slow.  On a 2015 MacBook Pro it takes around 4 minutes to execute.

Can you optimize the code such that:


1. It runs significantly faster, AND

2. It still produces the same output as the example code, for the given data.txt input, AND

3. It still calculates the Incremental Interquartile Mean after each value is read, AND

4. It will continue to produce correct output given any data set with any number of integer values between 0 and 600.


Please provide the optimized code, an automated test that proves that your code works, and answers to the following questions:


1. Explain how your optimization works and why you took this approach

2. Would your approach continue to work if there were millions or billions of input values?

3. Would your approach still be efficient if you needed to store the intermediate state between each IQM calculation in a data store?  If not, how would you change it to meet this requirement?
