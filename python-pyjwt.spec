%global pypi_name PyJWT
%global pkg_name pyjwt

# pytest < 5 needed
%bcond_with test

Name:           python-%{pkg_name}
Version:        2.10.1
Release:        1
Summary:        JSON Web Token implementation in Python
Group:          Development/Python
License:        MIT
URL:            https://pypi.org/project/PyJWT
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pkg_name}-%{version}.tar.gz

BuildSystem:    python
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(cryptography)
%if %{with test}
BuildRequires:  python3dist(flake8)
BuildRequires:  python3dist(flake8-import-order)
BuildRequires:  python3dist(pep8-naming)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-runner)
%endif

%{?python_provide:%python_provide python3-%{pkg_name}}
Requires:       python3dist(cryptography) >= 1.4

%description
A Python implementation of RFC 7519.

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/jwt
%{python_sitelib}/PyJWT-%{version}.dist-info
