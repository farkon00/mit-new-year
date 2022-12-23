import sys
import io

import pytest


from main import update_license

from dataclasses import dataclass

@dataclass
class Test:
    __test__ = False

    license_text: str
    repo_name: str
    expected_stdout: str
    expected_result: str
    target: int 

TEST_SUFFIX = \
"""
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

TESTS = [
    Test(
        f"MIT License\n\nCopyright (c) 2022 farkon00\n{TEST_SUFFIX}",
        "farkon00/cont",
        "",
        f"MIT License\n\nCopyright (c) 2022-2023 farkon00\n{TEST_SUFFIX}",
        2023
    ),
    Test(
        f"MIT License\n\nCopyright (c) 2021-2022 farkon00\n{TEST_SUFFIX}",
        "farkon00/binarian",
        "",
        f"MIT License\n\nCopyright (c) 2021-2024 farkon00\n{TEST_SUFFIX}",
        2024
    ),
    Test(
        f"MIT License\n\nCopyright (c) 1212-32340 user\n{TEST_SUFFIX}",
        "user/repo",
        "Year is already \"32340\" in user/repo\n",
        None,
        20254
    ),
    Test(
        f"MIT License\n\nCopyright (c) 1212-NaN user\n{TEST_SUFFIX}",
        "error/invalid",
        "Invalid year format \"1212-NaN\" in error/invalid\n",
        None,
        12345432
    )
]

@pytest.mark.parametrize("self", TESTS)
def test_update(self: Test):
    sys.stdout = io.StringIO()
    
    result = update_license(self.license_text, self.repo_name, target=self.target)

    assert result == self.expected_result
    assert sys.stdout.getvalue() == self.expected_stdout