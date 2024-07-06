from setuptools import setup, find_packages

setup(
    name='howto',
    version='0.1.0',
    author='w1redch4d',
    description='ChatGPT without API from your terminal',
    packages=find_packages(where='src'),  
    package_dir={'': 'src'},  
    install_requires=[
        'requests',
        'pybase64',
        'distro'
    ],

    entry_points={
        'console_scripts': [
            'howto = howto.howto:main',
        ]
    },
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown'
)
