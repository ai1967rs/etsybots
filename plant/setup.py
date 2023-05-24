from setuptools import setup, find_packages

```python
setup(
    name='etsy_seo_bot',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'selenium',
        'webdriver_manager',
        'beautifulsoup4',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'etsy_seo_bot=src.main:main',
        ],
    },
)
