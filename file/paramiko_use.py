#-*- coding:utf-8 -*-
"""
==============================================================================
Time : 2022/10/1
Author : Dufy
使用paramiko 进行与远程服务器的文件传递
參考： https://www.361shipin.com/blog/1515924524430786560
==============================================================================
"""
import paramiko
import logging, traceback
import os


class FileTransmit:
    """
    文件传递
    """
    def __init__(self, ip,port,user,pwd):
        pass
        self.ip = ip
        self.port = port
        self.user = user
        self.pwd = pwd
        self.client = paramiko.Transport((self.ip, self.port))
        self.client.connect(username=self.user,
                            password=self.pwd)
        self.err_count = 0

    def sftp_upload(self, remote_path, local_path):
        """
        # remote_path = r"/000000000009.jpg"
        # local_path = r"D:\code\python\test/000000000009.jpg"
        """
        try:
            sftp = paramiko.SFTPClient.from_transport(self.client)

            # 使用paramiko上传文件到远程主机
            sftp.put(local_path,remote_path)
        except:
            logging.error(traceback.format_exc())
            self.err_count += 1
            logging.error(f'远程目录:\n {remote_path} \nOR \n'
                            f'{"/".join(remote_path.split("/")[:-1])}\n不存在!! '
                            f'please check it')

    def sftp_download(self, remote_path, local_path):
        """
        从远程下载文件到本地
        Args:
            remote_path:
            local_path:

        Returns:

        """
        try:
            sftp = paramiko.SFTPClient.from_transport(self.client)
            sftp.get(remote_path, local_path)
            print(f'{self.ip}远程下载 {remote_path} 完毕！')
        except:
            logging.error(traceback.format_exc())


    def end_operation(self):
        self.client.close()

if __name__ == "__main__":
    pass
    ip = "10.208.17.106"
    local_path = r'C:\Users\Downloads'
    file_name = 'yolo7-v100-out-20221009.log'
    a = FileTransmit(ip,22,"root","123")
    a.sftp_download(f'/root/yolov7/{file_name}', os.path.join(local_path, file_name))
    a.end_operation()

