from setuptools import setup, find_packages

setup(
    name='events',
    version='0.1.0',
    description="A super fast, memory effcient events system for Python",
    author="Ahmed Rakan",
    author_email="ar.aldhafeeri11@gmail.com",
    packages=['events'],
    install_requires=[
        # Add any dependencies here
    ],
    test_suite='tests',
)