Name:           python-redislite
Version:        6.2.805324
Release:        1%{?dist}
Summary:        Redis built into a python package

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            https://github.com/yahoo/redislite
Source:         %{pypi_source redislite}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'redislite' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-redislite
Summary:        %{summary}

%description -n python3-redislite %_description


%prep
%autosetup -p1 -n redislite-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python3-redislite -f %{pyproject_files}


%changelog
* Mon Apr 10 2023 Omran Khan - 6.2.805324-1
- Initial package