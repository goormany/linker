import pytest


@pytest.mark.parametrize(
    "url",
    [
        ("google.com"),
        ("https://youtube.com"),
        ("tg.me://MyChanell"),
        ("string"),
        ("https://yandex.ru?page=1"),
        ("http://mphelper.space/"),
    ],
)
async def test_create_and_get_short_url(ac, url):
    response = await ac.post("/", json={"dest_url": url})
    assert response.status_code == 200

    data = response.json()
    data = data.get("data", None)
    assert isinstance(data, dict)
    assert "dest_url" in data
    assert "slug" in data

    dest_url_from_api = data["dest_url"]
    slug_from_api = data["slug"]

    assert dest_url_from_api == url

    data = await ac.get(f"/{slug_from_api}")
    assert data.status_code == 302

    assert "location" in data.headers
    location = data.headers["location"]
    assert location == dest_url_from_api
