# 重定向User Data至非C盘

迁移Google User Data至非C盘：

谷歌浏览器重定位了用户数据位置，定位在了D盘的Google文件夹，参考下面链接

https://www.hongkiat.com/blog/install-chrome-different-drive-windows-10/

使用junction.exe工具命令如下：

```bash
junction.exe "C:\Users\dell\AppData\Local\Google\Chrome" "D:\Google"
```

