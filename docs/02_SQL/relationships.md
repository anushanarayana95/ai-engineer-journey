# Database Relationships

## One-to-One
One record relates to exactly one other record.

Example:
User ↔ Passport

---

## One-to-Many
One parent has many children.

Example:
One Category → Many Articles

---

## Many-to-Many
Both sides can have multiple relationships.

Example:
Users ↔ Bookmarked Articles

Implemented using a bridge table:

Bookmarks

user_id
article_id