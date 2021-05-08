from typing import Tuple, List

import pytest
from laxleague.guardian import Guardian
from laxleague.player import Player
from testfixtures import TempDirectory


@pytest.fixture
def player_one() -> Player:
    return Player('Tatiana', 'Jones')


@pytest.fixture
def guardians() -> Tuple[Guardian, ...]:
    g1 = Guardian('Mary', 'Jones')
    g2 = Guardian('Joanie', 'Johnson')
    g3 = Guardian('Jerry', 'Johnson')
    return g1, g2, g3


@pytest.fixture()
def guardians_file(dir):
    data = "Mary,Jones\nJoanie,Johnson\nJerry,Johnson"
    return dir.write("test.csv", data.encode())


@pytest.fixture()
def guardians_list() -> List[Guardian]:
    return [Guardian(first_name='Mary', last_name='Jones'),
            Guardian(first_name='Joanie', last_name='Johnson'),
            Guardian(first_name='Jerry', last_name='Johnson')]


@pytest.fixture()
def dir():
    with TempDirectory() as d:
        yield d