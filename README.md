# readme

```
See website/youtube:

https://www.jetbrains.com/pycharm/guide/tutorials/visual_pytest/
https://www.youtube.com/watch?v=mLYTP41H8U0

credit to creator: Paul Everitt. 

This is just my code from his tutorial.
```


## setup python environment

```
pyenv local 3.9.2
virtualenv virtualenv
```

## install pycharm (ubuntu 20)

```
sudo snap install pycharm-community --classic
/snap/pycharm-community/238/bin/pycharm.sh .
```

## misc stuff

```
From within the terminal inside pycharm, we did a :

pip install -e .[tests]

We also split the editor vertically, and set the font size to 18, set the ptester to pytest, and set up the default python to the one in the virtualenv.
```

## directory structure:

```
steve@steve-VirtualBox:~/projects/pytest_pycharm$ tree -I virtualenv
.
├── README.md
├── requirements.txt
├── setup.py
├── src
│   ├── laxleague
│   │   ├── guardian.py
│   │   └── player.py
│   └── laxleague.egg-info
│       ├── dependency_links.txt
│       ├── PKG-INFO
│       ├── requires.txt
│       ├── SOURCES.txt
│       └── top_level.txt
└── tests
    ├── conftest.py
    ├── __init__.py
    ├── pytest.ini
    ├── test_guardian.py
    └── test_player.py

4 directories, 15 files

```

## revision May 8, 2021

```
added code to read guardians from a csv file.
added code to write guardians to a csv file.
added code that will load a csv file base don the player name (and tests with a method mock)
```


## coverage example (May 8, 2021)

 
```
Needed to:  pip3 install pytest-cov

Then:

steve@steve-VirtualBox:~/projects/pytest_pycharm$ pytest --cov=src/ --verbose
============================= test session starts ==============================
platform linux -- Python 3.9.2, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /home/linuxbrew/.linuxbrew/opt/python@3.9/bin/python3.9
cachedir: .pytest_cache
rootdir: /home/steve/projects/pytest_pycharm
plugins: cov-2.11.1
collected 8 items                                                              

tests/test_guardian.py::test_construction PASSED                         [ 12%]
tests/test_player.py::test_construction PASSED                           [ 25%]
tests/test_player.py::test_add_guardian PASSED                           [ 37%]
tests/test_player.py::test_add_guardians PASSED                          [ 50%]
tests/test_player.py::test_primary_guardian PASSED                       [ 62%]
tests/test_player.py::test_no_primary_guardian PASSED                    [ 75%]
tests/test_player.py::test_read_guardians_from_csv PASSED                [ 87%]
tests/test_player.py::test_write_guardians_to_csv PASSED                 [100%]

----------- coverage: platform linux, python 3.9.2-final-0 -----------
Name                        Stmts   Miss  Cover
-----------------------------------------------
src/laxleague/guardian.py       5      0   100%
src/laxleague/player.py        26      0   100%
-----------------------------------------------
TOTAL                          31      0   100%


============================== 8 passed in 0.06s ===============================
```

