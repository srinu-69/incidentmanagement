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


def delete_incident(incident_id):
    data = load_data()
    for i, it in enumerate(data):
        if it.get("id") == incident_id:
            if it.get("status") != "Resolved":
                return False, "Can only delete incidents with status 'Resolved'"
            data.pop(i)
            save_data(data)
            return True, "Deleted"
    return False, "Not found"
