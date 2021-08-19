%global pypi_name PyJWT
%global pkg_name pyjwt

# pytest < 5 needed
%bcond_with test

Name:           python-%{pkg_name}
Version:        2.0.1
Release:        %mkrel 2
Summary:        JSON Web Token implementation in Python
Group:          Development/Python
License:        MIT
URL:            https://pypi.org/project/PyJWT
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
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

%description
A Python implementation of RFC 7519.

%package -n     python3-%{pkg_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pkg_name}}
Requires:       python3dist(cryptography) >= 1.4

%description -n python3-%{pkg_name}
A Python implementation of RFC 7519.

%prep
%autosetup -n PyJWT-%{version}

# Remove bundled egg-info
rm -rf *.egg-info

%build
%py3_build

%install
%py3_install

%if %{with test}
%check
%{__python3} setup.py test
%endif

%files -n python3-%{pkg_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/jwt
%{python3_sitelib}/PyJWT-%{version}-py?.?.egg-info
