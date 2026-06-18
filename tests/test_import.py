"""Package import smoke tests."""


def test_package_import() -> None:
    import semantic_research_agent

    assert semantic_research_agent.__version__ == "0.1.0"
