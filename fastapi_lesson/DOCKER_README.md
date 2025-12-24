# Docker 部署指南

本指南将帮助你使用 Docker 部署 FastAPI 项目。

## 📋 前置要求

- 已安装 Docker Desktop 或 Docker Engine
- 确保 Docker 服务正在运行

## 🚀 快速开始

### 1. 构建 Docker 镜像

在项目根目录下执行：

```bash
docker build -t fastapi-clubs:latest .
```

**命令说明：**
- `docker build`: 构建镜像命令
- `-t fastapi-clubs:latest`: 为镜像打标签（名称:版本）
- `.`: 使用当前目录作为构建上下文

### 2. 运行容器

```bash
docker run -d -p 8000:8000 --name fastapi-app fastapi-clubs:latest
```

**命令说明：**
- `docker run`: 运行容器命令
- `-d`: 后台运行（detached mode）
- `-p 8000:8000`: 端口映射（主机端口:容器端口）
- `--name fastapi-app`: 为容器指定名称
- `fastapi-clubs:latest`: 使用的镜像名称

### 3. 访问应用

容器启动后，可以通过以下地址访问：

- **API 根路径**: http://localhost:8000
- **Swagger UI 文档**: http://localhost:8000/docs
- **ReDoc 文档**: http://localhost:8000/redoc

## 📝 常用 Docker 命令

### 查看运行中的容器

```bash
docker ps
```

### 查看所有容器（包括已停止的）

```bash
docker ps -a
```

### 查看容器日志

```bash
docker logs fastapi-app
```

实时查看日志：

```bash
docker logs -f fastapi-app
```

### 停止容器

```bash
docker stop fastapi-app
```

### 启动已停止的容器

```bash
docker start fastapi-app
```

### 重启容器

```bash
docker restart fastapi-app
```

### 删除容器

```bash
docker rm fastapi-app
```

### 删除镜像

```bash
docker rmi fastapi-clubs:latest
```

### 进入容器内部

```bash
docker exec -it fastapi-app /bin/bash
```

## 🔧 高级用法

### 使用环境变量

如果需要传递环境变量，可以使用 `-e` 参数：

```bash
docker run -d -p 8000:8000 \
  -e ENV_VAR_NAME=value \
  --name fastapi-app \
  fastapi-clubs:latest
```

### 挂载数据卷

如果需要挂载本地目录到容器：

```bash
docker run -d -p 8000:8000 \
  -v /本地路径:/容器路径 \
  --name fastapi-app \
  fastapi-clubs:latest
```

### 使用 docker-compose（推荐用于生产环境）

创建 `docker-compose.yml` 文件：

```yaml
version: '3.8'

services:
  fastapi:
    build: .
    ports:
      - "8000:8000"
    container_name: fastapi-app
    restart: unless-stopped
    environment:
      - PYTHONUNBUFFERED=1
```

然后运行：

```bash
docker-compose up -d
```

停止服务：

```bash
docker-compose down
```

## 🐛 故障排查

### 容器无法启动

1. 查看容器日志：
   ```bash
   docker logs fastapi-app
   ```

2. 检查端口是否被占用：
   ```bash
   lsof -i :8000  # macOS/Linux
   netstat -ano | findstr :8000  # Windows
   ```

### 无法访问应用

1. 确认容器正在运行：
   ```bash
   docker ps
   ```

2. 检查端口映射是否正确：
   ```bash
   docker port fastapi-app
   ```

3. 尝试从容器内部测试：
   ```bash
   docker exec fastapi-app curl http://localhost:8000
   ```

### 重新构建镜像

如果修改了代码或依赖，需要重新构建：

```bash
# 停止并删除旧容器
docker stop fastapi-app
docker rm fastapi-app

# 重新构建镜像（使用 --no-cache 强制重新构建）
docker build --no-cache -t fastapi-clubs:latest .

# 重新运行容器
docker run -d -p 8000:8000 --name fastapi-app fastapi-clubs:latest
```

## 📚 学习资源

- [Docker 官方文档](https://docs.docker.com/)
- [FastAPI 部署文档](https://fastapi.tiangolo.com/deployment/)
- [Dockerfile 最佳实践](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

## 💡 提示

1. **开发环境**：如果需要热重载，可以在 Dockerfile 的 CMD 中添加 `--reload` 参数，但这不推荐用于生产环境。

2. **生产环境**：建议使用多阶段构建、非 root 用户运行、以及使用更轻量的基础镜像（如 `python:3.12-alpine`）。

3. **安全性**：生产环境部署时，考虑添加健康检查、资源限制等配置。

