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
(.env)$ python .\main.py .\questions\20200801.txt
File: 20200801.txt
1 results, 0.0815 sec
No.1
-------------------------
| 6 5 7 | 4 8 3 | 2 9 1 |
| 1 2 9 | 7 6 5 | 4 8 3 |
| 4 8 3 | 1 9 2 | 7 6 5 |
-------------------------
| 3 9 4 | 5 1 6 | 8 2 7 |
| 7 6 2 | 3 4 8 | 1 5 9 |
| 8 1 5 | 9 2 7 | 6 3 4 |
-------------------------
| 5 4 6 | 2 7 9 | 3 1 8 |
| 2 3 1 | 8 5 4 | 9 7 6 |
| 9 7 8 | 6 3 1 | 5 4 2 |
-------------------------

--------------------------------------------------
Complete!!
--------------------------------------------------
Elapsed Time: 0.0815 sec
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
