# 第一个fastapi实例
from fastapi import FastAPI
import uvicorn

# 实例化服务
app = FastAPI()

# 路由端点注册
# 根路径
@app.get("/")
def read_root():
    return {"Hello": "World!"} # 原样返回字典

# 启动服务(服务器uvicorn), 默认端口8000
# 1.命令启动: uvicorn main01:app --reload
# Application startup complete. 重新编译
# 2.通过调试: fastapi dev main01.py
# 3.通过py执行: python main01.py
# 引入uvicorn指定参数

if __name__ == "__main__":
    uvicorn.run("main01:app", host="127.0.0.1", port=8000, reload=True)
