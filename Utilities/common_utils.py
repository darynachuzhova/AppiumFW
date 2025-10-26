import os
import json
import subprocess
import re
from pprint import pprint


def load_config():
    """Load configuration from config.json located one level above this file."""
    config_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
    config_path = os.path.abspath(config_path)

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"config.json not found at {config_path}")

    with open(config_path, "r") as file:
        return json.load(file)


def save_config(config):
    """Save updated configuration back to config.json."""
    config_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
    config_path = os.path.abspath(config_path)

    with open(config_path, "w") as file:
        json.dump(config, file, indent=2)
    print(f"💾 Updated config.json saved at {config_path}")


def get_active_udid():
    """Return the UDID of the currently booted iOS simulator."""
    print("🔧 Running get_active_udid() in:", os.getcwd())
    print("🔧 PATH =", os.environ.get("PATH"))

    try:
        output = subprocess.check_output(
            ["xcrun", "simctl", "list", "devices", "booted"],
            stderr=subprocess.STDOUT,
            text=True
        )
        print("📋 Raw output from xcrun:")
        print(output)

        for raw_line in output.splitlines():
            line = raw_line.strip()
            if "(Booted)" in line:
                match = re.search(r"\(([\w-]+)\)", line)
                if match:
                    udid = match.group(1)
                    print(f"✅ Active UDID found: {udid}")
                    return udid

        print("⚠️ No booted simulator found.")
        return None

    except subprocess.CalledProcessError as e:
        print(f"❌ Error running xcrun:\n{e.output}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None


if __name__ == "__main__":
    config = load_config()
    udid = get_active_udid()

    print("\nLoaded configuration:")
    pprint(config)

    if udid:
        config["udid"] = udid
        save_config(config)

    print(f"\nActive UDID: {udid}")
