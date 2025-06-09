# DiceTools
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Set of tools for D&D dice actions !

## Contents

<!-- toc -->

- [Installation](#installation)
- [Usage](#usage)
  * [Compute the chance to succed a challenge](#compute-the-chance-to-succed-a-challenge)
    + [Roll with an advantage](#roll-with-an-advantage)
    + [Roll with a disadvantage](#roll-with-a-disadvantage)
  * [Compute the average of a complex roll](#compute-the-average-of-a-complex-roll)
  * [Compute the full distribution of a complex roll](#compute-the-full-distribution-of-a-complex-roll)
  * [Compare two distribution](#compare-two-distribution)
  * [Roll a complex roll](#roll-a-complex-roll)
  * [Compute the expected number of rolls for a saving throw with bonus](#compute-the-expected-number-of-rolls-for-a-saving-throw-with-bonus)
- [Contributing](#contributing)

<!-- tocstop -->

## Installation

Clone this repo with

```
$ git clone https://github.com/vdbma/DiceTools
```

Install with
```
$ pip install -e .
```
while in the repository directory (`-e` option will auto-update the package for your python environement when pulling newer versions).

## Usage

### Compute the chance to succed a challenge

```
$ dicetools -d [challenge rating] [bonus]
```

**Examples**
```
$ dicetools -d 18 5
40 % chances to succed against a rating of 18 with a +5 bonus.
```
```
$ dicetools -d 10 3
70 % chances to succed against a rating of 10 with a +3 bonus.
```
#### Roll with an advantage
Use the `-A` option :
```
$ dicetools -d 18 5 -A
64.00 % chances to succed against a rating of 18 with a +5 bonus with advantage.
```
#### Roll with a disadvantage
Use the `-D` option :
```
$ dicetools -d 18 5 -D
16.00 % chances to succed against a rating of 18 with a +5 bonus with disadvantage.
```

### Compute the average of a complex roll
```
$ dicetools -a [roll]
```
*Note* you need to use quotes if there is a `-` in your roll.

**Examples**
```
$ dicetools -a "1d5 -1d7 +6"
Roll : 1d5  - 1d7  + 6
Average : 5.0
```
```
$ dicetools -a 1d20 + 7
Roll : 1d20  +  7
Average : 17.5
```

### Compute the full distribution of a complex roll
```
$ dicetools -s [roll]
```
*Note* you need to use quotes if there is a `-` in your roll.

You can use the `--mpl` option to have a matplotlib plot of the distribution instead of it being printed in the terminal.

**Examples**
```
$ dicetools -s 2d6
Roll : 2d6
Average : 7.0
Distribution :
2:   2.8 %     ██████████
3:   5.6 %     ████████████████████
4:   8.3 %     ███████████████████████████████
5:   11.1 %    █████████████████████████████████████████
6:   13.9 %    ███████████████████████████████████████████████████
7:   16.7 %    ██████████████████████████████████████████████████████████████
8:   13.9 %    ███████████████████████████████████████████████████
9:   11.1 %    █████████████████████████████████████████
10:  8.3 %     ███████████████████████████████
11:  5.6 %     ████████████████████
12:  2.8 %     ██████████
```

### Compare two distribution
```
$ dicetools -s [roll] -c [second roll]
```
*Note* you need to use quotes if there is a `-` in your roll.

You can use the `--mpl` option to have a matplotlib plot of the distribution instead of it being printed in the terminal.

The second roll distribution is printed in red.

### Roll a complex roll
```
$ dicetools -r [roll]
```
*Note* you need to use quotes if there is a `-` in your roll.

**Examples**
```
$ dicetools -r "1d5 -1d7 +6"
Roll : 1d5  - 1d7  + 6
Result : 7 (4, 3)
```
```
$ dicetools -r 1d20 + 7
Roll : 1d20  +  7
Result : 9 (2,)
```

### Compute the expected number of rolls for a saving throw with bonus

```
$ dicetools -w [bonus/malus]
```
This computes the expectation value for a propability law :
<img src="https://render.githubusercontent.com/render/math?math=P(X=n) = p(1-p)^{n-1}">
for which the expectation value is
<img src="https://render.githubusercontent.com/render/math?math=E(X) = \frac{1}{p}">


**Examples**
```
$ dicetools -w -5
For a saving throw with bonus -5, the expected number of rolls is 3.33
```
```
$ dicetools -w 3
For a saving throw with bonus +3, the expected number of rolls is 1.43
```

## Contributing

Please make use of `pre-commit` and `pytest` (will be used by the CI).
