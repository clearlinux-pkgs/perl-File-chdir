#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-chdir
Version  : 0.1010
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/File-chdir-0.1010.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/File-chdir-0.1010.tar.gz
Summary  : 'a more sensible way to change directories'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-chdir-license = %{version}-%{release}
Requires: perl-File-chdir-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
File::chdir - a more sensible way to change directories
VERSION
version 0.1010

%package dev
Summary: dev components for the perl-File-chdir package.
Group: Development
Provides: perl-File-chdir-devel = %{version}-%{release}
Requires: perl-File-chdir = %{version}-%{release}

%description dev
dev components for the perl-File-chdir package.


%package license
Summary: license components for the perl-File-chdir package.
Group: Default

%description license
license components for the perl-File-chdir package.


%package perl
Summary: perl components for the perl-File-chdir package.
Group: Default
Requires: perl-File-chdir = %{version}-%{release}

%description perl
perl components for the perl-File-chdir package.


%prep
%setup -q -n File-chdir-0.1010
cd %{_builddir}/File-chdir-0.1010

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
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-chdir
cp %{_builddir}/File-chdir-0.1010/LICENSE %{buildroot}/usr/share/package-licenses/perl-File-chdir/a587d626817be6e888f4a52291d03415d3d02b81
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-chdir/a587d626817be6e888f4a52291d03415d3d02b81

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
