from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.entity.models import Contacts
from src.schemas.contacts import ContactSchema, ContactUpdateSchema


async def get_contacts(limit: int, offset: int, db: AsyncSession):
    stmt = select(Contacts).offset(offset).limit(limit)
    contacts = await db.execute(stmt)
    return contacts.scalars().all()


async def get_contact(contact_id: int, db: AsyncSession):
    stmt = select(Contacts).filter_by(id=contact_id)
    contact = await db.execute(stmt)
    return contact.scalar_one_or_none()


async def create_contact(body: ContactSchema, db: AsyncSession):
    contact = Contacts(**body.model_dump(exclude_unset=True))
    db.add(contact)
    await db.commit()
    await db.refresh(contact)
    return contact


# async def update_todo(todo_id: int, body: TodoUpdateSchema, db: AsyncSession):
#     stmt = select(Todo).filter_by(id=todo_id)
#     result = await db.execute(stmt)
#     todo = result.scalar_one_or_none()
#     if todo:
#         todo.title = body.title
#         todo.description = body.description
#         todo.completed = body.completed
#         await db.commit()
#         await db.refresh(todo)
#     return todo
#
#
# async def delete_todo(todo_id: int, db: AsyncSession):
#     stmt = select(Todo).filter_by(id=todo_id)
#     todo = await db.execute(stmt)
#     todo = todo.scalar_one_or_none()
#     if todo:
#         await db.delete(todo)
#         await db.commit()
#     return todo