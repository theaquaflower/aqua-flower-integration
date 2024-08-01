import yaml
import logging

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers import entity_registry as er

_LOGGER = logging.getLogger(__name__)
DOMAIN = "aqua_flower"

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data

    # Create input booleans and toggle helpers
    await create_helpers(hass, entry)

    _LOGGER.info("Aqua Flower integration setup complete. Please refer to the documentation for adding the Lovelace dashboard configuration.")
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    hass.data[DOMAIN].pop(entry.entry_id)
    return True

async def create_helpers(hass: HomeAssistant, entry: ConfigEntry):
    # Define the helpers to be created
    helpers = [
        {"platform": "input_boolean", "name": "Zone 1 Schedule Toggle", "entity_id": "input_boolean.zone_1_schedule_toggle"},
        {"platform": "input_boolean", "name": "Zone 2 Schedule Toggle", "entity_id": "input_boolean.zone_2_schedule_toggle"},
        {"platform": "input_boolean", "name": "Show Schedule Settings", "entity_id": "input_boolean.show_schedule_settings"},
        {"platform": "input_number", "name": "Zone 1 Timer", "entity_id": "input_number.zone_1_timer", "min": 0, "max": 60, "step": 1},
        {"platform": "input_number", "name": "Zone 2 Timer", "entity_id": "input_number.zone_2_timer", "min": 0, "max": 60, "step": 1},
        # Add more helpers as needed
    ]

    for helper in helpers:
        platform = helper["platform"]
        name = helper["name"]
        entity_id = helper["entity_id"]

        # Check if the entity already exists
        entity_registry = er.async_get(hass)
        if entity_registry.async_get(entity_id):
            _LOGGER.info(f"Helper {entity_id} already exists")
            continue

        # Create the helper
        if platform == "input_boolean":
            await hass.services.async_call(
                "input_boolean",
                "create",
                {
                    "name": name,
                    "initial": False,
                    "entity_id": entity_id,
                },
                blocking=True,
            )
        elif platform == "input_number":
            await hass.services.async_call(
                "input_number",
                "create",
                {
                    "name": name,
                    "min": helper["min"],
                    "max": helper["max"],
                    "step": helper["step"],
                    "unit_of_measurement": "min",
                    "entity_id": entity_id,
                },
                blocking=True,
            )
        # Add more platforms as needed

        _LOGGER.info(f"Created helper {entity_id}")
