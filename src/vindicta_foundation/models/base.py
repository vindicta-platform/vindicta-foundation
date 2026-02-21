from datetime import datetime
from uuid import UUID, uuid4
from pydantic import BaseModel, ConfigDict, Field


class VindictaModel(BaseModel):
    """
    Base model for all Vindicta Platform entities.

    Constitutional Compliance:
    - Rule VII: All models must be strictly typed and serializable.
    - Rule XVI: Async-first mandate requires efficient serialization.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        frozen=False,
        validate_assignment=True,
        json_encoders={UUID: str, datetime: lambda v: v.isoformat()},
    )

    id: UUID = Field(
        default_factory=uuid4, description="Unique identifier for the entity"
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow, description="Timestamp of creation"
    )
    updated_at: datetime | None = Field(
        default=None, description="Timestamp of last update"
    )
