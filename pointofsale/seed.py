import os
from datetime import datetime

from dotenv import load_dotenv

from database import Base, SessionLocal, engine
from app.models.category import Category
from app.models.users import User
from app.models.customer import Customer

load_dotenv()


def seed_database():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        category_id = int(os.getenv("DEFAULT_CATEGORY_ID", "1"))
        user_id = int(os.getenv("DEFAULT_ADMIN_ID", "1"))
        customer_id = int(os.getenv("DEFAULT_CUSTOMER_ID", "1"))

        existing_category = db.query(Category).filter(
            Category.category_id == category_id
        ).first()

        if not existing_category:
            default_category = Category(
                category_id=category_id,
                category_name=os.getenv(
                    "DEFAULT_CATEGORY_NAME",
                    "General"
                ),
                description=os.getenv(
                    "DEFAULT_CATEGORY_DESCRIPTION",
                    "Default Category"
                ),
                parent_category_id=None,
                is_active=os.getenv(
                    "DEFAULT_CATEGORY_ACTIVE",
                    "true"
                ).lower() == "true"
            )
            db.add(default_category)

        existing_user = db.query(User).filter(
            User.user_id == user_id
        ).first()

        if not existing_user:
            default_user = User(
                user_id=user_id,
                username=os.getenv(
                    "DEFAULT_ADMIN_USERNAME",
                    "admin"
                ),
                password_hash=os.getenv(
                    "DEFAULT_ADMIN_PASSWORD_HASH"
                ),
                first_name=os.getenv(
                    "DEFAULT_ADMIN_FIRST_NAME",
                    "Admin"
                ),
                last_name=os.getenv(
                    "DEFAULT_ADMIN_LAST_NAME",
                    "User"
                ),
                role=os.getenv(
                    "DEFAULT_ADMIN_ROLE",
                    "Admin"
                ),
                shift_status=os.getenv(
                    "DEFAULT_ADMIN_SHIFT_STATUS",
                    "Clocked Out"
                )
            )
            db.add(default_user)

        existing_customer = db.query(Customer).filter(
            Customer.customer_id == customer_id
        ).first()

        if not existing_customer:
            default_customer = Customer(
                customer_id=customer_id,
                first_name=os.getenv(
                    "DEFAULT_CUSTOMER_FIRST_NAME",
                    "Walk-in"
                ),
                last_name=os.getenv(
                    "DEFAULT_CUSTOMER_LAST_NAME",
                    "Customer"
                ),
                email=os.getenv(
                    "DEFAULT_CUSTOMER_EMAIL",
                    "walkin@example.com"
                ),
                phone_number=os.getenv(
                    "DEFAULT_CUSTOMER_PHONE",
                    "0000000000"
                ),
                loyalty_points=int(
                    os.getenv(
                        "DEFAULT_CUSTOMER_LOYALTY_POINTS",
                        "0"
                    )
                ),
                registration_date=datetime.utcnow()
            )
            db.add(default_customer)

        db.commit()

        print("Successfully seeded database defaults!")

    except Exception as database_error:
        db.rollback()
        raise RuntimeError(
            f"Database seeding failed critically: {database_error}"
        ) from database_error

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()