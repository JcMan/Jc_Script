# Jc_Script
这是我日常用到的一些脚本
- ImageSize.py

    这个脚本的作用是改变图片的大小，有下面两种使用方式：

    `python ImageSize.py 0.3`

    `python ImageSize.py a.png 0.3`

    第一种使用方式是将文件夹下的所有图片都变为原来的0.3，第二种使用方式则将`a.png`变为0.3
- Zip.py

    这个脚本的作用是解压当前目录的所有zip文件，它需要一个参数，如下：

    `python Zip.py GBK`

    传入的`GBK`是文件的编码，因为Windows下的默认编码和ubuntu可能不一样，所以需要手动传入一个编码，避免解压之后出现乱码。
