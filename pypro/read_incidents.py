import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "incidents.json")


def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []


def list_incidents(status=None, severity=None):
    data = load_data()
    if status:
        data = [d for d in data if d.get("status") == status]
    if severity:
        data = [d for d in data if d.get("severity") == severity]
    return data


def get_incident_by_id(incident_id):
    data = load_data()
    for it in data:
        if it.get("id") == incident_id:
            return it
    return None
