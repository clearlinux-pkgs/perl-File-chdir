#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-chdir
Version  : 0.1011
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/File-chdir-0.1011.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/File-chdir-0.1011.tar.gz
Summary  : 'a more sensible way to change directories'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-File-chdir-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
File::chdir - a more sensible way to change directories
VERSION
version 0.1011

%package dev
Summary: dev components for the perl-File-chdir package.
Group: Development
Provides: perl-File-chdir-devel = %{version}-%{release}
Requires: perl-File-chdir = %{version}-%{release}

%description dev
dev components for the perl-File-chdir package.


%package perl
Summary: perl components for the perl-File-chdir package.
Group: Default
Requires: perl-File-chdir = %{version}-%{release}

%description perl
perl components for the perl-File-chdir package.


%prep
%setup -q -n File-chdir-0.1011
cd %{_builddir}/File-chdir-0.1011

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::chdir.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
