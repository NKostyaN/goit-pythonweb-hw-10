from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from src.database.db import get_db
from src.database.models import Contact, User
from src.services.contacts import ContactBookService
from src.services.auth import get_current_user
from src.schemas import ContactSet, ContactGet, ContactUpdate

from typing import List

router = APIRouter(prefix="/contacts")


@router.get("/", response_model=List[ContactGet])
async def get_all_contacts(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
) -> List[Contact]:
    contact_service = ContactBookService(db)
    contacts = await contact_service.get_all_contacts(skip, limit, user)
    return contacts


@router.get("/{contact_id}", response_model=ContactGet)
async def get_contact(
    contact_id: int,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
) -> Contact:
    contact_service = ContactBookService(db)
    contact = await contact_service.get_contact(contact_id, user)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact


@router.post("/", response_model=ContactGet, status_code=status.HTTP_201_CREATED)
async def create_contact(
    body: ContactSet,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    contact_service = ContactBookService(db)
    return await contact_service.create_contact(body, user)


@router.patch("/{contact_id}", response_model_exclude_unset=True)
async def update_contact(
    body: ContactUpdate,
    contact_id: int,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    contact_service = ContactBookService(db)
    contact = await contact_service.update_contact(contact_id, body, user)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return contact


@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_contact(
    contact_id: int,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    contact_service = ContactBookService(db)
    contact = await contact_service.remove_contact(contact_id, user)
    if contact is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found"
        )
    return None


@router.get("/birthdays/", response_model=List[ContactGet])
async def get_birthdays(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    contact_service = ContactBookService(db)
    return await contact_service.get_birthdays(skip, limit, user)


@router.get("/find/", response_model=List[ContactGet])
async def find_contacts(
    query: str,
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    user: User = Depends(get_current_user),
):
    contact_service = ContactBookService(db)
    return await contact_service.find_contacts(query, skip, limit, user)
