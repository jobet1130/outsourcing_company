import os
import sys
import subprocess
import platform
from pathlib import Path

def run_command(command, cwd=None):
    """Helper function to run shell commands with better error handling."""
    print(f"Running: {' '.join(command)}")
    try:
        subprocess.run(
            command,
            cwd=cwd,
            check=True,
            shell=platform.system() == 'Windows',
            stdout=sys.stdout,
            stderr=sys.stderr
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def setup_prisma():
    print("Setting up Prisma client...")
    
    # Get project root directory
    project_root = Path(__file__).parent.absolute()
    prisma_dir = project_root / "prisma"
    
    print("\n1. Installing Python dependencies...")
    if not run_command([sys.executable, "-m", "pip", "install", "-U", "prisma"]):
        print("Failed to install Python dependencies.")
        sys.exit(1)
    
    print("\n2. Installing Node.js dependencies...")
    os.chdir(prisma_dir)
    
    # Install npm packages locally
    if not run_command(["npm", "install"], cwd=prisma_dir):
        print("Failed to install Node.js dependencies.")
        sys.exit(1)
    
    print("\n3. Generating Prisma client...")
    if not run_command(["npx", "prisma", "generate"], cwd=prisma_dir):
        print("Failed to generate Prisma client.")
        
        # Try alternative approach if the first one fails
        print("\nTrying alternative approach...")
        if not run_command(["npx", "prisma", "generate", "--schema=./prisma/schema.prisma"], cwd=project_root):
            print("Alternative approach also failed.")
            sys.exit(1)
    
    print("\nPrisma client setup completed successfully!")
    print("You can now import and use the Prisma client in your Python code.")

if __name__ == "__main__":
    setup_prisma()
