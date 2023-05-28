import paramiko
from path import erp_file_path, erp_file_path2
import time


def run_erp(order_sn):
    # 通过文件读取本地私钥，可以设置password，我们这里没有设置
    private_key = paramiko.RSAKey.from_private_key_file(erp_file_path)

    # 创建SSH对象
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname='34.238.212.241', port=38022, username='ec2-user', pkey=private_key)

    # 执行命令
    start_time = time.time()
    print(f'开始同步订单({order_sn})到erp')
    stdin, stdout, stderr = ssh.exec_command(
        f'sudo php /var/www/http/zzcms-test4/htm/index.php syncer/syncOne/order_sn/{order_sn}')

    # 获取命令结果
    result = stdout.read()
    # print(result.decode('utf-8'))
    end_time = time.time()
    print(f'成功同步订单({order_sn})到erp,耗时 {end_time - start_time}')

    ssh.close()


def run_erp2():
    # 通过文件读取本地私钥，可以设置password，我们这里没有设置
    private_key = paramiko.RSAKey.from_private_key_file(erp_file_path2)

    # 创建SSH对象
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname='16.162.224.248', port=38022, username='azerp', pkey=private_key)

    stdin, stdout, stderr = ssh.exec_command(
        'sudo php /var/www/http/erp400/protected/yiic azReserveOrderInventory createAzReserveRecord')

    # 获取命令结果
    result = stdout.read()
    print(result.decode('utf-8'))
    ssh.close()

if __name__ == '__main__':
    run_erp2()
