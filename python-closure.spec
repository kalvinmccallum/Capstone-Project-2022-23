# Created by pyp2rpm-3.3.9
%global pypi_name closure
%global pypi_version 20191111

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Closure compiler packaged for Python

License:        BSD
URL:            http://pypi.python.org/pypi/closure
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
The Closure Compiler < is a tool for reducing the size of Javascript files to
make them download and run faster.It's a Java-based tool. This package, in the
spirit of the yuicompressor < package, provides a simple way to install and use
the the Closure compiler from Python, bundling the closure.jar with the Python
package.I recommend looking at webassets_ for your CSS/JS compression
needs......

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
The Closure Compiler < is a tool for reducing the size of Javascript files to
make them download and run faster.It's a Java-based tool. This package, in the
spirit of the yuicompressor < package, provides a simple way to install and use
the the Closure compiler from Python, bundling the closure.jar with the Python
package.I recommend looking at webassets_ for your CSS/JS compression
needs......


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{_bindir}/closure
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Mon Apr 17 2023 Soumil Kadam - 20191111-1
- Initial package.
