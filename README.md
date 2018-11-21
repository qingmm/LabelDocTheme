# LabelDocTheme
基于PyQT实现了一个可执行程序，能够打开存储字典列表数据的文件，并逐行读取显示其指定字段，并提供文本框便于对其进行主题标注。且由于我的数据为英文，因此调用了百度翻译进行实时翻译，提高效率。
运行环境：ubuntu16.04 python3.6 PyQt5
使用方法：python nlp_anotation.py直接运行弹出界面窗口。
python py2exe.py生成可执行文件，在当前目录下dist文件夹内，可以看到nlp_anotation可执行文件。未在windows环境下测试，但只要python与PyQt版本一致，代码应该是可移植的。
