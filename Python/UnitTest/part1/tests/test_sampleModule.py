from part1.myApp.sampleModule import Add,checkAge
import pytest

@pytest.mark.skip
class TestAdd:
    def test_Add(self):
        assert Add(1, 2) == 3

    def test_Add_fail(self):
        with pytest.raises(AssertionError):
            assert Add(3, 4) == 10

    def test_Add_str(self):
        assert Add("a", "b") == 'ab'


    def test_Add_str2(self):
        assert Add('5', '6') == '56'
class TestcheckAge :
    def test_checkAge(self):
        assert checkAge(5) == 5
    def test_checkAge_fail(self):
        with pytest.raises(ValueError,match='Incorrect Age') as e:
            checkAge(-2)

