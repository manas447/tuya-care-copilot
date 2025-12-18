def get_device_logs(device_id: str):
    return {
        "device_id": device_id,
        "device_type": "Smart Bulb",
        "status": "offline",
        "wifi_signal": "weak",
        "last_error": "CONNECTION_TIMEOUT",
        "firmware_version": "1.0.2"
    }
