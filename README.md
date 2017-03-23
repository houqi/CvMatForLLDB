# cvMat for LLDB

This is a script for lldb to debug OpenCV programs. You can print a Mat or just call `imshow` or `imwrite` in lldb just like you are dealing with OpenCV functions.

## What do you expect from this Plugin

This script provide 3 commands for lldb debugger.

- printMat : print an OpenCV Mat
- imwrite  : write an OpenCV Mat to image
- imshow   : show an OpenCV image

You can print a OpenCV Mat, or display the mat as picture, or save the mat as image in lldb debugger.

## How to use it

### Python Dependency

First you have to install opencv for python.

> Note that this script is fully based on the Python API of LLDB. Such API support only the native Python on the OSX. Make sure you can run `import cv2` in your system python.

### Setup LLDB

- Run command as below each time you launch lldb
- Or add a line in ~/.lldbinit and restart lldb

```
# you should fix the path by yourself
command script import "/path/to/cvmat.py"
```

### call printMat or imshow or imwrite

Let's take printMat as an example. In lldb if you run

```
printMat arr
```

You will get

```
flags: 1124024333
type: CV_32F
channels: 2
rows: 5, cols: 5
line step: 40
data address: 0x1029097e0
[[[  0.   1.]
  [  0.   1.]
  [  0.   1.]
  [  0.   1.]
  [  0.   1.]]]
```

## Thanks To

- https://github.com/carlodalmutto/ImageWatchLLDB

## Author

Name : Hou Qi
