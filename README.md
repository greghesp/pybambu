# Bambu Labs API Client

## About

This package subscribes to the MQTT Server on the Bambu Labs X1C 3D Printer.

> Note:  It is currently not up-to-date.  It's currently being worked on directly in a [HA Custom Component](https://github.com/greghesp/ha-bambulab/tree/main/custom_components/bambu_lab/pybambu), until it is more stable

## Installation

`pip install pybambu`


## Available Methods

### Connect to the printer
```py
connect()
```

### Listen for events from the printer
```py
subscribe(callback=method)
```

### Disconnect from the printer
```py
disconnect()
```
