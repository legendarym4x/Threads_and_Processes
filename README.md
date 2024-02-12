## Homework 03

### The first part is for threads

We wrote a program for processing the folder `"folder1"`, which `sorts` files in the specified folder by extensions using several streams. Accelerated processing of attached directories and files due to parallel execution 
of traversal of all folders in separate threads. The most time-consuming will be transferring a file and getting a list of files in a folder (iteration over the contents of the directory).

### The second part is for processes

We wrote an implementation of the `factorize` function, which accepts a list of numbers and returns a list of numbers into which the numbers from the input list are divided without a remainder.

Implemented the synchronous version and measured the execution time.

Then improved the performance of our function by implementing multiple CPU cores for parallel computation and measured the execution time again.

The `cpu_count()` function from the `multiprocessing` package was used to determine the number of cores on the machine.

