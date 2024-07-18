from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(username='Luis', email='luis@email.com', password='GqgY42')
    session.add(user)
    session.commit()
    result = session.scalar(select(User).where(User.email == 'luis@email.com'))
    assert result.id == 1
    assert result.username == 'Luis'
    assert result.email == 'luis@email.com'
