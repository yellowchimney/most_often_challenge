from lib.most_often import MostOften

def test_add_returns_updated_list():
    mostoften = MostOften([])
    mostoften.add_new("string")
    result = mostoften.starting_list

    assert result == ["string"]

def test_returns_for_empty_list():
    mostoften = MostOften([])
    result = mostoften.get_most_often()

    assert result == "no clear winner"

def test_returns_item_from_single_item_list():
    mostoften = MostOften([1])
    result = mostoften.get_most_often()

    assert result == 1

def test_returns_for_two_distinct_items():
    mostoften = MostOften([1, 2])
    result = mostoften.get_most_often()

    assert result == "no clear winner"

def test_returns_most_often_infirst_position():
    mostoften = MostOften([1, 1, 2])
    result = mostoften.get_most_often()
    
    assert result == 1
    
def test_returns_most_often_in_second_position():
    mostoften = MostOften([1, 2, 2])
    result = mostoften.get_most_often()

    assert result == 2