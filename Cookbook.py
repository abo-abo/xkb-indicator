#* Imports
from pycook.recipes.pip import reinstall, publish, clean
import pycook.insta as st

#* Recipes
def setup_semimap(recipe):
    st.cp("data/xmodmap.xkb", "/usr/share/X11/xkb/symbols/xx")

def setup_desktop(recipe):
    if st.cp("data/xkbi.desktop", "~/.local/share/applications/xkbi.desktop"):
        st.bash("update-desktop-database ~/.local/share/applications/")
