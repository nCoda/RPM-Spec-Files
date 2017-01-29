%global _basename contexter


Name:           python2-%{_basename}
Version:        0.1.3
Release:        1
Summary:        Contexter is a full replacement of the contextlib standard library module.

Group:          Applications/Multimedia
License:        MIT
URL:            https://bitbucket.org/defnull/contexter
Source0:        %{_basename}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel


%description
Contexter is a full replacement of the contextlib standard library module. It comes with more
features, a nicer API and full support for Python 2.5 up to 3.x from a single source file.


%prep
%autosetup -n %{_basename}-%{version}


%build
%py2_build


%install
%py2_install


%files
%doc README.rst
%{python2_sitelib}/%{_basename}.py
%{python2_sitelib}/%{_basename}.pyc
%{python2_sitelib}/%{_basename}.pyo
%{python2_sitelib}/%{_basename}-%{version}-py2.7.egg-info/


%changelog
* Sun Jan 29 2017 Christopher Antila <christopher.antila@ncodamusic.org> - 0.1.3-1
- Initial packaging.
