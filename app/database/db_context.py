from contextlib import contextmanager

import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from app.database.db_models import Base

main_engine = sa.create_engine(
    'sqlite:///database.db',
    echo=True,
)

DBSession = sessionmaker(
    bind=main_engine,
    expire_on_commit=False,
)

@contextmanager
def session_scope():
    """Provides a transactional scope around a series of operations."""
    session = DBSession()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
    
def create_db():
    Base.metadata.create_all(main_engine)    
    
def delete_db():
    Base.metadata.drop_all(main_engine)
        
# Tests
if __name__ == '__main__':
    delete_db()
    create_db()    
#     with session_scope() as s:
#         <actual_code>
