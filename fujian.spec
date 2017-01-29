Name:           python2-fujian
Version:        1.1.1
Release:        1
Summary:        An HTTP server that executes Python code.

Group:          Applications/Multimedia
License:        AGPLv3+
URL:            https://goldman.ncodamusic.org/diffusion/FJ/
Source0:        fujian-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2-pytest
BuildRequires:  python2-tornado

Requires:       python2-tornado


%description
It's simple: Fujian accepts Python code in the request body of a PUT request, executes the code,
then returns the result.

The server is named after Fujian (福建) Province of the Peopl's Republic of China. The intention is
to use it with our "lychee" software ("litchi" package on PyPI). Lychees are a fruit that grow in
southern China. Fujian is a province in southern China. If you're importing lychee (and we do indeed
want to ``import lychee``) they're probably coming from southern China.

Do note that this application opens the door to a wide range of security issues that we don't plan
to address. Fujian is intended for use on ``localhost`` only. Opening it up to the public Internet
is a tremendously bad idea!

Fujian already supports Python 3, and we will add support for PyPy3 when the time comes.


%prep
%autosetup -n fujian-%{version}


%build
%py2_build


%check
PYTHONPATH=%{buildroot}%{python2_sitelib} py.test


%install
%py2_install


%files
%license LICENSE
%doc README.rst
%{python2_sitelib}/fujian/
%{python2_sitelib}/Fujian-%{version}-py2.7.egg-info/


%changelog
* Sun Jan 29 2017 Christopher Antila <christopher.antila@ncodamusic.org> - 1.1.1-1
- Initial packaging.
