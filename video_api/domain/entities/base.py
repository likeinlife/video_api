import uuid
from dataclasses import dataclass, field


@dataclass(frozen=True, eq=False)
class BaseEntity:
    id: uuid.UUID = field(default_factory=uuid.uuid4, kw_only=True)
