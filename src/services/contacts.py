from sqlalchemy.ext.asyncio import AsyncSession

from src.repository.contacts import ContactBookRepository
from src.schemas import ContactSet, ContactUpdate

from src.database.models import User


class ContactBookService:
    def __init__(self, db: AsyncSession):
        self.contact_repository = ContactBookRepository(db)

    async def create_contact(self, body: ContactSet, user: User):
        return await self.contact_repository.create_contact(body, user)

    async def get_all_contacts(self, skip: int, limit: int, user: User):
        return await self.contact_repository.get_all_contacts(skip, limit, user)

    async def get_contact(self, contact_id: int, user: User):
        return await self.contact_repository.get_contact(contact_id, user)

    async def update_contact(self, contact_id: int, body: ContactUpdate, user: User):
        return await self.contact_repository.update_contact(contact_id, body, user)

    async def remove_contact(self, contact_id: int, user: User):
        return await self.contact_repository.remove_contact(contact_id, user)

    async def get_birthdays(self, skip: int, limit: int, user: User):
        return await self.contact_repository.get_birthdays(skip, limit, user)

    async def find_contacts(self, query: str, skip: int, limit: int, user: User):
        return await self.contact_repository.find_contacts(query, skip, limit, user)
