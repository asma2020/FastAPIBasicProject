from .engine_sync import Base
from .models import User
__all__ = [
  "Base",
  "User",
 ]

Base.metadata.create_all(bind = engine_sync)