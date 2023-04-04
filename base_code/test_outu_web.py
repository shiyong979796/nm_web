#:@ TIME 2021/11/22   16:11
#:@FILE  test_outu_web.py
#:@EMAIL  1557225637@QQ.C
import pytest


class Test_project:

    # @classmethod
    # def setup_class(cls):
    #     print('类级别前置方法--------------》')
    #
    # @classmethod
    # def teardown_class(cls):
    #     print('类级别后置方法--------------》')
    #
    #
    #
    # def setup(self):
    #     print('前置方法 ----------->setup')
    #
    # def teardown(self):
    #     print('后置方法------------》teardown')

    def add(self, *args):
        sum = 0
        if args:
            for i in args:
                sum += i
            return sum

    def test_add1(self):

        assert 500 == self.add(100, 400)
