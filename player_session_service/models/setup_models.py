from player_session_service import create_app


if __name__ == '__main__':
    app = create_app()
    from player_session_service.models import db
    db.sync_db()
