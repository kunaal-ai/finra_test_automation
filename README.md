# finra_test_automation
Python, Playwright, Jenkins, github hooks, HTML report, parallel test execution

# How to run test
- ```pytest``` - runs the tests and report will be saved in results dir.
- ```pytest --headed``` - runs tests in headed mode.

### Parallel Test
- To run test parallel run ```pytest -n x``` x is the number of workers.(e.g 4) or use 
- ```pytest -n auto``` , which will use all possible workers automatically.

# Plugins used
- [reporter-html1-0.8.3](https://pypi.org/project/pytest-reporter-html1/) - Generate reports in html format 
- [base-url-2.0.0](https://pypi.org/project/pytest-base-url/) - provides an optional base URL via the command line or configuration file.
- [dotenv-0.5.2](https://pypi.org/project/python-dotenv/) - reads key-value pairs from a .env file and can set them as environment variables.
- [xdist-3.3.1](https://pypi.org/project/pytest-xdist/) - distributing tests across multiple CPUs to speed up test execution:
- [playwright-0.3.3](https://playwright.dev/python/)

### Other tools and version
- python 3.10.9
- pytest 7.4.2


# Test generator
```playwright codegen```

# Test Coverage
```python3 -m pip install coverage```

## Run
```coverage run -m pytest```
More information([https://coverage.readthedocs.io/en/7.4.4/])
HTML Report
```coverage html```

### CI/CD
- Jenkins build gets triggered using webhook and proxy server via ngrok
- cron job schedule is set to 60 minutes.