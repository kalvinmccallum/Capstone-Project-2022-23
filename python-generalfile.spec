Name:           python-generalfile
Version:        2.5.14
Release:        1%{?dist}
Summary:        Easily manage files cross platform.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/ManderaGeneral/generalfile
Source:         %{pypi_source generalfile}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'generalfile' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-generalfile
Summary:        %{summary}

%description -n python3-generalfile %_description


%prep
%autosetup -p1 -n generalfile-%{version}


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


%files -n python3-generalfile -f %{pyproject_files}


%changelog
* Sun Apr 02 2023 Omran Khan - 2.5.14-1
- Initial package