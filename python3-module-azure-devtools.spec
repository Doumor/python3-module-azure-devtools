%define pypi_name azure-devtools

Name:    python3-module-%pypi_name
Version: 1.2.0
Release: alt1

Summary: Development tools for Python-based Azure tools
License: MIT
Group:   Development/Python3
VCS:     https://github.com/Azure/azure-python-devtools

Packager: Danilkin Danila <danild@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.rst LICENSE
%python3_sitelibdir/azure_devtools/
%python3_sitelibdir/azure_devtools-%version.dist-info/


%changelog
* Wed Oct 24 2023 Danilkin Danila <danild@altlinux.org> 1.2.0-alt1
- Initial build for Sisyphus
