from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

class Links(Base):
    __tablename__ = "links"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    dest_url: Mapped[str]
    slug: Mapped[str] = mapped_column(unique=True)