import asyncio

# Dummy product database
PRODUCTS_DB = [
    {"name": "Apple iPhone 15", "brand": "Apple", "total_weight": "200g", "price": "999", "currency": "$", "url": "https://apple.com/iphone-15"},
    {"name": "Samsung Galaxy S23", "brand": "Samsung", "total_weight": "210g", "price": "899", "currency": "$", "url": "https://samsung.com/galaxy-s23"},
    {"name": "Sony Headphones", "brand": "Sony", "total_weight": "250g", "price": "199", "currency": "$", "url": "https://sony.com/headphones"},
]

async def search_products_pipeline(query: str):
    await asyncio.sleep(0)  # simulate async
    query_lower = query.lower()
    # Return products that contain the query in the name
    return [p for p in PRODUCTS_DB if query_lower in p["name"].lower()]
