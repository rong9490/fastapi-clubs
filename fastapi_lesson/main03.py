# 路径参数; 查询参数(问号?键值对)
from fastapi import FastAPI

app = FastAPI()

@app.get("args1/{id}")
def path_args1(id: int):
    return {"msg_id": id}

# 需要同时两个查询参数才能匹配上; 如何字符串转数字
@app.get("args2/{id}/{name}")
def path_args2(id: int, name: str):
    return {"msg_id": id, "msg_name": name}

# 查询参数: page / limit
@app.get("query1")
def path_query1(page: int, limit: int):
    return {"page": page, "limit": limit}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main03:app", reload=True)
