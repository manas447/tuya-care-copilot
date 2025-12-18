def analyze_issue(logs):
    if logs["wifi_signal"] == "weak":
        return {
            "issue": "Weak WiFi signal causing disconnection",
            "solution": [
                "Move device closer to router",
                "Restart the smart bulb",
                "Check 2.4GHz WiFi compatibility",
                "Update firmware from Tuya app"
            ]
        }

    return {
        "issue": "Unknown issue",
        "solution": ["Contact support"]
    }
