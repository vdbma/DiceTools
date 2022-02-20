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
$ python DiceTools/main.py -d [challenge rating] [bonus]
```

**Examples**
```
$ python DiceTools/main.py -d 18 5
40 % chances to succed against a rating of 18 with a 5 bonus.
```
```
$ python DiceTools/main.py -d 10 3
70 % chances to succed against a rating of 10 with a 3 bonus.
```
### Compute the average of a complex roll
```
$ python DiceTools/main.py -p [roll]
```
*Note* you need to use quotes if there is a `-` in your roll.

**Examples**
```
$ python DiceTools/main.py -p "1d5 -1d7 +6"
Roll : 1d5  - 1d7  + 6
Average : 5.0
```
```
$ python DiceTools/main.py -p 1d20 + 7   
Roll : 1d20  +  7
Average : 10.5
```
## Contributing

Please make use of `pre-commit` and `pytest` (will be used by the CI).
