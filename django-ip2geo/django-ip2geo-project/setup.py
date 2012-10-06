from distutils.core import setup

setup(name='django-ip2geo',
      version='0.1',

      packages=['ip2geo'],
      package_dir={'ip2geo': './ip2geo'},
      
      data_files=[
                  ('django-ip2geo',),
                  ],
      
      url='http://code.google.com/p/django-ip2geo',
      download_url = 'http://code.google.com/p/django-ip2geo/downloads/list',
      description='Simple Django pluggable to get country/region/city from the IP address.',
      long_description='Simple Django pluggable that uses MaxMind (http://www.maxmind.com/) to get country/region/city from the IP address.',
      platforms='python and django platforms',
      author='Paulo Cheque',
      author_email='paulocheque@gmail.com',
      license='MIT',
      )
