import pytest

# pytest.main(['-s','-v','--reruns',"2",'--reruns-delay','5',r'--alluredir=output\allure_report','-m mark1'])
pytest.main(['-s', '-v', '--reruns', "2", '--reruns-delay', '5', r'--alluredir=.output\allure_report'])
