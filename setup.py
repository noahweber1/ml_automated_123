
from distutils.core import setup
setup(
  name = 'ml_automated_123',         # How you named your package folder (MyLib)
  packages = ['ml_automated_123'],   # Chose the same as "name"
  version = "1.0.0",      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Automated machine learning',   # Give a short description about your library
  author = 'Noah Weber',                   # Type in your name
  author_email = 'noahweber53@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/noahweber1/ml_automated',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Automated ML'],   # Keywords that define your package best
  install_requires=['hyperopt>=0.2',
                      'networkx>=2.1',
                      'numpy>=1.17',
                      'pandas>=0.24',
                      'scikit-learn>=0.22',
                      'xgboost>=0.9'],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)