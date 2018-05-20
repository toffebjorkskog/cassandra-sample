from setuptools import setup

setup(
    name='player_session_service',
    packages=['app'],
    version="0.0.1",
    include_package_data=True,
    install_requires=[
        'cassandra-driver',
        'flask',
        'flask-cqlalchemy',
        'flask-restplus',
        'requests'
    ]
)
