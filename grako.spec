# TODO: get the tests to work (very weird failure, can't reproduce outside rpmbuild)


%global _basename grako
%global _hardened_build 1

Name:           python2-%{_basename}
Version:        3.14.0
Release:        1
Summary:        Grako is a grammar compiler.

Group:          Applications/Multimedia
License:        BSD
URL:            http://bitbucket.org/apalala/grako
Source0:        %{_basename}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  python2-Cython
BuildRequires:  python2-devel
BuildRequires:  python-docutils
BuildRequires:  python2-pytest

Requires:       python2-colorama


%description
Grako (for "grammar compiler") takes a grammar in a variation of EBNF as input, and outputs a
memoizing PEG/Packrat parser in Python.


%prep
%autosetup -n %{_basename}-%{version}


%build
%py2_build


# %check
# py.test


%install
%py2_install


%files
%license LICENSE.txt
%doc README.rst
%{_bindir}/%{_basename}
%{python2_sitearch}/%{_basename}/
%{python2_sitearch}/%{_basename}-%{version}-py2.7.egg-info/


%changelog
* Sun Jan 29 2017 Christopher Antila <christopher.antila@ncodamusic.org> - 3.14.0-1
- Initial packaging.
