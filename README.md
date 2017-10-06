# nexpose-client-python
[![Travis](https://img.shields.io/travis/rapid7/nexpose-client-python.svg)](https://travis-ci.org/rapid7/nexpose-client-python) [![PyPI Version](https://img.shields.io/pypi/v/nexpose.svg)](https://pypi.python.org/pypi/nexpose) ![PyPI Status](https://img.shields.io/pypi/status/nexpose.svg) [![GitHub license](https://img.shields.io/badge/license-BSD-blue.svg)](https://raw.githubusercontent.com/rapid7/nexpose-client-python/master/LICENSE) ![PyPI Pythons](https://img.shields.io/pypi/pyversions/nexpose.svg)

This is the official Python package for the Python Nexpose API client library.

For assistance with using the library or to discuss different approaches, please open an issue. To share or discuss scripts which use the library head over to the [Nexpose Resources](https://github.com/rapid7/nexpose-resources) project.

Check out the [wiki](https://github.com/rapid7/nexpose-client-python/wiki) for walk-throughs and other documentation. Submit bugs and feature requests on the [issues](https://github.com/rapid7/nexpose-client-python/issues) page.

This library provides calls to the Nexpose XML APIs version 1.1 and 1.2.

nexpose-client-python uses [Semantic Versioning](http://semver.org/). This allows for confident use of [version pinning](https://www.python.org/dev/peps/pep-0440/#version-specifiers) in your requirements file.

## Testing
Make sure tests requirements are installed with `pip install -r requirements_tests.txt`

```
$ py.test
============================================================= test session starts =============================================================
platform linux2 -- Python 2.7.10, pytest-3.2.2, py-1.4.34, pluggy-0.4.0
collected 27 items

tests/test_LoadFixture.py ...
tests/test_NexposeNode.py .
tests/test_NexposeReportConfigurationSummary.py ..
tests/test_NexposeSession.py ...........
tests/test_NexposeTag.py .....
tests/test_NexposeUserAuthenticatorSummary.py .
tests/test_NexposeVulnerability.py ....

```

## Release Notes

Release notes are available on the [Releases](https://github.com/rapid7/nexpose-client-python/releases) page.

## Contributions

We welcome contributions to this package. Please see [CONTRIBUTING](.github/CONTRIBUTING.md) for details.

Full usage examples or task-oriented scripts should be submitted to the [Nexpose Resources](https://github.com/rapid7/nexpose-resources) project. Smaller examples can be added to the [wiki](https://github.com/rapid7/nexpose-client-python/wiki).

## License

The nexpose-client-python library is provided under the 3-Clause BSD License. See [LICENSE](./LICENSE) for details.

## Credits
Davinsi Labs
Rapid7, Inc.

See [contributors](./contributors.md) for more info.
