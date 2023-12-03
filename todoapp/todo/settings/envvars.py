from todoapp.general.utils.collections import deep_update
from todoapp.general.utils.settings import get_settings_from_env

# globals() is a dictionary of global variables
deep_update(globals(), get_settings_from_env(ENVVAR_SETTINGS_PREFIX))