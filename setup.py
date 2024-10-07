from setuptools import setup, find_packages

setup(
    name="unit_converter",
    version="0.1",
    author="Twinkel-Twinkel",
    author_email="None",
    description="Library untuk konversi unit panjang, berat, suhu, dan waktu",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)