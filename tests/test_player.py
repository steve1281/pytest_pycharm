import pytest

from laxleague.player import Player


def test_construction(player_one):
    assert 'Jones' == player_one.last_name
    assert 'Tatiana' == player_one.first_name
    assert [] == player_one.guardians


def test_add_guardian(player_one, guardians):
    player_one.add_guardian(guardians[0])
    assert [guardians[0]] == player_one.guardians


# @pytest.mark.skip(reason="blah")
def test_add_guardians(player_one, guardians):
    player_one.add_guardian(guardians[0])
    player_one.add_guardians((guardians[1], guardians[2]))
    assert list(guardians) == player_one.guardians


# @pytest.mark.skip(reason="blah")
def test_primary_guardian(player_one, guardians):
    player_one.add_guardian(guardians[0])
    player_one.add_guardians((guardians[1], guardians[2]))
    assert guardians[0] == player_one.primary_guardian


# def test_no_primary_guardian(player_one):
#    with pytest.raises(IndexError) as exc:
#        player_one.primary_guardian
#    assert 'list index out of range' == str(exc.value)


def test_no_primary_guardian(player_one):
    assert None is player_one.primary_guardian


def test_read_guardians_from_csv(player_one, guardians_list, guardians_file):
    player_one.load_guardian_file(guardians_file)
    assert player_one.guardians == guardians_list


def test_write_guardians_to_csv(player_one, guardians, temp_dir):
    player_one.add_guardians(guardians)
    path = temp_dir.path + "/test.csv"
    player_one.write_guardians_file(path=path)
    p = Player("Test", "Name")
    p.load_guardian_file(path)
    assert p.guardians == player_one.guardians
