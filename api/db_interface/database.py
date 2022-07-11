from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

PGHOST= os.getenv("PGHOST")
PGDATABASE= os.getenv("PGDATABASE")
PGUSER= os.getenv("PGUSER")
PGPASWORD= os.getenv("PGPASSWORD")

SQLALCHEMY_DATABASE_URL = f"postgresql://{PGUSER}:{PGPASWORD}@{PGHOST}:15432/{PGDATABASE}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
