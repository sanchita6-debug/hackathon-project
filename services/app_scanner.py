from app_monitor import search_apps
from app_similarity import calculate_similarity
from developer_checker import DeveloperChecker
from risk_engine import calculate_risk_score
from description_similarity import description_similarity
from keyword_detector import keyword_score


def scan_apps(
    brand_name,
    official_developer,
    official_description
):

    apps = search_apps(brand_name)

    results = []

    for app in apps:

        similarity = calculate_similarity(
            brand_name,
            app["app_name"]
        )

        developer = DeveloperChecker.developer_check(
            official_developer,
            app["developer"]
        )

        desc_score = description_similarity(
            official_description,
            app["description"]
        )

        kw = keyword_score(
            app["app_name"] +
            " " +
            app["description"]
        )

        risk = calculate_risk_score(
            name_similarity=similarity,
            developer_similarity=developer["similarity_score"],
            description_similarity=desc_score,
            keyword_score=kw["score"]
        )

        results.append({
            "app_name": app["app_name"],
            "developer": app["developer"],
            "name_similarity": similarity,
            "developer_status": developer["status"],
            "developer_similarity": developer["similarity_score"],
            "description_similarity": desc_score,
            "keywords_found": kw["keywords"],
            "risk_score": risk["risk_score"],
            "risk_level": risk["risk_level"]
        })

    return results


if __name__ == "__main__":

    results = scan_apps(
        brand_name="Paytm",
        official_developer="One97 Communications Ltd.",
        official_description="Secure UPI payments, money transfer, recharge and bill payments."
    )

    for app in results:
        print(app)