import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("butenkosergii")
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    assert r["total_count"] == 42
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("katekvitna")
    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_singl_char_can_be_found(github_api):
    r = github_api.search_repo("s")
    assert r["total_count"] != 0


@pytest.mark.api
def test_emoji_foggy_exists(github_api):
    r = github_api.get_emoji()
    assert "foggy" in r


@pytest.mark.api
def test_emoji_testemoji_not_exists(github_api):
    r = github_api.get_emoji()
    assert "testemoji" not in r


@pytest.mark.api
def test_get_emoji_status_200(github_api):
    r = github_api.get_emoji_status()
    assert r.status_code == 200


@pytest.mark.api
def test_get_emoji_status_not_304(github_api):
    r = github_api.get_emoji_status()
    assert r.status_code != 304
