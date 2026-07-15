# Source Model

## Purpose

The `Source` model stores information about the news publisher or organization.

Examples:

* BBC
* CNN
* NDTV
* Reuters
* The Hindu

Instead of storing the source name repeatedly inside every article, the application stores it once and links articles using a Foreign Key.

This reduces duplicate data and follows database normalization principles.

---

# Source Model Structure

```python
class Source(Base):
    __tablename__ = "sources"

    id = Column(Integer, primary_key=True)

    name = Column(String, unique=True, nullable=False)

    country = Column(String)

    articles = relationship(
        "Article",
        back_populates="source"
    )
```

---

# Fields

## id

```python
id = Column(Integer, primary_key=True)
```

### Purpose

Unique identifier for every news source.

Examples:

| id | Source |
| -- | ------ |
| 1  | BBC    |
| 2  | CNN    |
| 3  | NDTV   |

A Primary Key:

* must be unique
* cannot be NULL
* identifies one row

---

## name

```python
name = Column(String, unique=True, nullable=False)
```

### Purpose

Stores the name of the news organization.

Examples:

* BBC
* CNN
* Reuters
* NDTV

### Why String?

A source name is text.

### Why nullable=False?

Every source must have a name.

Without a name, the source has no identity.

### Why unique=True?

Each news organization should exist only once in the database.

Without `unique=True` this could happen:

| id | name |
| -- | ---- |
| 1  | BBC  |
| 2  | BBC  |

This creates duplicate source records.

Making the name unique ensures all articles reference the same source.

---

## country

```python
country = Column(String)
```

### Purpose

Stores the country where the news organization belongs.

Examples:

* UK
* USA
* India

### Why is it optional?

Some APIs provide country information.

Some do not.

The application can still function without this information.

Therefore:

```python
country = Column(String)
```

is better than

```python
country = Column(String, nullable=False)
```

---

## articles

```python
articles = relationship(
    "Article",
    back_populates="source"
)
```

### Purpose

Creates a one-to-many relationship.

One Source

↓

Many Articles

Example:

BBC

↓

* AI News
* Space News
* Sports News

Now SQLAlchemy allows:

```python
bbc.articles
```

instead of writing SQL JOIN queries manually.

---

# Relationship

```text
Source

↓

One

↓

Many

↓

Articles
```

Each article belongs to exactly one source.

Each source can publish many articles.

---

# Business Rules

* Every source must have a unique name.
* Every source must have an ID.
* Country information is optional.
* One source can publish many articles.
* Duplicate news organizations should not exist.

---

# Database Concepts Used

* Primary Key
* Unique Constraint
* Nullable Fields
* One-to-Many Relationship
* SQLAlchemy relationship()

---

# Interview Questions

## Why is the source name unique?

Because every news organization should exist only once in the database.

This prevents duplicate source records and ensures all related articles reference the same source.

---

## Why is country optional?

Some news providers do not return country information.

The application can still function correctly without it.

Therefore, the field is optional.

---

## Why use relationship()?

It allows SQLAlchemy to navigate between Python objects.

Example:

```python
bbc.articles
```

instead of writing SQL JOIN statements manually.

---

# Key Takeaways

* The Source model stores information about news organizations.
* `id` uniquely identifies each source.
* `name` is required and unique.
* `country` is optional.
* One source can have many articles.
* `relationship()` makes related objects easy to access.
* The Source model follows database normalization by storing publisher information only once.
