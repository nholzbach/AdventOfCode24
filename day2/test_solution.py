import pytest
from solution import check_row_safety


# Test cases for check_row_safety
@pytest.mark.parametrize(
    "report, expected",
    [
        # Case 1: All differences positive and > 1
        ([1, 3, 5, 7], True),

        # Case 2: All differences negative and < -1
        ([8, 5, 3, 2, 1], True),

        # Case 3: Differences alternate signs
        ([1, 3, 2, 4], False),

        # Case 4: Differences all positive but not all <3
        ([1, 5, 8, 12], False),

        # Case 5: Differences all < 4 in magnitude and alternate signs
        ([1, 3, 1, 3], False),

        # Case 6: one of the numbers is the same (difference=0)
        ([1, 2, 2, 4, 5], False),

    ],
)
def test_check_row_safety(report, expected):
    result = check_row_safety(report)
    assert result == expected, f"Failed for input: {report}"
