# TODO: compile and ship docs
# TODO: ship demos and boilerplate
# TODO: enable the test suite


Name:           python2-abjad
Version:        2.17
Release:        2
Summary:        Abjad is a Python API for Formalized Score Control

Group:          Applications/Multimedia
License:        GPLv3
URL:            http://abjad.mbrsi.org/
Source0:        abjad-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-enum34
BuildRequires:  python2-mock
BuildRequires:  python2-ply
BuildRequires:  python2-pytest
BuildRequires:  python-six

Requires:       lilypond
Requires:       python-enum34
Requires:       python2-ply
Requires:       python-six


%description
Abjad helps composers build up complex pieces of music notation in an iterative and incremental way.
Use Abjad to create symbolic representations of all the notes, rests, staves, tuplets, beams and
slurs in any score. Because Abjad extends the Python programming language, you can use Abjad to
make systematic changes to your music as you work. And because Abjad wraps the powerful LilyPond
music notation package, you can use Abjad to control the typographic details of the symbols on
the page.


%prep
%autosetup -n abjad-%{version}
# NB: we can't ship this because setup.py tries to bytecompile it but it's not valid Python
rm -R abjad/boilerplate


%build
%py2_build


# %check
# PYTHONPATH=%{buildroot}%{python2_sitelib} py.test


%install
%py2_install


%files
%license LICENSE
%doc README.rst
%{_bindir}/abjad
%{_bindir}/ajv
%{python2_sitelib}/abjad/
%{python2_sitelib}/Abjad-%{version}-py2.7.egg-info/


%changelog
* Sun Jan 29 2017 Christopher Antila <christopher.antila@ncodamusic.org> - 2.17-3
- Remove "requires" on python2-pathlib2.

* Sun Jan 29 2017 Christopher Antila <christopher.antila@ncodamusic.org> - 2.17-2
- Add "requires" on LilyPond.

* Sat Jan 28 2017 Christopher Antila <christopher.antila@ncodamusic.org> - 2.17-1
- Initial packaging.
