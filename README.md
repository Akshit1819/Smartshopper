🛒 SmartShopper

SmartShopper is a smart shopping assistant built with Django + Django REST Framework.
It helps users search for products (e.g., “365 WholeFoods Peanut Butter”) and instantly fetches structured product information such as name, brand, price, and weight.

The system is optimized for speed and scalability using async requests, caching, and a Django API backend.

🚀 Features

🌐 Web frontend with a clean, attractive UI (Home & About pages).

⚡ Real-time product information pipeline.

🔄 Parallel/async requests for faster performance.

🗄️ Caching to reduce repeated fetch times.

🔌 Exposed as a REST API for external clients.

 

⚙️ Installation & Setup
1️⃣ Clone the repo
git clone https://github.com/your-username/smartshopper.git
cd smartshopper

2️⃣ Create and activate virtual environment
python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On Mac/Linux

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run migrations
python manage.py migrate

5️⃣ Start the development server
python manage.py runserver


Now visit 👉 http://127.0.0.1:8000/

🔗 API Endpoints
Test API
GET /api/test/


Response:

{"message": "Django REST Framework is working 🚀"}

Product Search API (planned)
GET /api/search/?q=peanut+butter


Response:

[
  {
    "name": "365 WholeFoods Peanut Butter",
    "brand": "WholeFoods",
    "price": "$5.99",
    "weight": "16oz"
  }
]

🛠️ Tech Stack

Django

Django REST Framework

Python Asyncio

Requests / HTTPX

SQLite (default DB)

📌 Next Steps

✅ Add product search scraping logic.

✅ Improve caching (Redis/Database).

✅ Deploy to cloud (Heroku / AWS / Render).

✅ Add user accounts for personalized shopping.
