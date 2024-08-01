import yaml
import logging

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

_LOGGER = logging.getLogger(__name__)
DOMAIN = "aqua_flower"

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    # Setup the integration from configuration.yaml if applicable
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    # Store the configuration entry data
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data

    # Log a message to inform the user about the next steps
    _LOGGER.info("Aqua Flower integration setup complete. Please refer to the documentation for adding the Lovelace dashboard configuration.")
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    # Unload the configuration entry and clean up
    hass.data[DOMAIN].pop(entry.entry_id)
    return True
