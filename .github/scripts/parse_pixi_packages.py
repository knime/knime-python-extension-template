import json
import sys
from pathlib import Path


def main() -> int:
    pixi_json_path = Path("pixi-packages.json")

    if not pixi_json_path.exists():
        print("Could not analyze pixi packages: pixi-packages.json not found")
        return 0

    try:
        with pixi_json_path.open("r", encoding="utf-8") as f:
            data = json.load(f)

        total_packages = 0
        environments = []

        if isinstance(data, dict):
            for environment_name, environment_data in data.items():
                environments.append(environment_name)
                if (
                    isinstance(environment_data, dict)
                    and "packages" in environment_data
                ):
                    total_packages += len(environment_data["packages"])

        print(f"- **Total packages:** {total_packages}")
        print(f"- **Environments:** {environments}")

    except Exception as error:  # noqa: BLE001
        # Print a friendly message and exit successfully so the caller can choose how
        # to handle it
        print(f"Error analyzing packages: {error}")
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
