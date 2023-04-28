%global pypi_name nicegui
%global pypi_version 1.2.6

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Python-based UI framework which shows up in your web browser.

License:        MIT
URL:            https://github.com/zauberzeug/nicegui
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
NiceGUI is an easy-to-use, Python-based UI framework, which shows up in your web
browser. You can create buttons, dialogs, Markdown, 3D scenes, plots and much
more.

%package -n     python3-%{pypi_name}

Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       (python3dist(fastapi) >= 0.92 with python3dist(fastapi) < 0.93~~)
Requires:       (python3dist(fastapi-socketio) >= 0.0.10 with python3dist(fastapi-socketio) < 0.0.11~~)
Requires:       (python3dist(importlib-metadata) >= 6 with python3dist(importlib-metadata) < 7~~)
Requires:       (python3dist(jinja2) >= 3.1.2 with python3dist(jinja2) < 4~~)
Requires:       (python3dist(markdown2) >= 2.4.7 with python3dist(markdown2) < 3~~)
Requires:       (python3dist(matplotlib) >= 3.5 with python3dist(matplotlib) < 4~~)
Requires:       (python3dist(matplotlib) >= 3.6 with python3dist(matplotlib) < 4~~)
Requires:       (python3dist(orjson) >= 3.8.6 with python3dist(orjson) < 4~~)
Requires:       (python3dist(plotly) >= 5.13 with python3dist(plotly) < 6~~)
Requires:       (python3dist(pygments) >= 2.9 with python3dist(pygments) < 3~~)
Requires:       (python3dist(python-multipart) >= 0.0.6 with python3dist(python-multipart) < 0.0.7~~)
Requires:       (python3dist(pywebview) >= 4.0.2 with python3dist(pywebview) < 5~~)
Requires:       python3dist(typing-extensions) >= 3.10
Requires:       (python3dist(uvicorn) >= 0.20 with python3dist(uvicorn) < 0.21~~)
Requires:       (python3dist(vbuild) >= 0.8.1 with python3dist(vbuild) < 0.9~~)
Requires:       (python3dist(watchfiles) >= 0.18.1 with python3dist(watchfiles) < 0.19~~)
%description -n python3-%{pypi_name}
NiceGUI is an easy-to-use, Python-based UI framework, which shows up in your web
browser. You can create buttons, dialogs, Markdown, 3D scenes, plots and much
more.

%prep
%autosetup -n %{pypi_name}-%{pypi_version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Thu Apr 06 2023 Jasmin - 1.2.6-1
- Initial package.

