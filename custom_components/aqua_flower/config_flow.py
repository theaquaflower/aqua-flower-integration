from homeassistant import config_entries
from homeassistant.core import callback
import voluptuous as vol
from .const import DOMAIN  # Import the domain constant from const.py

class AquaFlowerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Aqua Flower."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_PUSH

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return AquaFlowerOptionsFlowHandler(config_entry)

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="Aqua Flower", data=user_input)

        # Define the configuration schema
        schema = vol.Schema({
            # Add any configuration fields you require here
            # Example: vol.Required("api_key"): str
        })

        return self.async_show_form(step_id="user", data_schema=schema)

class AquaFlowerOptionsFlowHandler(config_entries.OptionsFlow):
    """Handle options flow for Aqua Flower."""

    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        # Define the options schema
        schema = vol.Schema({
            # Add any options fields you require here
            # Example: vol.Optional("update_interval", default=60): int
        })

        return self.async_show_form(step_id="init", data_schema=schema)
