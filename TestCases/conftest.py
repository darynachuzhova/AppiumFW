import json
import os
import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions
import subprocess
import time

def load_config():
    """Load configuration from config.json"""
    config_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
    config_path = os.path.abspath(config_path)

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"config.json not found at: {config_path}")

    with open(config_path, "r") as f:
        return json.load(f)


def get_active_udid():
    """Return UDID of the currently booted iOS simulator"""
    try:
        result = subprocess.run(
            ["xcrun", "simctl", "list", "devices", "booted"],
            capture_output=True,
            text=True
        )
        lines = result.stdout.strip().split("\n")
        for line in lines:
            if "(" in line and ")" in line and "Booted" in line:
                return line.split("(")[1].split(")")[0]
    except Exception as e:
        print(f"Could not retrieve UDID: {e}")
    return None


@pytest.fixture(scope="class")
def test_setup(request):
    """Setup Appium driver before tests and quit after"""
    config = load_config()
    udid = get_active_udid()

    if not udid:
        raise RuntimeError("No active iOS simulator found. Please boot one before running tests.")

    print(f"Loaded configuration: {config}")
    print(f"Active UDID: {udid}")

    options = XCUITestOptions()
    options.platform_name = config["platformName"]
    options.platform_version = config["platformVersion"]
    options.device_name = config["deviceName"]
    options.udid = udid
    options.app = config["app"]
    options.automation_name = "XCUITest"

    time.sleep(2)  # optional wait for Appium server to be ready

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    request.cls.driver = driver
    yield
    driver.quit()
