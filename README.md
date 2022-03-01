# DiceTools
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Set of tools for D&D dice actions !

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
40 % chances to succed against a rating of 18 with a 5 bonus.
```
```
$ dicetools -d 10 3
70 % chances to succed against a rating of 10 with a 3 bonus.
```
### Compute the average of a complex roll
```
$ dicetools -p [roll]
```
*Note* you need to use quotes if there is a `-` in your roll.

**Examples**
```
$ dicetools -p "1d5 -1d7 +6"
Roll : 1d5  - 1d7  + 6
Average : 5.0
```
```
$ dicetools -p 1d20 + 7
Roll : 1d20  +  7
Average : 17.5
```

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

### Compute the expected number of rolls for a save roll with bonus

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
For a save roll with bonus -5, the expected number of roll is 2.33
```
```
$ dicetools -w 3
For a save roll with bonus +3, the expected number of roll is 0.43
```

## Contributing

Please make use of `pre-commit` and `pytest` (will be used by the CI).
