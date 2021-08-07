Name: procinfo
Version: 18
Release: 43
Summary: A tool for displaying system information
License: GPL+
Source: ftp://ftp.cistron.nl/pub/people/00-OLD/svm/procinfo-%{version}.tar.gz
Patch0: procinfo-14-misc.patch
Patch3: procinfo-17-mandir.patch
Patch5: procinfo-17-uptime.patch
Patch6: procinfo-17-lsdev.patch
Patch7: procinfo-18-acct.patch
Patch8: procinfo-18-mharris-use-sysconf.patch
Patch9: procinfo-18-maxdev.patch
Patch10: procinfo-18-ranges.patch
Patch11: procinfo-18-cpu-steal.patch
Patch12: procinfo-18-intr.patch
Patch13: procinfo-18-intrprint.patch
Patch14: procinfo-18-version.patch
Patch15: procinfo-18-man-comment.patch
Patch16: procinfo-18-socklist.patch
Patch17: procinfo-18-idle-overflow.patch
Patch18: procinfo-strsignal.patch

BuildRequires:  ncurses-devel gcc

%package help
Summary: Documentation for procinfo

%description
This package provides tools for displaying information about the system.
It is easy to install and use it.

%description help
This package contains documentation for procinfo.

%prep
%setup -q
%patch0 -p1
%patch3 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p0
%patch17 -p1
%patch18 -p1

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS -I/usr/include/ncurses" LDFLAGS= LDLIBS=-lncurses

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man8
make install prefix=$RPM_BUILD_ROOT/usr mandir=$RPM_BUILD_ROOT/%{_mandir}

%files
%doc CHANGES README
%{_bindir}/procinfo
%{_bindir}/socklist
%{_bindir}/lsdev

%files help
%{_mandir}/man8/lsdev.8*
%{_mandir}/man8/procinfo.8*
%{_mandir}/man8/socklist.8*

%changelog
* Sat Aug 07 2021 caodongxia<caodongxia@huawei.com> - 18-43
- Use strsignal not sys_siglist

* Thu Feb 13 2020 openEuler Buildteam <buildteam@openeuler.org> - 18-42
- DESC:update the spec
