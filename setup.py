from setuptools import setup, find_packages

setup(
    name='Py3rebase',
    version='3.1.1',
    url='https://github.com/fullbore/Pyrebase',
    description='A simple python wrapper for the Firebase API',
    author='Ben McNelly',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='Firebase',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'requests==2.24.0',
        'gcloud==0.18.3',
        'oauth2client==4.1.3',
        'requests_toolbelt==0.9.1',
        'python_jwt==3.2.6',
        'pycryptodome==3.9.8',
        'urllib3==1.25.9'
    ]
)
