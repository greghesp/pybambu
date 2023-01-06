# Bambu Labs API Client

## About

This package subscribes to the MQTT Server on the Bambu Labs X1C 3D Printer

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
