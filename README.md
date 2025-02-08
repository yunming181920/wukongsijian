# wukongsijian
该代码用于造4悟空刷四剑，建议百万战力带二阶魂斧和主线饰品，最好有时装。
## 部署流程
* exe运行
夸克链接(https://pan.quark.cn/s/40cbe5835427)
看说明！！！看说明！！！看说明！！！图片需要自己替换一下。
直接运行里面的exe文件即可，有问题走python渠道。
* python环境配置
  python渠道可以用来改其他角色(如果复读技能就能过四剑的话)
  直接去浏览器搜索pycharm，下载一个pycharm社区版(免费)。新建一个项目，pycharm会让你下载一个python环境，直接下载就好，将本项目复制到新建的项目里面。
  
  看说明！！！看说明！！！看说明！！！图片需要自己替换一下。
  
  按win+左将pycharm放在左边，将360游戏大厅的造4放在右边
  进入左侧工具栏里面的terminal/命令行
  ```
  cd game
  pip install numpy
  pip install opencv-python
  pip install pyautogui
  pip install pygetwindow
  python script.py
  ```
  
## 说明
由于我是第一次写脚本，对于图像匹配的设计还有问题，代码中仅仅实现了像素级匹配，也就是说用户在使用这个代码时，对于关键的图片还需要自己再去截一遍。
对于各种程序中刷新时间的设置，在refresh函数中修改时间即可，函数中的文件命名应该很容易知道是哪个步骤的时停。
每天第一次启动造4和进入不周山会有提示，需要自己手动点掉。
