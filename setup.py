from setuptools import setup


setup(
    # Because django-statsd was taken, I called this django-statsd-mozilla.
    name='django-statsd-mozilla',
    version='0.4.0',
    description='Django interface with statsd',
    long_description=open('README.rst').read(),
    author='Andy McKay',
    author_email='andym@mozilla.com',
    license='BSD',
    install_requires=['statsd >= 2.1.2, != 3.2 , <= 4.0'],
    packages=['django_statsd',
              'django_statsd/patches',
              'django_statsd/clients',
              'django_statsd/loggers',
              'django_statsd/management',
              'django_statsd/management/commands'],
    url='https://github.com/django-statsd/django-statsd',
    entry_points={
        'nose.plugins.0.10': [
            'django_statsd = django_statsd:NoseStatsd'
        ]
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)
