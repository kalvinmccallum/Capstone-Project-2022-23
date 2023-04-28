Name:           python-show-in-file-manager
Version:        1.1.4
Release:        1%{?dist}
Summary:        Open the system file manager and select files in it

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/damonlynch/showinfilemanager
Source:         %{pypi_source show-in-file-manager}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'show-in-file-manager' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-show-in-file-manager
Summary:        %{summary}

%description -n python3-show-in-file-manager %_description


%prep
%autosetup -p1 -n show-in-file-manager-%{version}


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


%files -n python3-show-in-file-manager -f %{pyproject_files}


%changelog
* Sun Apr 02 2023 Omran Khan - 1.1.4-1
- Initial package