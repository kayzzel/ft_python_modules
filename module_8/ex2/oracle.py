import os
from dotenv import load_dotenv
from urllib.parse import urlparse

# Detect and load .env if it exists
env_exists: bool = os.path.exists(".env")
if env_exists:
    load_dotenv()

# Required configuration keys
REQUIRED_KEYS: list[str] = [
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT"
]

# Valid values for some keys
VALID_MATRIX_MODES: list[str] = ["development", "production"]
VALID_LOG_LEVELS: list[str] = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


def get_config(var_name: str, required=False) -> str | None:
    """Retrieve a configuration variable and optionally warn if missing"""
    value: str | None = os.getenv(var_name)
    if required and not value:
        source: str = ".env file" if env_exists else "Environment variable"
        print(f"[WARN] {var_name} not found in {source}!")
    return value


def validate_config(config: dict[str, str | None]) -> bool:
    """Validate formats of the configuration variables"""
    valid: bool = True

    # Check if the .env exist
    if not env_exists:
        return False

    # MATRIX_MODE
    mode: str | None = config.get("MATRIX_MODE", "")
    if mode and mode.lower() not in VALID_MATRIX_MODES:
        print("[WARN] MATRIX_MODE should be 'development' or "
              f"'production', got '{config.get('MATRIX_MODE')}'")
        valid = False

    # DATABASE_URL (very basic validation)
    db_url: str | None = config.get("DATABASE_URL", "")
    if not db_url or "://" not in db_url:
        print(f"[WARN] DATABASE_URL seems invalid: '{db_url}'")
        valid = False

    # API_KEY (just check it’s non-empty and not placeholder)
    api_key: str | None = config.get("API_KEY", "")
    if not api_key or api_key.upper() in ["YOUR_API_KEY", "SECRET"]:
        print("[WARN] API_KEY is missing or looks like a placeholder")
        valid = False

    # LOG_LEVEL
    log_level: str | None = config.get("LOG_LEVEL", "")
    if log_level and log_level.upper() not in VALID_LOG_LEVELS:
        print(f"[WARN] LOG_LEVEL should be one of {VALID_LOG_LEVELS}, "
              f"got '{config.get('LOG_LEVEL')}'")
        valid = False

    # ZION_ENDPOINT (simple URL check)
    endpoint: str | None = config.get("ZION_ENDPOINT", "")
    parsed = urlparse(endpoint)
    if not endpoint or not parsed.scheme or not parsed.netloc:
        print(f"[WARN] ZION_ENDPOINT should be a valid URL, got '{endpoint}'")
        valid = False

    return valid


def check_env_file() -> bool:
    """Check if .env exists and all required keys are present"""
    print("\nEnvironment security check:")

    if not env_exists:
        print("[WARN] .env file is missing! "
              "Some configuration may not be loaded.")
        return False

    # Read .env manually
    env_content: dict[str, str] = {}

    try:
        with open(".env", "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    env_content[key.strip()] = val.strip()
    except Exception as err:
        print(f"Error {err.__class__.__name__}: {err}")

    missing_keys = [
        k for k in REQUIRED_KEYS
        if k not in env_content or not env_content[k]
    ]

    if missing_keys:
        print(f"[WARN] .env file is not properly configured. "
              f"Missing keys: {', '.join(missing_keys)}")
        return False

    print("[OK] .env file properly configured")

    return True


def check_security() -> None:
    """Basic checks for hardcoded secrets"""
    api_key: str = os.getenv("API_KEY", "")
    hardcoded_keys: list[str] = ["YOUR_API_KEY", "SECRET"]
    if any(hk in api_key.upper() for hk in hardcoded_keys):
        print("[WARN] Possible hardcoded secrets detected")
    else:
        print("[OK] No hardcoded secrets detected")

    if os.getenv("MATRIX_MODE") == "production":
        print("[OK] Production overrides available")
    else:
        print("[INFO] Running in development mode")


def main():
    print("Accessing the Mainframe")
    print("ORACLE STATUS: Reading the Matrix...")

    # Load configuration
    config: dict[str, str | None] = {}
    for key in REQUIRED_KEYS:
        config[key] = get_config(key, required=True)

    print("\nConfiguration loaded:")
    print(f"Mode: {config['MATRIX_MODE'] or 'Not found'}")
    print(f"Database: {config['DATABASE_URL'] or 'Not found'}")
    print(f"API Access: "
          f"{'Authenticated' if config['API_KEY'] else 'Not Authenticated'}")
    print(f"Log Level: {config['LOG_LEVEL'] or 'Not found'}")
    print(f"Zion Network: Online at {config['ZION_ENDPOINT'] or 'Not found'}")

    # Run security and .env checks
    check_security()
    check_env_file()

    # Validate formats
    print("\nConfiguration format check:")
    if validate_config(config):
        print("[OK] All configuration values have valid formats")
    else:
        print("[WARN] Some configuration values may be invalid")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
