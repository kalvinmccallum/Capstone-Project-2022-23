Name:           python-usb-resetter
Version:        1.3.0
Release:        1%{?dist}
Summary:        small tool to reset USB controllers, hubs or devices

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD
URL:            https://github.com/netinvent/udev_monitor
Source:         %{pypi_source usb_resetter}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'usb-resetter' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-usb-resetter
Summary:        %{summary}

%description -n python3-usb-resetter %_description


%prep
%autosetup -p1 -n usb_resetter-%{version}


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


%files -n python3-usb-resetter -f %{pyproject_files}


%changelog
* Mon Apr 10 2023 Omran Khan - 1.3.0-1
- Initial package