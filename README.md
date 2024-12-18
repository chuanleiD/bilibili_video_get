## bilibili_video_get

一个本地端的，bilibili下载工具

### 一、实现流程

参考：https://blog.csdn.net/knighthood2001/article/details/139014757

1. 使用selenium打开指定链接
2. 获取请求m4s的目标地址
3. 请求两个m4s的目标地址，获取音频和无声的视频
4. 采用ffmpeg合并为最终的视频

### 二、开发环境搭建

1. 在项目根目录下，创建venv虚拟环境

2. 参考`requirements.txt`配置环境

3. 进入虚拟环境，并运行`run.py` 

4. 代码结构如下：

   ```cmd
   tree
   ├─data // 本地cookie保存在这
   ├─venv // 虚拟环境
   ├─run.py // 代码入口
   ├─util
   │  ├─__pycache__
   │  ├─__init__.py
   │  ├─capture.py // 抓包
   │  ├─download.py // 视频下载
   │  ├─initialization.py // 代码环境初始化 
   │  ├─login.py // 利用cookie登录
   │  ├─merge.py // 合并音视频
   │  └─set_options.py // driver配置
   └─requirements.txt // pip需要安装的第三方库
   ```

### 三、发行版本

参考如下方法打包python项目：

[chuanleiD/pystand_go: 一款使用go重写的pystand，用于python项目在windows下更便捷的分发](https://github.com/chuanleiD/pystand_go)

