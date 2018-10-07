# PI_thon_estimate ![PI](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Pi-symbol.svg/1058px-Pi-symbol.svg.png)
This is project 1 for COSC 274, using RNG to prove Ernesto Cesaro's Theorem.

## Overview
To statistically determine the value of Pi based on Ernesto Cesaro's Theorem using the various random number generator facilities. Cesaro's theorem states that given two random integers, x and y, the probability that gcd(x, y) = 1 is 6/(Pi^2). Using random number generators, we can generate statistical estimates of Pi. Note that the random number generator used affects how close the resulting estimate is to Pi (3.1416).

## Authors and Sources
**Authors:** Seth Rasmussen and Chris Patania
**Sources:** The `randomapi.py` module used in this program was made by Mitchell Cohen under the MIT License and the original source can be found at his [Github Page](https://github.com/mitchchn/randomapi/blob/master/randomapi.py)

## Usage (On *nix platforms)
To use this program you can clone this repository to your local machine using this command: `git clone https://github.com/reno777/PI_thon_estimate.git`. After you have cloned it navigate to the directory that you cloned it to, change the file permissions with `chmod u+x PI_thon_estimate.py`, and then use the command `python PI_thon_estimate.py` to state the program. 

Once the program is running it will ask the user to input the first seed value, and then immediately ask for the second seed value. Once this has been completed the program will do the rest and output the results once it is done.

## Dependencies
1. Python 2.7 
   **Note:** As this program was written in python 2.7 syntax it will not run if you are using python 3. 
2. The randomapi module created by Mitchell Cohen.

## Pi Estimation
This program generates a list of 1000 numbers between 1 and 1000. It then takes the list and finds the greatest common divisor(GCD) equaling 1 from each of the numbers using the following code:

```python
for i in range(len(rng_list)-1) : #iterates over the length of the list passed to the function
    if fractions.gcd(rng_list[i],rng_list[i+1]) == 1 : 
        total += 1
```

The actual estimation of Pi happens in this code: `pi = math.sqrt((6*1000)/total)`

## Issues
If the program is not running correctly with `python PI_thon_estimate.py` please ensure that you have python 2.7 installed first. If it is still giving you problems try running it with `python2.7 PI_thon_estimate.py`
