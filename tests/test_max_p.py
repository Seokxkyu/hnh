from hnh.utils import get_max_label, get_max_score2, get_max_score3

def test_max_p_label():
    p = [
        {'label': 'hot dog', 'score': 0.5},
        {'label': 'not hot dog', 'score': 0.4}
    ]

    assert get_max_label(p) == "hot dog"
    assert get_max_score2(p) == "hot dog"
    assert get_max_score3(p) == "hot dog"
