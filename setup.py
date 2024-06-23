from setuptools import setup

setup(
    name='vreedb-python',
    version='0.0.1',
    description='the vreedb python client',
    url='https://github.com/spookieoli/vreedb-python',
    author='Oliver Sharif',
    author_email='Oliver.Sharif@protonmail.com',
    license='apache 2',
    packages=['vreedb'],
    install_requires=['httpx>=0.27.0', 'setuptools'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Everyone',
        'License :: OSI Approved :: Apache 2 License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MS :: Windows',
        'Programming Language :: Python :: 3.10+',
    ],
)
