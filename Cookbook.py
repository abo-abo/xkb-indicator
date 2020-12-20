#* Imports
from pycook.recipes.pip import reinstall, publish
import pycook.insta as st

#* Recipes
def setup_desktop(recipe):
    if st.cp("data/xkbi.desktop", "~/.local/share/applications/xkbi.desktop"):
        st.bash("update-desktop-database ~/.local/share/applications/")
