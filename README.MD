# 背景
使用poetry构建工具打包python程序,基于aiohttp异步发送压力

# 安装依赖
```
poetry install 
```

# 虚拟环境
```
virtualenv -p /Library/Frameworks/Python.framework/Versions/3.6/bin/python3 --no-site-packages venv
```

# 本地调试
```
poetry run python3 -m poetry_project --thread-count 100 --load-time 1  --load-url http://127.0.0.1:8763/hi
```

# 本地打包
```
poetry build 
```

# 本地安装
```
pip3 install /dist/poetry_project-0.1.0.tar.gz
```

# 卸载项目
```
pip3 uninstall poetry-project
```

# 正式运行
```
poetry_run --thread-count 100 --load-time 1  --load-url http://127.0.0.1:8763/hi
```

# pip安装
```
pip3 install git+https://github.com/xinxi1990/poetry_project.git@master
```

# git release
```
git tag -a v1.0 -m "relase 1.0版本"

git push origin v1.0
```


# 参考

poetry使用
```
https://testerhome.com/topics/20929
```