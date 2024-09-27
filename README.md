# file_split 大文件分割
**简介：** 一开始突然有这个需求，很简单，但是懒得写代码，就去网上找，发现网上的代码都是一坨，所以自己花了几分钟写了一份  
**功能：** 大文件切分成多个小文件  
**实例：** 假设你要分割的大文件所在位置为`'./project/big_file'`，你想要将它分割成`10`份，你可以用以下示例代码来实现👇
 ```python
python file_split.py --data_path './project/big_file' --num_splits 10
 ```
