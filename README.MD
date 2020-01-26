# 背景
使用poetry构建工具打包python程序,使用命令行运行

# 安装依赖
```
poetry install 
```

# 本地调试
```
poetry run python3 -m poetry_project --thread-count 10
```

# 本地打包
```
poetry build 
```

# 本地安装
```
pip3 install /dist/poetry_project-0.1.0.tar.gz
```

# 正式运行
```
poetry_run --thread-count 10
```

# pip安装
```bash
pip3 install git+https://github.com/xinxi1990/poetry_project.git@master
```

