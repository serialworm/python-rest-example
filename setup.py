from setuptools import setup

setup(name='python-rest-example',
      version='0.1',
      description='REST api example',
      url='https://github.com/serialworm/python-rest-example',
      author='serialworm',
      author_email='eric.beringer@gmail.com',
      license='MIT',
      install_requires=[
        'beautifulsoup4',
        'falcon',
        'Flask',
        'itsdangerous',
        'Jinja2',
        'MarkupSafe',
        'python-mimeparse',
        'requests',
        'requests-cache',
        'six',
        'Werkzeug'
      ],
      zip_safe=False)
