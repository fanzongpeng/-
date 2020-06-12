import pytest


class RunDemo:
    def run(self):
        pytest.main(["-s", "-v", r"E:\阳光产险只能生命表系统\test_case\test_logginpage.py"])


if __name__ == '__main__':
    r = RunDemo()
    r.run()
