from app.core import security


def test_verify_password():
    assert (
        security.verify_password("adminnimda", "$2b$12$aeT7eHQ4DssYDyRtFiXgounhOYm9GvamKJgVOo3r8FuxXNFA17INy") is True
    )
