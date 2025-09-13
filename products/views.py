import requests
from django.shortcuts import render
from django.http import JsonResponse

# Frontend home (renders index.html)
def frontend_home(request):
    return render(request, "index.html")

# Search endpoint (calls external API)
def search_products(request):
    query = request.GET.get("q", "")
    if not query:
        return JsonResponse({"results": []})

    # Example external API (replace with real one)
    api_url = f"https://dummyjson.com/products/search?q={query}"
    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        data = response.json()

        # Adapt results to match your frontend structure
        results = [
            {
                "id": item.get("id"),
                "name": item.get("title"),
                "brand": item.get("brand", "N/A"),
                "price": item.get("price"),
                "currency": "USD",  # or parse if API provides
                "total_weight": "N/A",
                "image": item.get("thumbnail"),
                "url": f"https://dummyjson.com/products/{item.get('id')}",
            }
            for item in data.get("products", [])
        ]

        return JsonResponse({"results": results})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


# Optional: Get all products from external API
def all_products(request):
    try:
        response = requests.get("https://dummyjson.com/products?limit=20", timeout=5)
        response.raise_for_status()
        data = response.json()

        results = [
            {
                "id": item.get("id"),
                "name": item.get("title"),
                "brand": item.get("brand", "N/A"),
                "price": item.get("price"),
                "currency": "USD",
                "total_weight": "N/A",
                "image": item.get("thumbnail"),
                "url": f"https://dummyjson.com/products/{item.get('id')}",
            }
            for item in data.get("products", [])
        ]

        return JsonResponse({"results": results})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
