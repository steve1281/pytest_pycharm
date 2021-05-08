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
```

