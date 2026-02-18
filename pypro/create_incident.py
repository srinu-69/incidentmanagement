import json
import os
from datetime import datetime

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


def _generate_id(data):
    nums = []
    for it in data:
        iid = it.get("id", "")
        if iid.startswith("INC-"):
            try:
                nums.append(int(iid.split("-")[1]))
            except Exception:
                pass
    next_num = max(nums) + 1 if nums else 1
    return f"INC-{next_num:03d}"


def create_incident(service, severity, description):
    data = load_data()
    incident = {
        "id": _generate_id(data),
        "service": service,
        "severity": severity,
        "description": description,
        "status": "Open",
        "created_at": datetime.now().isoformat()
    }
    data.append(incident)
    save_data(data)
    return incident
