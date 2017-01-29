# TODO: get the tests to run (requires "eventlet")

%global _basename signalslot


Name:           python2-%{_basename}
Version:        0.1.1
Release:        1
Summary:        Simple Signal/Slot implementation

Group:          Applications/Multimedia
License:        MIT
URL:            https://github.com/numergy/signalslot
Source0:        %{_basename}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-contexter
BuildRequires:  python2-devel
BuildRequires:  python2-pytest
BuildRequires:  python-pytest-cov
BuildRequires:  python-pytest-pep8
BuildRequires:  python-six
BuildRequires:  python2-weakrefmethod

Requires:       python2-contexter
Requires:       python-six
Requires:       python2-weakrefmethod


%description
This package provides a simple and stupid implementation of the Signal/Slot pattern for Python.
Wikipedia has a nice introduction:

> Signals and slots is a language construct introduced in Qt for communication between objects
> which makes it easy to implement the Observer pattern while avoiding boilerplate code.

Rationale against Signal/Slot is detailed in the “Pattern” section of the documentation.


%prep
%autosetup -n %{_basename}-%{version}


%build
%py2_build


# %check
# PYTHONPATH=%{buildroot}%{python2_sitelib} py.test


%install
%py2_install


%files
%doc README.rst
%{python2_sitelib}/%{_basename}/
%{python2_sitelib}/%{_basename}-%{version}-py2.7.egg-info/


%changelog
* Sun Jan 29 2017 Christopher Antila <christopher.antila@ncodamusic.org> - 0.1.1-1
- Initial packaging.
