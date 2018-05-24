from setuptools import setup

setup(
    name='player_session_service',
    author='Christoffer Björkskog',
    author_email='christoffer.bjorkskog@gmail.com',
    url="http://ai.bskog.com",
    py_modules=['main'],
    packages=['app', 'app.apis', 'app.core', 'app.models'],
    version="0.0.1",
    include_package_data=True,
    install_requires=[
        'cassandra-driver',
        'flask',
        'flask-cqlalchemy',
        'flask-restplus',
        'requests',
        'python-dateutil'
        # One could also install dev requirementa here
        # But i feel that for development you should use pipenv on localhost.
    ]
)
