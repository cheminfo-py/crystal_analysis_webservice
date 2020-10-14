from crystal_analysis_webservice.core import run_analysis


def test_core():
    with open("HKUST-1.cif", "r") as fh:
        content = fh.read()

    out = run_analysis(content)
    assert out == "tbo"
