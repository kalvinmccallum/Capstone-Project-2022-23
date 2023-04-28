Name:           python-photo-calendar
Version:        0.1.1
Release:        1%{?dist}
Summary:        Creates custom weekly/monthly/... photo calendars

License:        LGPLv3
URL:            https://github.com/stranskyjan/photo-calendar
Source:         %{pypi_source photo-calendar}

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
Photo Calendar is a Python tool that allows you to create personalized calendars with your own photos}


%description %_description

%package -n     python3-photo-calendar
Summary:        %{summary}

%description -n python3-photo-calendar %_description


%prep
%autosetup -p1 -n photo-calendar-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python3-photo-calendar -f %{pyproject_files}


%changelog
* Fri Mar 24 2023 Jasmin Marwad <jasminmarwad@gmail.com> - 0.1.1-1
- Initial package
