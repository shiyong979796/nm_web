#:@ TIME 2021/12/23   10:53
#:@FILE  path.py
#:@EMAIL  1557225637@QQ.COM
import os

base_dir=os.path.dirname(os.path.abspath(__file__))

log_file_dir=os.path.join(base_dir,r'output','log')

report_dir=os.path.join(base_dir,r'output','allure_report')

error_picture_dir=os.path.join(base_dir,r'output','error_picture')

allure_dir=os.path.join(base_dir,'output','allure_report')


if __name__ == '__main__':
    print(base_dir)
    print(log_file_dir)
    print(error_picture_dir)
    print(allure_dir)