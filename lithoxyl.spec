%global _basename lithoxyl


Name:           python2-%{_basename}
Version:        0.4.0
Release:        1
Summary:        A systematic approach to logging, profiling, and statistics collection.

Group:          Applications/Multimedia
License:        BSD
URL:            https://github.com/mahmoud/lithoxyl
Source0:        %{_basename}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-boltons
BuildRequires:  python2-devel
BuildRequires:  python2-pytest

Requires:       python2-boltons >= 16.5.0


%description
A systematic approach to application instrumentation, including logging, semantic profiling,
and statistics collection. Very lightweight, very Pythonic.


%prep
%autosetup -n %{_basename}-%{version}


%build
%py2_build


%check
PYTHONPATH=%{buildroot}%{python2_sitelib} py.test build


%install
%py2_install


%files
%{python2_sitelib}/%{_basename}/
%{python2_sitelib}/%{_basename}-%{version}-py2.7.egg-info/


%changelog
* Sun Jan 29 2017 Christopher Antila <christopher.antila@ncodamusic.org> - 0.4.0-1
- Initial packaging.
