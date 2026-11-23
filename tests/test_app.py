from app.main import app
client = app.test_client()
def test_health():
    assert client.get("/health").status_code == 200
def test_search_sanitizes():
    r = client.get("/search?q=<script>alert(1)</script>")
    assert b"<script>" not in r.data
