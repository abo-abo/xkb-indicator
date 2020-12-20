#* Info
# Copyright (C) 2020 Oleh Krehel
# Author: Oleh Krehel <ohwoeowho@gmail.com>
# URL: https://github.com/abo-abo/xkb-indicator
# Version: 0.1.0
# Keywords: xkb

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# For a full copy of the GNU General Public License
# see <http://www.gnu.org/licenses/>.

#* Imports
import sys
import re
import signal
import gi
gi.require_version ("Gtk", "3.0")
gi.require_version ("AppIndicator3", "0.1")
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import GObject
import pycook.insta as st

#* Functions
def current_layout():
    r = st.scb("setxkbmap -query")
    return re.search("layout: *(.*)", r).group(1)

def label(toggle=False):
    cur_layout = current_layout()
    if toggle:
        return "ua" if cur_layout == "xx" else "en"
    else:
        return ("en" if cur_layout == "xx" else "ua") + " ⏷"

#* Class
class XkbIndicator:
    def __init__(self):
        self.app = "xkb-indicator"
        self.indicator = appindicator.Indicator.new(
            self.app,
            "input-keyboard-symbolic",
            category=appindicator.IndicatorCategory.OTHER)
        self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.build_menu())
        self.indicator.set_label(label(), self.app)

    def build_menu(self):
        menu = gtk.Menu()
        item_quit = gtk.MenuItem("quit")
        item_quit.connect("activate", self.stop)

        self.item_toggle = gtk.MenuItem(label(True))
        self.item_toggle.connect("activate", self.toggle)

        menu.append(self.item_toggle)
        menu.append(item_quit)
        menu.show_all()
        return menu

    def toggle(self, source):
        cur_layout = current_layout()
        if cur_layout == "xx":
            next_layout = "ua"
        else:
            next_layout = "xx"
        st.scb(f"setxkbmap {next_layout}")
        self.item_toggle.set_label(label(True))
        GObject.idle_add(
            self.indicator.set_label,
            label(),
            self.app,
            priority=GObject.PRIORITY_DEFAULT)

    def stop(self, source):
        st.scb("setxkbmap xx")
        gtk.main_quit()

def main(argv=None):
    argv = argv or sys.argv
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    XkbIndicator()
    GObject.threads_init()
    gtk.main()

#* Script
if __name__ == '__main__':
    main(sys.argv)
