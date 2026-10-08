import json
from google_play_scraper import search


def search_apps(brand_name):
    results = search(
        brand_name,
        lang="en",
        country="us",
        n_hits=10
    )

    app_list = []

    for app in results:
        app_info = {
            "app_name": app.get("title", "N/A"),
            "developer": app.get("developer", "N/A"),
            "description": app.get("description", "N/A")
        }

        app_list.append(app_info)

    return app_list


if __name__ == "__main__":
    brand = "Nike"

    apps = search_apps(brand)

    print(json.dumps(apps, indent=4))