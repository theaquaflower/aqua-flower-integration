# Aqua Flower Integration

Welcome to the Aqua Flower custom Home Assistant integration! This integration provides comprehensive control over your Aqua Flower irrigation system directly from Home Assistant.

## Features
- Control and monitor multiple zones
- Schedule watering times and durations
- View real-time and historical watering data

## Installation

### Step 1: Add the Custom Integration
1. Ensure you have [HACS](https://hacs.xyz/) installed in your Home Assistant.
2. Go to HACS > Integrations > Explore & Add Repositories.
3. Search for "Aqua Flower" and install it.

### Step 2: Configure the Integration
1. Go to Configuration > Integrations.
2. Click on "Add Integration" and search for "Aqua Flower".
3. Follow the on-screen instructions to complete the setup.

### Step 3: Add the Lovelace Card
Once the integration is set up, add the following configuration to your Lovelace dashboard to use the Aqua Flower card:

```yaml
type: custom:layout-card
layout_type: custom:grid-layout
cards:
  - type: vertical-stack
    cards:
      - type: entities
        title: Aqua Flower
        entities:
          - entity: select.select_zone
            name: Select Zone
          - entity: switch.show_schedule_settings
            name: Show Zone Settings
        card_mod:
          style: |
            ha-card {
              background: transparent;
              border-style: none;
              text-align: center;
            }
      - type: conditional
        conditions:
          - entity: switch.show_schedule_settings
            state: 'on'
          - entity: select.select_zone
            state: All Zones
        card:
          type: entities
          title: All Zones Settings
          entities:
            - entity: switch.all_zones_schedule_toggle
              name: All Zones
            - entity: number.all_zones_schedule_on_time
              name: All Zones Start Time
            - entity: select.all_zones_days
              name: All Zones Days
            - entity: number.all_zones_duration
              name: All Zones Duration (min)
          card_mod:
            style: |
              ha-card {
                background: transparent;
                border-style: none;
                text-align: center;
              }
      - type: conditional
        conditions:
          - entity: switch.show_schedule_settings
            state: 'on'
          - entity: select.select_zone
            state: Zone 1
        card:
          type: entities
          title: Zone 1 Settings
          entities:
            - entity: switch.zone_1_schedule_toggle
              name: Zone 1
            - entity: number.zone_1_schedule_on_time
              name: Zone 1 Start Time
            - entity: select.zone_1_days
              name: Zone 1 Days
            - entity: number.zone_1_duration
              name: Zone 1 Duration (min)
          card_mod:
            style: |
              ha-card {
                background: transparent;
                border-style: none;
                text-align: center;
              }
      - type: conditional
        conditions:
          - entity: switch.show_schedule_settings
            state: 'on'
          - entity: select.select_zone
            state: Zone 2
        card:
          type: entities
          title: Zone 2 Settings
          entities:
            - entity: switch.zone_2_schedule_toggle
              name: Zone 2
            - entity: number.zone_2_schedule_on_time
              name: Zone 2 Start Time
            - entity: select.zone_2_days
              name: Zone 2 Days
            - entity: number.zone_2_duration
              name: Zone 2 Duration (min)
          card_mod:
            style: |
              ha-card {
                background: transparent;
                border-style: none;
                text-align: center;
              }
      - type: conditional
        conditions:
          - entity: switch.show_schedule_settings
            state: 'on'
          - entity: select.select_zone
            state: Zone 3
        card:
          type: entities
          title: Zone 3 Settings
          entities:
            - entity: switch.zone_3_schedule_toggle
              name: Zone 3
            - entity: number.zone_3_schedule_on_time
              name: Zone 3 Start Time
            - entity: select.zone_3_days
              name: Zone 3 Days
            - entity: number.zone_3_duration
              name: Zone 3 Duration (min)
          card_mod:
            style: |
              ha-card {
                background: transparent;
                border-style: none;
                text-align: center;
              }
      - type: conditional
        conditions:
          - entity: switch.show_schedule_settings
            state: 'on'
          - entity: select.select_zone
            state: Zone 4
        card:
          type: entities
          title: Zone 4 Settings
          entities:
            - entity: switch.zone_4_schedule_toggle
              name: Zone 4
            - entity: number.zone_4_schedule_on_time
              name: Zone 4 Start Time
            - entity: select.zone_4_days
              name: Zone 4 Days
            - entity: number.zone_4_duration
              name: Zone 4 Duration (min)
          card_mod:
            style: |
              ha-card {
                background: transparent;
                border-style: none;
                text-align: center;
              }
      - type: conditional
        conditions:
          - entity: switch.show_schedule_settings
            state: 'on'
          - entity: select.select_zone
            state: Zone 5
        card:
          type: entities
          title: Zone 5 Settings
          entities:
            - entity: switch.zone_5_schedule_toggle
              name: Zone 5
            - entity: number.zone_5_schedule_on_time
              name: Zone 5 Start Time
            - entity: select.zone_5_days
              name: Zone 5 Days
            - entity: number.zone_5_duration
              name: Zone 5 Duration (min)
          card_mod:
            style: |
              ha-card {
                background: transparent;
                border-style: none;
                text-align: center;
              }
      - type: conditional
        conditions:
          - entity: switch.show_schedule_settings
            state: 'on'
          - entity: select.select_zone
            state: Zone 6
        card:
          type: entities
          title: Zone 6 Settings
          entities:
            - entity: switch.zone_6_schedule_toggle
              name: Zone 6
            - entity: number.zone_6_schedule_on_time
              name: Zone 6 Start Time
            - entity: select.zone_6_days
              name: Zone 6 Days
            - entity: number.zone_6_duration
              name: Zone 6 Duration (min)
          card_mod:
            style: |
              ha-card {
                background: transparent;
                border-style: none;
                text-align: center;
              }
  - type: custom:stack-in-card
    card_mod:
      style: |
        ha-card {
          background: transparent;
          border-style: none;
          text-align: center;
        }
    cards:
      - type: vertical-stack
        cards:
          - show_name: true
            show_icon: true
            icon_height: 40px
            type: button
            tap_action:
              action: toggle
            entity: switch.all_zones_switch
            show_state: false
            name: All Zones
            icon: mdi:pipe-valve
            card_mod:
              style: |
                ha-card {
                  background: transparent;
                  border-style: none;
                  text-align: center;
                }
          - type: custom:mushroom-number-card
            entity: number.all_zones_timer
            name: All Zones Timer
            icon: mdi:timer
            icon_color: white
            card_mod:
              style: |
                ha-card {
                  background: transparent;
                  border-style: none;
                  text-align: center;
                }
          - type: grid
            columns: 2
            square: false
            cards:
              - type: custom:stack-in-card
                card_mod:
                  style: |
                    ha-card {
                      background: transparent;
                      border-style: none;
                      text-align: center;
                    }
                cards:
                  - type: vertical-stack
                    cards:
                      - show_name: true
                        show_icon: true
                        icon_height: 40px
                        type: button
                        tap_action:
                          action: toggle
                        entity: switch.zone_1
                        show_state: false
                        name: Zone 1
                        icon: mdi:pipe-valve
                        card_mod:
                          style: |
                            ha-card {
                              background: transparent;
                              border-style: none;
                            }
                      - type: custom:mushroom-number-card
                        entity: number.zone_1_timer
                        icon: mdi:timer
                        icon_color: white
                      - type: entity
                        entity: sensor.zone_1_on_time
                        name: Zone 1 On Time Today
                        icon: mdi:timer-outline
                        card_mod:
                          style: |
                            ha-card {
                              background: transparent;
                              border-style: none;
                            }
              - type: custom:stack-in-card
                card_mod:
                  style: |
                    ha-card {
                      background: transparent;
                      border-style: none;
                      text-align: center;
                    }
                cards:
                  - type: vertical-stack
                    cards:
                      - show_name: true
                        show_icon: true
                        icon_height: 40px
                        type: button
                        tap_action:
                          action: toggle
                        entity: switch.zone_2
                        show_state: false
                        name: Zone 2
                        icon: mdi:pipe-valve
                        card_mod:
                          style: |
                            ha-card {
                              background: transparent;
                              border-style: none;
                            }
                      - type: custom:mushroom-number-card
                        entity: number.zone_2_timer
                        icon: mdi:timer
                        icon_color: white
                      - type: entity
                        entity: sensor.zone_2_on_time
                        name: Zone 2 On Time Today
                        icon: mdi:timer-outline
                        card_mod:
                          style: |
                            ha-card {
                              background: transparent;
                              border-style: none;
                            }
              - type: custom:stack-in-card
                card_mod:
                  style: |
                    ha-card {
                      background: transparent;
                      border-style: none;
                      text-align: center;
                    }
                cards:
                  - type: vertical-stack
                    cards:
                      - show_name: true
                        show_icon: true
                        icon_height: 40px
                        type: button
                        tap_action:
                          action: toggle
                        entity: switch.zone_3
                        show_state: false
                        name: Zone 3
                        icon: mdi:pipe-valve
                        card_mod:
                          style: |
                            ha-card {
                              background: transparent;
                              border-style: none;
                            }
                      - type: custom:mushroom-number-card
                        entity: number.zone_3_timer
                        icon: mdi:timer
                        icon_color: white
                      - type: entity
                        entity: sensor.zone_3_on_time
                        name: Zone 3 On Time Today
                        icon: mdi:timer-outline
                        card_mod:
                          style: |
                            ha-card {
                              background: transparent;
                              border-style: none;
                            }
              - type: custom:stack-in-card
                card_mod:
                  style: |
                    ha-card {
                      background: transparent;
                      border-style: none;
                      text-align: center;
                    }
                cards:
                  - type: vertical-stack
                    cards:
                      - show_name: true
                        show_icon: true
                        icon_height: 40px
                        type: button
                        tap_action:
                          action: toggle
                        entity: switch.zone_4
                        show_state: false
                        name: Zone 4
                        icon: mdi:pipe-valve
                        card_mod:
                          style: |
                            ha-card {
                              background: transparent;
                              border-style: none;
                            }
                      - type: custom:mushroom-number-card
                        entity: number.zone_4_timer
                        icon: mdi:timer
                        icon_color: white
                      - type: entity
                        entity: sensor.zone_4_on_time
                        name: Zone 4 On Time Today
                        icon: mdi:timer-outline
                        card_mod:
                          style: |
                            ha-card {
                              background: transparent;
                              border-style: none;
                            }
              - type: custom:stack-in-card
                card_mod:
                  style: |
                    ha-card {
                      background: transparent;
                      border-style: none;
                      text-align: center;
                    }
                cards:
                  - type: vertical-stack
                    cards:
                      - show_name: true
                        show_icon: true
                        icon_height: 40px
                        type: button
                        tap_action:
                          action: toggle
                        entity: switch.zone_5
                        show_state: false
                        name: Zone 5
                        icon: mdi:pipe-valve
                        card_mod:
                          style: |
                            ha-card {
                              background: transparent;
                              border-style: none;
                            }
                      - type: custom:mushroom-number-card
                        entity: number.zone_5_timer
                        icon: mdi:timer
                        icon_color: white
                      - type: entity
                        entity: sensor.zone_5_on_time
                        name: Zone 5 On Time Today
                        icon: mdi:timer-outline
                        card_mod:
                          style: |
                            ha-card {
                              background: transparent;
                              border-style: none;
                            }
              - type: custom:stack-in-card
                card_mod:
                  style: |
                    ha-card {
                      background: transparent;
                      border-style: none;
                      text-align: center;
                    }
                cards:
                  - type: vertical-stack
                    cards:
                      - show_name: true
                        show_icon: true
                        icon_height: 40px
                        type: button
                        tap_action:
                          action: toggle
                        entity: switch.zone_6
                        show_state: false
                        name: Zone 6
                        icon: mdi:pipe-valve
                        card_mod:
                          style: |
                            ha-card {
                              background: transparent;
                              border-style: none;
                            }
                      - type: custom:mushroom-number-card
                        entity: number.zone_6_timer
                        icon: mdi:timer
                        icon_color: white
                      - type: entity
                        entity: sensor.zone_6_on_time
                        name: Zone 6 On Time Today
                        icon: mdi:timer-outline
                        card_mod:
                          style: |
                            ha-card {
                              background: transparent;
                              border-style: none;
                            }
  - type: custom:mini-graph-card
    entities:
      - entity: sensor.zone_1_on_time
      - entity: sensor.zone_2_on_time
      - entity: sensor.zone_3_on_time
      - entity: sensor.zone_4_on_time
      - entity: sensor.zone_5_on_time
      - entity: sensor.zone_6_on_time
    card_mod:
      style: |
        ha-card {
        background: transparent;
        border-style: none;
        text-align: center;
        }
    hours_to_show: 168
    line_width: 5
    legend: true
    points_per_hour: 0.1
    decimals: 0
    lower_bound: 0
    labels_secondary: true
