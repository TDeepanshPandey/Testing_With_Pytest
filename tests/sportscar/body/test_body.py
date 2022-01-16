from pytest import mark

@mark.hello
class BodyTest:
    def test_windshield(self):
        assert True
    def test_door(self):
        assert True
    @mark.smoke
    def test_body_function_as_expected(self):
        assert True

