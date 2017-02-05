# TODO: tests
# TODO: build and package docs

%global _basename lychee


Name:           python2-%{_basename}
Version:        0.5.3
Release:        2
Summary:        Lychee is an engine for MEI document management and conversion.

Group:          Applications/Multimedia
License:        AGPLv3+
URL:            https://goldman.ncodamusic.org/diffusion/FJ/
Source0:        %{_basename}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  mercurial-hug > 0.4
BuildRequires:  python2-abjad == 2.17
BuildRequires:  python2-devel
BuildRequires:  python2-grako >= 3.14
BuildRequires:  python2-lithoxyl >= 0.4
BuildRequires:  python2-signalslot
BuildRequires:  python2-pytest

Requires:       mercurial-hug > 0.4
Requires:       python2-abjad == 2.17
Requires:       python2-grako >= 3.14
Requires:       python2-lithoxyl >= 0.4
Requires:       python2-signalslot

%if 0%{?fedora} >= 25
BuildRequires:  python2-lxml
Requires:       python2-lxml
%else
BuildRequires:  python-lxml
Requires:       python-lxml
%endif


%description
Lychee is an engine for MEI document management and conversion.


%prep
%autosetup -n %{_basename}-%{version}


%build
# replace the Grako-generated parser to make sure it's using the same version we have
grako -c -o lychee/converters/inbound/lilypond_parser.py lychee/converters/inbound/lilypond.ebnf
%py2_build


# %check
# PYTHONPATH=%{buildroot}%{python2_sitelib} py.test


%install
%py2_install


%files
%license LICENSE
%doc README.md
%{python2_sitelib}/%{_basename}/
%{python2_sitelib}/Lychee-%{version}-py2.7.egg-info/


%changelog
* Sat Feb 4 2017 Christopher Antila <christopher.antila@ncodamusic.org> - 0.5.3-2
- Fix the "requires" on Lithoxyl.

* Sun Jan 29 2017 Christopher Antila <christopher.antila@ncodamusic.org> - 0.5.3-1
- Initial packaging.
