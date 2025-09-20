from setuptools import setup, find_packages

setup(
    name="prisma_client",
    version="0.1.0",
    packages=find_packages(include=['prisma', 'prisma.*']),
    python_requires=">=3.8",
    install_requires=[
        'prisma-client>=0.10.0',
    ],
)
