from setuptools import setup, find_packages
import sys

try:
    import mdtraj
except ImportError:
    print('Building and running clustering requires mdtraj. See '
          'http://mdtraj.org/latest/installation.html for help!')
    sys.exit(1)

setup(name='clustering',
      version='0.1',
      description=('Cluster analysis tool for heterogenous lipid ' +
                   'membranes.'),
      url='https://github.com/uppittu11/clustering',
      author='Parashara Shamaprasad',
      author_email='p.shama@vanderbilt.edu',
      license='MIT',
      packages=['clustering'],
      package_dir={'clustering': 'clustering/'},
      include_package_data=True,
      install_requires=["mdtraj"],
)