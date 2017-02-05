%global _basename ncoda
%global _hardened_build 1
%global debug_package %{nil}
%global __provides_exclude (libnode)
%global __requires_exclude (libnode|ffmpeg)


Name:           nCoda
Version:        1702.4.0
Release:        1
Summary:        nCoda itself.

Group:          Applications/Multimedia
License:        AGPLv3+
URL:            https://ncodamusic.org/
Source0:        %{_basename}-%{version}.tar.gz

BuildRequires:  nodejs
BuildRequires:  web-assets-devel

Requires:       libjulius
Requires:       python2-fujian
Requires:       python2-lychee
Requires:       web-assets-filesystem


%description
nCoda itself.


%prep
%autosetup -n %{_basename}-%{version}


%build
npm install


%install
mkdir -p %{buildroot}%{_libdir}/%{_basename}
cp -R node_modules %{buildroot}%{_libdir}/%{_basename}
mkdir -p %{buildroot}%{_bindir}
cp %{_basename} %{buildroot}%{_bindir}
chmod u=rwx,g=rx,o=rx %{buildroot}%{_bindir}/%{_basename}


%files
%{_bindir}/%{_basename}
%{_libdir}/%{_basename}


%changelog
* Sat Feb 4 2017 Christopher Antila <christopher.antila@ncodamusic.org> - 1702.0.4
- Initial packaging.
