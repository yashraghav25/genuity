# setup.py for genuity_os
from setuptools import setup, find_packages

setup(
    name='genuity_os',
    version='0.1.0',
    description='A Python library for generative models, differential privacy, and tabular data synthesis.',
    author='Shivansh Gupta',
    author_email='g.shivansh@iitg.ac.in',
    url='https://github.com/yashraghav25/genuity_os',
    packages=find_packages(),
    install_requires=[
        "pandas>=1.3",
        "numpy>=1.21",
        "scikit-learn>=1.0",
        "torch>=1.9",
        "category-encoders>=2.6",
        "joblib>=1.2",
    ],
    python_requires='>=3.9',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    include_package_data=True,
    package_data={
        '': ['*.md', '*.txt']
    },
    entry_points={
        'console_scripts': [
            'genuity-cli=genuity.cli:main',
        ],
    },
)
