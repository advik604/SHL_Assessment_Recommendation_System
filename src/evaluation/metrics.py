def extract_slug(url):
    """
    Extract the final slug from SHL URL
    """
    return url.strip().lower().rstrip("/").split("/")[-1]


def recall_at_k(preds, truth):
    """
    preds: list of predicted URLs
    truth: list of ground truth URLs
    """

    pred_slugs = set(extract_slug(p) for p in preds)
    truth_slugs = set(extract_slug(t) for t in truth)

    hits = pred_slugs.intersection(truth_slugs)

    return len(hits) / len(truth_slugs) if truth_slugs else 0.0


def mean_recall(scores):
    return sum(scores) / len(scores) if scores else 0.0