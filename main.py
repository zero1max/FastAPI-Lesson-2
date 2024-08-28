from fastapi import FastAPI, Query, Path
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

# feed_query = Query(max_length=30)

# @app.get('/news/feed')
# async def news_feed(search: Annotated[list[str] | None, feed_query] = None):
#     return {"news": ['new1', 'new2', 'new3'], 'serach_key':search}

# ----------------------------------------------------------------------------------------------------------

# feed_query = Query(max_length=30, title='Qidiruv kaliti', description="Lorem Ipsum")

# @app.get('/news/feed')
# async def news_feed(search: Annotated[str , feed_query] = 'all'):
#     return {"news": ['new1', 'new2', 'new3'], 'serach_key':search}

# ----------------------------------------------------------------------------------------------------------

# feed_query = Query(max_length=30, title='Qidiruv kaliti', description="Lorem Ipsum", alias='news-query', include_in_schema=False)

# @app.get('/news/feed')
# async def news_feed(search: Annotated[str , feed_query] = 'all'):
#     if search:
#         pass
#     return {"news": ['new1', 'new2', 'new3'], 'serach_key':search}

# ----------------------------------------------------------------------------------------------------------

# @app.get('/news/feed/{category}')
# async def news_feed(
#     category: str, 
#     search: str = 'all'):
#     if search:
#         pass
#     return {"news": ['new1', 'new2', 'new3'],"category": category ,'serach_key':search}

# ----------------------------------------------------------------------------------------------------------

@app.get('/news/feed/{new_id}')
async def news_feed(
    new_id: Annotated[int, Path(title='News ID', gt=0, le=100)], 
    search: str = 'all'):
    if search:
        pass
    return {"news": ['new1', 'new2', 'new3'], "new_id": new_id ,'serach_key':search}

# gt = greater than > >= gt. ge    =====    < <=  lt. le