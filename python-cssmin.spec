Name:           python-cssmin
Version:        0.2.0
Release:        1%{?dist}
Summary:        A Python port of the YUI CSS compression algorithm.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        UNKNOWN
URL:            http://github.com/zacharyvoase/cssmin
Source:         %{pypi_source cssmin}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'cssmin' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-cssmin
Summary:        %{summary}

%description -n python3-cssmin %_description


%prep
%autosetup -p1 -n cssmin-%{version}


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


%files -n python3-cssmin -f %{pyproject_files}


%changelog
* Mon Apr 17 2023 Soumil Kadam - 0.2.0-1
- Initial package