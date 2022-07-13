# Python Testing

## pytest-bdd 
* [Python Testing 101: pytest-bdd][]
* [BDD library for the pytest runner][]

## Hooks
[pytest-bdd hooks][]

Add to `conftest.py`
```python
def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f"<<< {step}")
```

## Monkey patching
In `decoder_witH_patching.feature`, there are new scenarios.

We'd like to re-use `decoder_turned_on` so it should be moved to `conftest.py`.

[How to monkeypatch/mock modules and environments][]


## [pytest fixture scope][]
Make Decoder initialization longer, due to `sleep(1)`.

## [manage logging][]
Intercept logging from `channel_up`



[Python Testing 101: pytest-bdd]: https://automationpanda.com/2018/10/22/python-testing-101-pytest-bdd/
[BDD library for the pytest runner]: https://pypi.org/project/pytest-bdd/
[pytest-bdd hooks]: https://pypi.org/project/pytest-bdd/#hooks
[How to monkeypatch/mock modules and environments]: https://docs.pytest.org/en/7.1.x/how-to/monkeypatch.html
[pytest fixture scope]: https://docs.pytest.org/en/7.1.x/reference/reference.html#pytest-fixture
[manage logging]: https://docs.pytest.org/en/7.1.x/how-to/logging.html#how-to-manage-logging