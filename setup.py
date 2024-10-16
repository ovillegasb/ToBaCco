"""Installation file."""

from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

setup(
    name="ToBaCco",
    version="3.1.0",
    packages=find_packages(),
    install_requires=install_requires,
    author="Orlando Villegas",
    author_email="ovillegas.bello0317@gmail.com",
    description='Topological MOF generator by molecular block alignment.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/ovillegasb/tobacco',
    classifiers=[  # Clasificadores opcionales
        "Programming Language :: Python :: 3",
        "LICENSE :: OSI APPROVED :: GNU GENERAL PUBLIC LICENSE V3 (GPLV3)",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'tobacco=tobacco.__main__:main',
        ],
    },
    package_data={
        'tobacco': ['data/.gitkeep'],
    },
    python_requires='>=3.9'
)