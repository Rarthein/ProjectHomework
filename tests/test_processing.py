import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def status_data():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]


@pytest.mark.parametrize("state, expected_result", [
    ("EXECUTED", [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]),
    ("CANCELED", [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]),
    ("PENDING", [])  # Проверка, когда нет словарей с указанным статусом
])
def test_filter_by_state(status_data, state, expected_result):
    assert filter_by_state(status_data, state) == expected_result


# Дополнительные тесты для проверки конкретных случаев
def test_filter_executed(status_data):
    result = filter_by_state(status_data, "EXECUTED")
    assert result == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]


def test_filter_empty_state(status_data):
    result = filter_by_state(status_data, "")
    assert result == []
