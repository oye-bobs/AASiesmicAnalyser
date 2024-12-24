from setuptools import setup, find_packages

setup(
    name="siesmc_ai_cleaner",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "segyio>=1.9.0",
        "scipy>=1.7.0",
        "scikit-learn>=0.24.0",
        "matplotlib>=3.4.0",
        "pytest>=6.2.5",
        "pyyaml>=5.4.1",
        "click>=8.0.0",
        "seaborn>=0.11.0"
    ],
    entry_points={
        'console_scripts': [
            'siesmic=src.cli:cli',
        ],
    },
)
