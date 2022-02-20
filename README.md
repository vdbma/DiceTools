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

## Contributing

Please make use of `pre-commit` and `pytest` (will be used by the CI).
