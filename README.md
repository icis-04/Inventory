# Parts Ledger

## Run it
```bash
cd backend
python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open http://localhost:8000/docs for interactive API docs.
Copy your parts-ledger.html into frontend/index.html to serve it at http://localhost:8000/.

## What's real vs. what's a stub
- Items CRUD, search, filtering, SQLite storage, QR label generation: fully working, tested.
- Photo upload/fetch: fully working, stores JPEGs in backend/photo_storage/.
- app/services/printer.py: stub — wire in python-escpos or brother_ql once you know your printer model.
- app/services/ai_classify.py: stub — needs ANTHROPIC_API_KEY set to call the vision model.

## Next real step
Point the frontend's window.storage calls at these endpoints (fetch('/items'), etc.)
instead of browser storage, so multiple staff/devices share one inventory.
