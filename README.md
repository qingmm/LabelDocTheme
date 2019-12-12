# LabelDocTheme

基于**PyQT**实现了一个可执行程序，能够打开存储字典列表数据的文件，并逐行读取显示其指定字段，并提供文本框便于对其进行主题标注。且由于我的数据为英文，因此调用了百度翻译进行实时翻译，提高效率。

## 代码说明

***nlp_anotation.py***为主要代码文件，***translate.py***中提供了百度翻译的函数，使用前需先在百度翻译申请*api*和*key*方能使用，***py2exe.py***为生成可执行文件的代码，若修改了主文件的名称，则需在***py2exe.py***中进行相应的修改。***test.json***为测试数据。

## 运行环境

***ubuntu16.04***
***python3.6***
***PyQt5***

## 使用方法

使用前请先配置好PyQt5，PyQt4与5之间差异较大，不能保证兼容。

`python nlp_anotation.py` 直接运行弹出界面窗口。(此处要注意，*python* 需要为配置好 *PyQt5* 的 *python* )

`python py2exe.py` 生成可执行文件，在当前目录下 *dist* 文件夹内，可以看到 ***nlp_anotation*** 可执行文件。未在*windows*环境下测试，但只要*python*与*PyQt*版本一致，代码应该是可移植的。若要在*Windows*下运行，则需要在***nlp_anotation.py***中修改默认打开目录。

在最下方的文本框中可手动输入标签，点击*Next*显示下一条记录，代码会自动将输入过的标签添加到下拉框中，减少人工操作量，注意*label*之间是以`;`分割的。

界面如下图所示：

![界面截图](https://github.com/qingmm/LabelDocTheme/blob/master/show.png)
