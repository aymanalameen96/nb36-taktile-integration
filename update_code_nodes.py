import os
import json
import requests

# Environment variables
API_KEY = os.environ["TAKTILE_API_KEY"]
BASE_URL = "https://eu-central-1.taktile-org.decide.taktile.com/run/api/v1/flows/patch-decision-graph/sandbox/decide"

HEADERS = {
    "X-Api-Key": API_KEY,
    "Content-Type": "application/json"
}

def update_code_node(flow_id, node_id, src_code):
    """Update a Taktile Code Node using the new payload structure."""
    payload = {
        "data": {
            "flow_id": flow_id,
            "node_id": node_id,
            "src_code": src_code
        },
        "metadata": {
            "version": "v1.0",
            "entity_id": "nb36-default"  # You could also pull this from config.json if needed
        },
        "control": {
            "execution_mode": "sync"
        }
    }

    response = requests.post(BASE_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        print(f"✅ Successfully updated node '{node_id}' in flow '{flow_id}'")
    else:
        print(f"❌ Failed to update node '{node_id}': {response.status_code} - {response.text}")
        response.raise_for_status()

def main():
    try:
        with open("config.json", "r") as config_file:
            config = json.load(config_file)
    except Exception as e:
        print(f"❌ Failed to load config.json: {e}")
        return

    for filename, node_info in config.items():
        flow_id = node_info.get("flow_id")
        node_id = node_info.get("node_id")  # updated key
        if not flow_id or not node_id:
            print(f"⚠️ Missing flow_id or node_id for '{filename}' in config.json")
            continue

        code_path = os.path.join("code", filename)
        if not os.path.isfile(code_path):
            print(f"⚠️ Code file '{filename}' not found.")
            continue

        try:
            with open(code_path, "r") as code_file:
                src_code = code_file.read()
        except Exception as e:
            print(f"❌ Could not read '{filename}': {e}")
            continue

        update_code_node(flow_id, node_id, src_code)

if __name__ == "__main__":
    main()
