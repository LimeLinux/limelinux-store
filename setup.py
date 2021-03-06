#!/usr/bin/env python

from setuptools import setup, find_packages
import glob
import os

os.system('pyrcc5 limestorelib.qrc -o limestorelib/resource.py')

datas = [
    ('/usr/share/applications', glob.glob("data/*.desktop")),
    ('/etc/skel/.config/autostart', ['data/limelinux-updater.desktop']),
    ('/usr/share/icons/hicolor/scalable/apps', ['data/limelinux-store.svg','data/limelinux-updater.svg']),
    ('/usr/share/icons/hicolor/scalable/mimetypes', ["data/application-x-pisi.svg"]),
    ('/usr/share/limelinux-store/languages',glob.glob("languages/*.qm")),
    ('/usr/share/limelinux-store/apps', glob.glob("apps/*.svg"))
]

setup(
    name = "limelinux-store",
    scripts = ["limelinux-store","limelinux-updater"],
    packages = find_packages(),
    version = "1.0",
    license = "GPL v3",
    description = "Lime GNU/Linux Store And Updater",
    author = "Fatih KAYA",
    author_email = "sonakinci41@gmail.com",
    url = "https://github.com/limelinux/LimeLinux-Store",
    keywords = ["PyQt5"],
    data_files = datas
)
