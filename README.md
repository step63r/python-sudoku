# python-sudoku

## Description

Solve Sudoku (number place) with DFS (backtracking).

## Requirement

- Python 3.7.7
- virtualenv 20.0.31

## Usage

Generate input file such as in ``questions`` directory.

Run script as below to get all solutions.

```
(.env)$ python .\main.py .\questions\sample.txt
1 results, 0.1395 sec
No.1
-------------------------
| 5 3 4 | 6 7 8 | 9 1 2 |
| 6 7 2 | 1 9 5 | 3 4 8 |
| 1 9 8 | 3 4 2 | 5 6 7 |
-------------------------
| 8 5 9 | 7 6 1 | 4 2 3 |
| 4 2 6 | 8 5 3 | 7 9 1 |
| 7 1 3 | 9 2 4 | 8 5 6 |
-------------------------
| 9 6 1 | 5 3 7 | 2 8 4 |
| 2 8 7 | 4 1 9 | 6 3 5 |
| 3 4 5 | 2 8 6 | 1 7 9 |
-------------------------
```

## Install

Fork and clone this repository.

```
$ git clone https://github.com/yourname/python-sudoku.git
```

Create virtualenv (here is example with Windows and PowerShell).

```
$ python -m virtualenv -p "$env:LOCALAPPDATA\Programs\Python\Python37\python.exe" .env
```

Install packages.

```
$ .\env\Scripts\activate
(.env)$ pip install -r .\requirements.txt
```

## Contribution

1. Fork this repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create new Pull Request

## References

- Example questions from [数独問題集](http://www.sudokugame.org/)

## License

MIT License

## Author

[minato](https://blog.minatoproject.com/)
