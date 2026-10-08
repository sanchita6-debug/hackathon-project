from rapidfuzz import fuzz


def description_similarity(
    official_description,
    candidate_description
):

    score = fuzz.token_set_ratio(
        official_description.lower(),
        candidate_description.lower()
    )

    return round(score, 2)