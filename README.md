# Simple python test playground.

To run all tests, call 
```python
python -m unittest discover -p '*_test.py'
```

This is a very simple console program that uses a function wrapped inside a 
decorator. The tests focus on showing how we can mock a decorator.

This program requires at least Python 3.7.

### Use the program.
```python
# The only allowed names are 'Juan', 'Joseph' and 'Kalyan'.
# All other names will raise an exception.
python main.py
```
