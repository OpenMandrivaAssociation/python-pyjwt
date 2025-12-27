%global pypi_name PyJWT
%global module pyjwt

# pytest < 5 needed
%bcond test 0

Name:           python-%{module}
Version:        2.10.1
Release:        2
Summary:        JSON Web Token implementation in Python
Group:          Development/Python
License:        MIT
URL:            https://pypi.org/project/PyJWT
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{module}-%{version}.tar.gz
BuildSystem:    python
BuildArch:      noarch

BuildRequires:  pkgconfig(python)
BuildRequires:  python%{pyver}dist(cryptography)
BuildRequires:  python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(wheel)
%if %{with test}
BuildRequires:  python%{pyver}dist(flake8)
BuildRequires:  python%{pyver}dist(flake8-import-order)
BuildRequires:  python%{pyver}dist(pep8-naming)
BuildRequires:  python%{pyver}dist(pytest)
BuildRequires:  python%{pyver}dist(pytest-cov)
BuildRequires:  python%{pyver}dist(pytest-runner)
%endif

%{?python_provide:%python_provide python3-%{module}}
Requires:       python%{pyver}dist(cryptography) >= 1.4

%description
A Python implementation of RFC 7519.

%prep
%autosetup -n %{module}-%{version} -p1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info/

%files
%license LICENSE
%doc README.rst
%{python_sitelib}/jwt
%{python_sitelib}/%{module}-%{version}.dist-info
