import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "incidents.json")


def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def update_status(incident_id, new_status):
    allowed = ["Open", "Investigating", "Mitigated", "Resolved"]
    if new_status not in allowed:
        return False, f"Status must be one of: {', '.join(allowed)}"
    data = load_data()
    for it in data:
        if it.get("id") == incident_id:
            it["status"] = new_status
            save_data(data)
            return True, "Updated"
    return False, "Not found"


def update_description(incident_id, new_description):
    data = load_data()
    for it in data:
        if it.get("id") == incident_id:
            it["description"] = new_description
            save_data(data)
            return True
    return False


def update_severity(incident_id, new_severity):
    allowed = ["SEV1", "SEV2", "SEV3"]
    if new_severity not in allowed:
        return False
    data = load_data()
    for it in data:
        if it.get("id") == incident_id:
            it["severity"] = new_severity
            save_data(data)
            return True
    return False
