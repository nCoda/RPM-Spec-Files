Name:           mercurial-hug
Version:        0.4.3
Release:        1
Summary:        A wrapper for select Mercurial functionality.

License:        GPLv3+
URL:            https://goldman.ncodamusic.org/diffusion/HUG/
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  pytest
BuildRequires:  mercurial >= 3

%if 0%{?fedora}
BuildRequires:  python-mock
%else
BuildRequires:  python2-mock
%endif

Requires:       mercurial >= 3

%description
This library provides a wrapper around select Mercurial functionality. We aim for the wrapper to be
friendlier to use than Mercurial itself (the libraries, that is, which are largely undocumented) and
also to provide a stable API. To achieve this, we will implement *only* the functionality we need,
and if you ask nicely we might also implement the functionality you need too.


%prep
%autosetup


%build
%py2_build


%check
PYTHONPATH=%{buildroot}%{python2_sitelib} py.test tests


%install
%py2_install


%files
%license LICENSE
%doc README.rst
%{python2_sitelib}/hug
%{python2_sitelib}/mercurial_hug-%{version}-py2.7.egg-info


%changelog
* Sat Feb 4 2017 Christopher Antila <chrisotpher@ncodamusic.org> - 0.4.3-1
- Upgrade to release 0.4.3.
- Improve the specfile.

* Wed May 25 2016 Christopher Antila <christopher@ncodamusic.org> - 0.4.2-2
- Modify "files" section so, you know, Fedora.

* Wed May 25 2016 Christopher Antila <christopher@ncodamusic.org> - 0.4.2-1
- Okay... *now* it'll work in Fedora... right?

* Wed May 25 2016 Christopher Antila <christopher@ncodamusic.org> - 0.4.1-4
- Now it'll work in Fedora?

* Wed May 25 2016 Christopher Antila <christopher@ncodamusic.org> - 0.4.1-3
- Reorganize spec and use better macros.

* Wed May 25 2016 Christopher Antila <christopher@ncodamusic.org> - 0.4.1-2
- Support Fedora (?)

* Wed May 25 2016 Christopher Antila <christopher@ncodamusic.org> - 0.4.1-1
- Initial packagement.
