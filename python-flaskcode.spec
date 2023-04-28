Name:           python-flaskcode
Version:        0.0.8
Release:        1%{?dist}
Summary:        Web based code editor on python flask framework

License:        MIT
URL:            https://github.com/sujeetkv/flaskcode
Source:         %{pypi_source flaskcode}

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
A web based code editor which uses the python flask framework.}


%description %_description

%package -n     python3-flaskcode
Summary:        %{summary}

%description -n python3-flaskcode %_description


%prep
%autosetup -p1 -n flaskcode-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python3-flaskcode -f %{pyproject_files}


%changelog
* Fri Mar 24 2023 Jasmin Marwad - 0.0.8-1
- Initial package
