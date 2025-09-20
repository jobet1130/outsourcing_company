import os
from pathlib import Path
from dotenv import load_dotenv
from prisma import Prisma, register
from prisma.models import User  # Example model import

# Load environment variables from .env file
load_dotenv()

# Initialize Prisma client
prisma = Prisma()

# Register the client to be accessible globally
register(prisma)

def init_prisma():
    """Initialize the Prisma client and connect to the database."""
    prisma.connect()
    
    # Create database tables if they don't exist
    # This will be handled by Prisma's migration system
    # Run `prisma db push` to sync your schema with the database
    
    return prisma

def disconnect_prisma():
    """Disconnect the Prisma client."""
    if prisma.is_connected():
        prisma.disconnect()

# Example usage:
# prisma = init_prisma()
# user = await User.prisma().create(data={
#     'email': 'user@example.com',
#     'name': 'John Doe'
# })
# disconnect_prisma()
