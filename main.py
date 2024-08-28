from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

# @app.get('/news/feed')
# async def news_feed(search: str = 'all'):
#     return {"news": ['new1', 'new2', 'new3'], 'serach_key':search}

# ----------------------------------------------------------------------------------------------------------

# @app.get('/news/feed')
# async def news_feed(search: str , start_date: str | None = None):
#     return {"news": ['new1', 'new2', 'new3'], 'serach_key':search, 'start_date':start_date}

# ----------------------------------------------------------------------------------------------------------

# @app.get('/news/feed')
# async def news_feed(search: Annotated[str | None, Query(max_length=30, min_length=5)] = None):
#     return {"news": ['new1', 'new2', 'new3'], 'serach_key':search}

# --- OR ---

# feed_query = Query(max_length=30, min_length=5, pattern="[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+")

# @app.get('/news/feed')
# async def news_feed(search: Annotated[str | None, feed_query] = None):
#     return {"news": ['new1', 'new2', 'new3'], 'serach_key':search}

# ----------------------------------------------------------------------------------------------------------

feed_query = Query(max_length=30)

@app.get('/news/feed')
async def news_feed(search: Annotated[list[str] | None, feed_query] = None):
    return {"news": ['new1', 'new2', 'new3'], 'serach_key':search}