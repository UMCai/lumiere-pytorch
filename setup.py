from setuptools import setup, find_packages

setup(
  name = 'lumiere-pytorch',
  packages = find_packages(exclude=[]),
  version = '0.0.1',
  license='MIT',
  description = 'Lumiere',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/lucidrains/lumiere-pytorch',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'text-to-video'
  ],
  install_requires=[
    'einops>=0.7.0',
    'einx[torch]>=0.1.3',
    'torch>=2.0'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)
