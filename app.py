from fastapi import FastAPI, Depends,Body
from typing import Annotated,Optional
import uvicorn
from pydantic import BaseModel, Field

app = FastAPI()

class CreatePost(BaseModel):
    title: str
    content: str
async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    print('in common')
    return {"q": q, "skip": skip, "limit": limit}
@app.get("/blogs")
async def blog_list(params:Annotated[dict, Depends(common_parameters)]):
    print("inside")
    return {"results": [1,2,3,4,5]}

@app.get("/{test}")
def test(test:int, is_private: bool):
    return {"message": {test}}

@app.post("/create")
def CreatBlogPost(post: CreatePost = Body()):
    return post

if __name__=="__main__":
    uvicorn.run(app)