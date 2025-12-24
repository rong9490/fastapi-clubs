# 第一个fastapi实例
import uvicorn
from fastapi import FastAPI

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
    # 添加swaggerui依赖：运行前请确保已安装 fastapi[all] 或 fastapi[standard]
    # pip install fastapi[standard]
    # 访问 http://127.0.0.1:8000/docs 可打开Swagger UI文档
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


# # 路径参数; 查询参数(问号?键值对)
# from fastapi import FastAPI

# app = FastAPI()

# @app.get("args1/{id}")
# def path_args1(id: int):
#     return {"msg_id": id}

# # 需要同时两个查询参数才能匹配上; 如何字符串转数字
# @app.get("args2/{id}/{name}")
# def path_args2(id: int, name: str):
#     return {"msg_id": id, "msg_name": name}

# # 查询参数: page / limit; 默认参数;
# @app.get("query1")
# def path_query1(page: int, limit = None):
#     return {"page": page, "limit": limit}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main03:app", reload=True)

def get_full_name(first_name: str, last_name: str) -> str:
    full_name: str = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))