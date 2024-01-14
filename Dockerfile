# Dockerfile to build a flask app
# 使用官方 Python 镜像作为基础镜像
FROM python:3.8

# 设置工作目录
WORKDIR /app

# 复制应用程序代码到工作目录
COPY . /app

# 安装应用程序依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露应用程序运行的端口（如果需要）
EXPOSE 5000

# 定义应用程序启动命令
CMD ["python", "app.py"]
