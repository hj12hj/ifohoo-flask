下载项目后 进入 lib 文件夹下 执行 pip3 install -r requirements.txt 安装依赖
[]: # Title: README
当你新导入依赖后到lib文件夹下执行 pip3 freeze > requirements.txt

当客户无外网部署时候
本地下载依赖
pip3 download --platform anylinux_x86_64 --no-deps on -d pip_packages/ -r requirements.txt
服务器执行
pip3 install --no-index --find-links=lib -r requirements.txt

centos安装Dm驱动
驱动包在dmlib目录下
https://cloud.tencent.com/developer/article/1912401

64位机器安装oracle环境
https://blog.csdn.net/qq_49122165/article/details/125660284

centos服务器安装 python3.9
https://www.cnblogs.com/rainbow-tan/p/16330525.html
