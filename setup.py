from distutils.core import setup
import os

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
#
# Cribbed from James Bennett's setup.py because I was lazy
# <james@b-list.org>  -- <http://www.b-list.org/>
#
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('as_eimp'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'):
            del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[13:]  # Strip "approvals/" or "approvals\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))


setup(name='django-as_eimp',
      version='0.0',
      description='A djano app for managing Electric Imps',
      author='Eric Scanner Luce',
      author_email='scanner@apricot.com',
      url='http://github.com/scanner/django-as_eimp/',
      package_dir={'as_eimp': 'as_eimp'},
      packages=packages,
      package_data={'as_eimp': data_files},
      classifiers=['Development Status :: Alpha',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
