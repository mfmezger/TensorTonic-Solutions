def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    indicies = list(range(len(scores)))

    score_dict = dict(zip(indicies, scores))

    for idx in sorted(rated_indices, reverse=True):
        del score_dict[idx]

    sorted_indices = [k for k, v in sorted(score_dict.items(), key=lambda item: item[1], reverse=True)]

    return sorted_indices[:k]