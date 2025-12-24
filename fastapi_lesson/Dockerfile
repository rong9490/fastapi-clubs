# 使用官方 Python 运行时作为基础镜像
FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# 复制依赖文件
COPY requirements.txt .

# 安装 Python 依赖
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY main.py .

# 暴露端口
EXPOSE 8000

# 启动命令
# 使用 uvicorn 运行 FastAPI 应用
# --host 0.0.0.0 允许外部访问
# --port 8000 指定端口
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

