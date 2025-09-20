# Outsourcing Company Management System

This is a Django project with Prisma ORM integration.

## Prerequisites

- Python 3.8+
- Node.js (for Prisma CLI)
- XAMPP (for MySQL)
- Poetry (for dependency management)

## Setup

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   poetry install
   ```

2. **Install Prisma CLI**:
   ```bash
   npm install -g prisma
   ```

3. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```
   Update the `.env` file with your database credentials.

4. **Set up the database**:
   - Start XAMPP and ensure MySQL is running
   - Create a new database using phpMyAdmin or MySQL CLI
   - Update the `DB_NAME` in your `.env` file

5. **Initialize Prisma**:
   ```bash
   cd prisma
   prisma generate
   prisma db push
   ```

6. **Run migrations (when you modify your schema)**:
   ```bash
   prisma migrate dev --name init
   ```

## Project Structure

- `prisma/` - Contains Prisma schema and migrations
  - `schema.prisma` - Database schema definition
  - `prisma.py` - Prisma client initialization
- `.env` - Environment variables (not in version control)
- `.env.example` - Example environment variables
- `requirements.txt` - Python dependencies
- `pyproject.toml` - Project configuration

## Using Prisma in Your Django Project

Import and use the Prisma client in your Django views:

```python
from prisma import prisma

# Initialize the client
prisma.connect()

# Example: Create a new user
user = await prisma.user.create(
    data={
        'email': 'user@example.com',
        'name': 'John Doe'
    }
)

# Example: Query users
users = await prisma.user.find_many()

# Don't forget to disconnect when done
prisma.disconnect()
```

## Development

- Run the development server:
  ```bash
  python manage.py runserver
  ```

- Access the admin interface at `http://localhost:8000/admin/`

## License

MIT
