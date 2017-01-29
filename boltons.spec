%global _basename boltons


Name:           python2-%{_basename}
Version:        17.0.0
Release:        1
Summary:        Functionality that should be in the standard library. Like builtins, but Boltons.

Group:          Applications/Multimedia
License:        BSD
URL:            https://github.com/mahmoud/boltons
Source0:        %{_basename}-%{version}.zip

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-pytest
BuildRequires:  python2-pytest-cov


%description
Functionality that should be in the standard library. Like builtins, but Boltons.


%prep
%autosetup -n %{_basename}-%{version}


%build
%py2_build


%check
PYTHONPATH=%{buildroot}%{python2_sitelib} py.test


%install
%py2_install


%files
%license LICENSE
%doc README.md
%{python2_sitelib}/%{_basename}/
%{python2_sitelib}/%{_basename}-%{version}-py2.7.egg-info/


%changelog
* Sun Jan 29 2017 Christopher Antila <christopher.antila@ncodamusic.org> - 17.0.0-1
- Initial packaging.
