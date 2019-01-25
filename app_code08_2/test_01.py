import allure
class Test_001:
    @allure.step(title="步骤1")
    def test_001_1(self):
        print('--->test_001_1')
        assert True
    @allure.step(title="步骤2")
    def test_001_2(self):
        print('--->test_001_2')
        assert False
