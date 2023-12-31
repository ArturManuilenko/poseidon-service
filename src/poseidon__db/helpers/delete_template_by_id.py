from uuid import UUID

from src.conf.common import POSEIDON__SYS_USER_ID
from src.poseidon__db.helpers.get_template_by_id import get_template_by_id


def delete_template_by_id(template_id: UUID) -> None:
    template = get_template_by_id(template_id)
    template.mark_as_deleted(user_modified_id=UUID(POSEIDON__SYS_USER_ID))
