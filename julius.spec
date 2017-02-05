%global _basename julius


Name:           lib%{_basename}
Version:        0.1.2
Release:        1
Summary:        The user interface of nCoda.

Group:          Applications/Multimedia
License:        AGPLv3+
URL:            https://goldman.ncodamusic.org/diffusion/JL/
Source0:        %{_basename}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  web-assets-devel
BuildRequires:  nodejs

Requires:       web-assets-filesystem
Requires:       fontawesome-fonts
Requires:       mozilla-fira-mono-fonts
Requires:       mozilla-fira-sans-fonts


%description
The user interface of nCoda.


%prep
%autosetup -n %{_basename}-%{version}
npm install


%build
export NODE_ENV="production"
mkdir build
node_modules/.bin/lessc css/ncoda/main.less build/main.css
node_modules/.bin/browserify js/ncoda-init.js -o build/ncoda.js


%check
npm test


%install
mkdir -p %{buildroot}%{_webassetdir}/%{_basename}
cp build/main.css %{buildroot}%{_webassetdir}/%{_basename}/main.css
cp build/ncoda.js %{buildroot}%{_webassetdir}/%{_basename}/ncoda.js
cp lib/diff_match_patch.js %{buildroot}%{_webassetdir}/%{_basename}/diff_match_patch.js
cp node_modules/codemirror/lib/codemirror.css %{buildroot}%{_webassetdir}/%{_basename}/codemirror.css
cp node_modules/codemirror/addon/merge/merge.css %{buildroot}%{_webassetdir}/%{_basename}/codemirror-merge.css
cp css/lib/vida.css %{buildroot}%{_webassetdir}/%{_basename}/vida.css
cp index-fedora.html %{buildroot}%{_webassetdir}/%{_basename}/index.html



%files
%{_webassetdir}/%{_basename}/


%changelog
* Sat Feb 4 2017 Christopher Antila <christopher.antila@ncodamusic.org> - 0.1.2-1
- Initial packaging.
