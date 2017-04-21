import os
from setuptools import setup, find_packages

package_name = 'PulseEffects'
locale_dir = 'share/locale/'
os.makedirs(locale_dir, exist_ok=True)

po_dir = 'po/'

po_files = [x for x in os.listdir(po_dir) if x[-3:] == ".po"]

langs = [x.split('.')[0] for x in po_files]

for lang in langs:
    mo_path = locale_dir + lang + '/LC_MESSAGES/'

    os.makedirs(mo_path, exist_ok=True)

    po_path = po_dir + lang + '.po'

    cmd_list = ['msgfmt', po_path, '-o', mo_path + package_name + '.mo']

    os.system(' '.join(cmd_list))


setup(name='PulseEffects',
      version='1.1.9',
      description='Audio effects for Pulseaudio applications',
      url='https://github.com/wwmm/PulseEffects',
      author='wwmm',
      author_email='wellington.melo@cefet-rj.br',
      license='GPL3',
      packages=find_packages(),
      install_requires=[
          'gi',
          'gst-plugins-good',
          'gst-plugins-bad',
          'gst-python',
          'swh-plugins'
      ],
      scripts=['pulseeffects'],
      include_package_data=True,
      zip_safe=False)
